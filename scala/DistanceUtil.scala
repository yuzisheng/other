import scala.collection.mutable.ListBuffer
import scala.math._

object DistanceUtils {
  /**
   * 欧式距离
   */
  def euclideanDistance(p1: (Double, Double), p2: (Double, Double)): Double = {
    sqrt(pow(p1._1 - p2._1, 2) + pow(p1._2 - p2._2, 2))
  }

  /**
   * 曼哈顿距离
   */
  def manhattanDistance(p1: (Double, Double), p2: (Double, Double)): Double = {
    abs(p1._1 - p2._1) + abs(p1._2 - p2._2)
  }

  /**
   * 顶角度数
   */
  def vertexDegree(p: (Double, Double), segment: ((Double, Double), (Double, Double))): Double = {
    val a = euclideanDistance(p, segment._1)
    val b = euclideanDistance(p, segment._2)
    val c = euclideanDistance(segment._1, segment._2)
    acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)).toDegrees
  }

  /**
   * 单点到线的距离
   */
  def singlePoint2Line(p: (Double, Double), line: Seq[(Double, Double)]): Double = {
    line.map(euclideanDistance(p, _)).min
  }

  /**
   * 多点到线的距离
   */
  def multiPoint2Line(pt: Seq[(Double, Double)], line: Seq[(Double, Double)]): Double = {
    (for (p <- pt) yield line.map(euclideanDistance(p, _)).min).sum
  }

  /**
   * Lp Norm: 线线距离 (要求两线长度相等)
   */
  def LpNorm(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)]): Double = {
    assert(line1.size == line2.size)
    (for (p1 <- line1; p2 <- line2) yield euclideanDistance(p1, p2)).sum
  }

  /**
   * LCSS: 最长子序列 线线距离 (要求两线长度相等)
   */
  def longestCommonSubSeq(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)], minDistance: Double): Int = {
    val (n, m) = (line1.length, line2.length)
    val (short_line, long_line) = if (n <= m) (line1, line2) else (line2, line1)
    (for (p1 <- short_line) yield (for (p2 <- long_line) yield euclideanDistance(p1, p2)).min).count(_ <= minDistance)
  }

  /**
   * EDR: 编辑距离 线线距离
   */
  def editDistanceOnRealSeq(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)], minDistance: Double): Double = {
    val (n, m) = (line1.length, line2.length)
    if (n == 0) return 1 - m / max(n, m)
    if (m == 0) return 1 - n / max(n, m)

    val matrix = Array.ofDim[Int](n + 1, m + 1)
    for (i <- 0 to n) matrix(i)(0) = i
    for (j <- 0 to m) matrix(0)(j) = j
    for (i <- 1 to n; j <- 1 to m) {
      val temp = if (euclideanDistance(line1(i - 1), line2(j - 1)) <= minDistance) 0 else 1
      matrix(i)(j) = Seq(matrix(i - 1)(j) + 1, matrix(i)(j - 1) + 1, matrix(i - 1)(j - 1) + temp).min
    }
    // for (i <- 0 to m) println(matrix(i).toList)
    1 - matrix(n)(m).toDouble / max(n, m)
  }

  /**
   * DTW: 线线距离
   */
  def dynamicTimeWarping(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)]): Double = {
    val (n, m) = (line1.length, line2.length)
    if (n == 0 || m == 0) return Double.MaxValue
    val matrix = Array.ofDim[Double](n + 1, m + 1)
    for (i <- 0 to n; j <- 0 to m) {
      val i_1 = i - 1
      if (i == 0 && j == 0) matrix(i)(j) = 0.0
      else if (i == 0 || j == 0) matrix(i)(j) = Double.MaxValue
      else {
        val j_1 = j - 1
        matrix(i)(j) = euclideanDistance(line1(i_1), line2(j_1))
        matrix(i)(j) += Seq(matrix(i_1)(j_1), matrix(i)(j_1), matrix(i_1)(j)).min
      }
    }
    matrix(n)(m)
  }

  /**
   * 豪斯多夫距离: 线线距离
   */
  def hausdorffDistance(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)]): Double = {
    val line1ToLine2 = (for (p1 <- line1) yield (for (p2 <- line2) yield euclideanDistance(p1, p2)).min).max
    val line2ToLine1 = (for (p2 <- line2) yield (for (p1 <- line1) yield euclideanDistance(p1, p2)).min).max
    max(line1ToLine2, line2ToLine1)
  }

  /**
   * 狗绳距离: 线线距离
   */
  def frechetDistance(line1: Seq[(Double, Double)], line2: Seq[(Double, Double)]): Double = {
    def _c(ca: Array[Array[Double]], i: Int, j: Int, P: Seq[(Double, Double)], Q: Seq[(Double, Double)]): Double = {
      if (ca(i)(j) > -1.0) return ca(i)(j)
      else if (i == 0 && j == 0) ca(i)(j) = euclideanDistance(P.head, Q.head)
      else if (i > 0 && j == 0) ca(i)(j) = max(_c(ca, i - 1, 0, P, Q), euclideanDistance(P(i), Q.head))
      else if (i == 0 && j > 0) ca(i)(j) = max(_c(ca, 0, j - 1, P, Q), euclideanDistance(P.head, Q(j)))
      else if (i > 0 && j > 0) ca(i)(j) = max(Seq(_c(ca, i - 1, j, P, Q), _c(ca, i - 1, j - 1, P, Q), _c(ca, i, j - 1, P, Q)).min, euclideanDistance(P(i), Q(j)))
      else ca(i)(j) = Double.MaxValue
      ca(i)(j)
    }

    val (n, m) = (line1.length, line2.length)
    val ca = Array.fill(n, m)(-1.0)
    _c(ca, n - 1, m - 1, line1, line2)
  }

  /**
   * 边角是否在指定范围内
   */
  def withRange(p: (Double, Double), segment: ((Double, Double), (Double, Double)), minDegree: Double): Boolean = {
    vertexDegree(segment._1, (p, segment._2)) <= minDegree && vertexDegree(segment._2, (p, segment._1)) <= minDegree
  }

  /**
   * 基于角度的轨迹与路径相似性计算
   *
   * @return (相似度, 置信度)
   */
  def degreeBasedSimilarity(pt: Seq[(Double, Double)], path: Seq[((Double, Double), (Double, Double))]): (Double, Double) = {
    val segDistance = for (seg <- path) yield euclideanDistance(seg._1, seg._2)
    val segWeight = for (d <- segDistance) yield d / segDistance.sum

    val p2SegDistance = new ListBuffer[Seq[Double]]
    path.foreach(seg => p2SegDistance.append(for (p <- pt; if withRange(p, seg, 90)) yield vertexDegree(p, seg) / 180))

    assert(segWeight.size == p2SegDistance.size)
    var similarity = 0.0
    var confidence = 0.0
    for (i <- p2SegDistance.indices) {
      similarity += ((p2SegDistance(i).sum / p2SegDistance(i).size) * segWeight(i))
      confidence += ((1 - exp(-p2SegDistance(i).size)) * segWeight(i))
    }
    (similarity, confidence)
  }

  def main(args: Array[String]): Unit = {
    println(euclideanDistance((1, 1), (2, 2)))
    println(manhattanDistance((1, 1), (2, 2)))
    println(vertexDegree((0, 1), ((0, 0), (1, 0))))
    println(withRange((-1, 1), ((0, 0), (1, 0)), 90))
    println(degreeBasedSimilarity(Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8), (1.8, 1.2)), Seq(((0, 0), (1, 0)), ((1, 1), (2, 1)))))
    println(editDistanceOnRealSeq(Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8), (1.8, 1.2)), Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8)), 1))
    println(longestCommonSubSeq(Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8), (1.8, 1.2)), Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8)), 1))
    println(longestCommonSubSeq(Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8)), Seq((0.2, 0.2), (0.8, -0.2), (1.2, 0.8), (1.8, 1.2)), 1))
    println(dynamicTimeWarping(Seq((0.2, 0.2), (0.8, -0.2)), Seq((0.2, 0.2), (0.8, -0.2))))
    println(hausdorffDistance(Seq((0.2, 0.2), (0.8, -0.2)), Seq((0.2, 0.2), (0.8, -0.2))))
    println(frechetDistance(Seq((0.2, 0.2), (0.8, -0.2)), Seq((0.2, 0.2), (0.8, -0.2))))
  }

}