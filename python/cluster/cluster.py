import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def load_data(data_path):
    """
    读取指定目录下的所有数据文件
    :param data_path: 数据存放目录
    :return: data_list: 列表中每个元素为一个矩阵
    """
    list_data = []
    file_name = []
    for info in os.listdir(data_path):
        file_name.append(info)
        domain = os.path.abspath(data_path)
        info = os.path.join(domain, info)
        # 矩阵以浮点数的形式读入,并保存为numpy的矩阵格式
        data = np.loadtxt(info, dtype=np.float32)
        list_data.append(data)
    print("++ load data done")
    return list_data, file_name


def save_cluster(list_cluster, list_info):
    """
    保存聚类之后的结果(以txt形式保存与原先矩阵大小一致的聚类后的矩阵),默认路径为程序执行路径
    :param list_cluster: 聚类后的矩阵数据列表
    :param list_info: 文件的名称列表
    :return:
    """
    for i in range(len(list_cluster)):
        # 例如:D:/data/point_cluster.txt
        save_path = list_info[i].split(".")[0] + "_cluster.txt"
        # 元素保存为整数的格式
        np.savetxt(save_path, list_cluster[i], fmt="%d")


def equal_width_cluster(data, k, file_name, if_visualize=False):
    """
    等宽离散化:将属性从最小值到最大值分成具有相同宽度的k个区间
    :param data: 矩阵
    :param k: 区间数
    :param file_name: 文件名称,用来保存可视化结果
    :param if_visualize: 是否可视化
    :return: 离散化之后的结果(与原矩阵大小相同)
    """
    # 对原矩阵进行一份拷贝
    data_copy = data.copy()
    # 将二维数据转为一维(直接拉平)
    data_one_dim = np.squeeze(data_copy.reshape(-1, 1))  # (n, )
    # 求矩阵的最大最小值和区间大小
    min_value = np.min(data)
    max_value = np.max(data)
    interval = (max_value - min_value) / k
    # 离散化:标号从0到k-1,共k个类别
    # 初始化一个一维空矩阵
    cluster_data_one_dim = np.empty(data_one_dim.shape, dtype=np.int32)
    # 遍历矩阵
    for i in range(len(data_one_dim)):
        # 若是最大值则标号为(k-1),主要为了防止出现浮点数误差导致出现(k+1)个类别
        if data_one_dim[i] == max_value:
            cluster_data_one_dim[i] = k - 1
        else:
            cluster_data_one_dim[i] = int((data_one_dim[i] - min_value) / interval)
    # 还原到原来的二维矩阵
    cluster_data = cluster_data_one_dim.reshape(data.shape)
    # 是否进行可视化
    if if_visualize:
        plt.subplot(121)
        plt.scatter(data_one_dim, [0] * len(data_one_dim))
        plt.title("raw data")
        plt.subplot(122)
        plt.scatter(data_one_dim, [0] * len(data_one_dim), c=cluster_data_one_dim)
        plt.title("equal width cluster")
        plt.savefig(file_name.split(".")[0] + "_visualize.jpg")
        # plt.show()
    # 返回结果
    return cluster_data


def equal_freq_cluster(data, k, file_name, if_visualize=False):
    """
    等频离散化:将属性从最小值到最大值分成具有相同元素个数的k个区间
    :param data: 矩阵
    :param k: 区间数
    :param file_name: 文件名称,用来保存可视化结果
    :param if_visualize: 是否可视化
    :return: 离散化之后的结果(与原矩阵大小相同)
    """
    # 对原矩阵进行一份拷贝
    data_copy = data.copy()
    # 将二维数据转为一维(直接拉平)
    data_one_dim = np.squeeze(data_copy.reshape(-1, 1))  # (n,)
    # 排序,便于找到百分位切分点
    data_one_dim_sort = np.sort(data_one_dim)
    # bins列表保存的是每个切分百分位点的值
    bins_list = []
    for i in range(k):
        bins_list.append(data_one_dim_sort[int((i / k) * len(data_one_dim_sort))])
    # 最后一个值应为矩阵最大值,为防止出现边界问题,直接设为无穷大inf
    bins_list.append(np.inf)
    # 打印bins_list
    # print(bins_list)
    # 离散化:标号从0到k-1,共k个类别
    # 初始化一个一维空矩阵
    cluster_data_one_dim = np.empty(data_one_dim.shape, dtype=np.int32)
    for i in range(len(data_one_dim)):
        for j in range(k):
            # 若值在bins_list[j]和bins_list[j+1]之间,则标号为j,j在[0,k-1]之间
            if bins_list[j] <= data_one_dim[i] < bins_list[j + 1]:
                cluster_data_one_dim[i] = j
    # 还原到原来的二维矩阵
    cluster_data = cluster_data_one_dim.reshape(data.shape)
    # 是否进行可视化
    if if_visualize:
        plt.subplot(121)
        plt.scatter(data_one_dim, [0] * len(data_one_dim))
        plt.title("raw data")
        plt.subplot(122)
        plt.scatter(data_one_dim, [0] * len(data_one_dim), c=cluster_data_one_dim)
        plt.title("equal freq cluster")
        plt.savefig(file_name.split(".")[0] + "_visualize.jpg")
        # plt.show()
    # 返回结果
    return cluster_data


def kmeans_cluster(data, cluster_number, file_name, if_visualize=False):
    """
    k-Means要求输入聚类的个数
    :param data: 矩阵
    :param cluster_number: 聚类的个数
    :param if_visualize 是否进行可视化,默认不进行可视化
    :return: 聚类之后的结果(与原矩阵大小相同)
    """
    # 将二维数据转为一维(直接拉平)
    # 例如: [[1, 2], [3, 4]] => [1, 2, 3, 4]
    data_one_dim = data.reshape(-1, 1)
    # 对一维数据进行kmeans聚类
    cluster_predict = KMeans(n_clusters=cluster_number).fit_predict(data_one_dim)
    # 将结果还原为原矩阵大小
    cluster_data = cluster_predict.reshape(data.shape)
    # 是否进行可视化
    if if_visualize:
        plt.subplot(121)
        plt.scatter(data_one_dim, [0] * len(data_one_dim))
        plt.title("raw data")
        plt.subplot(122)
        plt.scatter(data_one_dim, [0] * len(data_one_dim), c=cluster_predict)
        plt.title("kmeans cluster")
        plt.savefig(file_name.split(".")[0] + "_visualize.jpg")
        # plt.show()
    # 返回结果
    return cluster_data


if __name__ == '__main__':
    """
    本程序对指定目录下所有txt文件按照一维进行聚类,并保存结果,并可进行可视化(可选)
    """
    # 设定参数
    data_path = "./data"  # 数据存放绝对路径
    cluster_number = 4  # 聚类的数量k
    if_visualize = True  # 是否进行可视化

    # 第一步:加载数据
    list_data, list_file_name = load_data("./data")
    # 第二步:进行聚类
    list_cluster = []  # 建立一个列表用来保存聚类后的数据
    # 遍历数据进行聚类并保存
    for i in range(len(list_data)):
        # 选取聚类的方法
        # cluster_data = kmeans_cluster(list_data[i], cluster_number, list_file_name[i], if_visualize=if_visualize)
        # cluster_data = equal_width_cluster(list_data[i], cluster_number, list_file_name[i], if_visualize=if_visualize)
        cluster_data = equal_freq_cluster(list_data[i], cluster_number, list_file_name[i], if_visualize=if_visualize)
        # 将聚类结果保存到列表中
        list_cluster.append(cluster_data)
    print("++ cluster done")
    # 第三步:保存聚类结果(txt文件格式,路径为程序执行的路径)
    save_cluster(list_cluster, list_file_name)
    print("++ save cluster done")

    # 结束程序
    print("all done")
