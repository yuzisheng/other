import json
from math import exp, sqrt, pow


class YileiNie:
    def __init__(self, params_file_path):
        """
        所有指定参数存在JSON文件中统一进行读取
        """
        params = json.load(open(params_file_path))
        self.T_0_t = params["T_0_t"]  # 郊区气象站所测得的逐时平均温度 (长度为24的列表)
        self.phi_a_t = params["phi_a_t"]  # 所在区气候区典型气象日的空气相对湿度 (长度为24的列表)
        self.PSA_t = params["PSA_t"]  # 设计地块范围空地上建筑的逐时阴影率 (长度为24的列表)
        self.I_0_t = params["I_0_t"]  # 水平面太阳总辐射照度 (长度为24的列表)
        self.I_dif_t = params["I_dif_t"]  # 水平散射辐射照度 (长度为24的列表)
        self.F_1to8 = params["F_1to8"]  # 面积 (长度为8的列表)
        self.m_1to8 = params["m_1to8"]  # 类下垫面的太阳辐射吸收系数: 普通水泥, 普通沥青, 透水砖, 透水沥青, 植草砖, 草地, 草灌草地, 草地 (长度为8的列表)
        self.green = params["green"]  # 是否存在绿化 (布尔值: true/false)
        self.SVF = params["SVF"]  # 设计地块范围内空地的平均天空角系数 (浮点数)
        self.f_L = params["f_L"]  # 设计地块范围内空地的绿化遮阳覆盖率 (浮点数)
        self.xi_L = params["xi_L"]  # 设计地块范围内空地的平均太阳辐射透射比 (浮点数)
        self.c_L = params["c_L"]  # 绿化遮阳的对流得热比例 (浮点数)
        self.V_t = params["V_t"]  # 场内的平均风速 (浮点数)
        self.sum_F_Qi = params["sum_F_Qi"]  # 设计地块上逐个乔木树冠的垂直投影面积总和 (浮点数)
        self.F_BL = params["F_BL"]  # 商业区累计建筑立面面积 (浮点数)
        self.F_B = params["F_B"]  # 设计地块范围上累计建筑基底面积 (浮点数)
        self.S_0 = params["S_0"]  # 设计地块范围的面积 (浮点数)
        self.CTTC_D = params["CTTC_D"]  # 商业区空地热时间常数 (浮点数)
        self.CTTC_B = params["CTTC_B"]  # 商业区建筑热时间常数 (浮点数)
        self.CTTC_Q = params["CTTC_Q"]  # 商业区乔木热时间常数 (浮点数)
        self.sigma = params["sigma"]  # Stefan-Boltzmann常数 (浮点数)

    def cal_delta_Ta_solar_t(self):
        """
        :return: 计算太阳辐射升温delta_Ta_solar_t
        """
        # step 1: 计算商业区地表的平均太阳辐射吸收系数m, 即各类下垫面的平均太阳辐射吸收系数的加权平均值
        assert len(self.m_1to8) == len(self.F_1to8)
        m = sum([self.m_1to8[_] * self.F_1to8[_] for _ in range(len(self.m_1to8))]) / sum(self.F_1to8)

        # step 2: 计算设计地块范围太阳辐射照度的阶跃量delta_Ipen_lambda
        assert len(self.I_0_t) == len(self.I_dif_t) == len(self.PSA_t)
        if self.green:
            # 若存在绿化
            temp = [(self.I_0_t[_] - self.I_dif_t[_]) * (1 - self.PSA_t[_]) + self.I_dif_t[_] * self.SVF for _ in
                    range(len(self.I_0_t))]
            Ipen_t = [_ * (1 - self.f_L * ((1 - self.xi_L) * (1 - self.c_L))) for _ in range(len(temp))]
            pass
        else:
            # 若不存在绿化
            Ipen_t = [(self.I_0_t[_] - self.I_dif_t[_]) * (1 - self.PSA_t[_]) for _ in range(len(self.I_0_t))]
        delta_Ipen_lambda = [Ipen_t[_] - Ipen_t[_ - 1] for _ in range(1, len(Ipen_t))].append(0)

        # step 3: 计算地表平均换热系数h
        h = 9.8 + 4.1 * self.V_t

        # step 4: 计算场地内平均热时间常数CTTC
        CTTC = (1 - (self.F_B + self.sum_F_Qi) / self.S_0) * self.CTTC_D + (self.F_BL / self.S_0) * self.CTTC_B + (
                self.sum_F_Qi / self.S_0) * self.CTTC_Q

        # 计算并返回最终结果
        delta_Ta_solar_t = []
        for t in range(24):
            delta_Ta_solar_t.append(
                sum([(m * delta_Ipen_lambda[_] / h) * (1 - exp(-(t - _) / CTTC)) for _ in range(t + 1)]))

        return delta_Ta_solar_t

    def cal_delta_T_NLWR_t(self):
        """
        :return: 计算长波辐射降温delta_T_NLWR_t
        """
        # step 1: 指定sigma
        # step 2: 指定T_0_t
        # step 3: 计算B_r_t
        # 所在区气候区典型气象日的水蒸气分压力P_a_t
        P_a_t = [self.phi_a_t[_] * exp(23.5612 - 4030 / (self.T_0_t[_] + 235)) for _ in range(len(self.phi_a_t))]
        B_r_t = [0.51 + 0.076 * sqrt(P_a_t[_]) for _ in range(len(P_a_t))]
        # step 4: 指定设计地块范围内空地的平均天空角系数SVF
        # step 5: 计算地表平均换热系数h
        h = 9.8 + 4.1 * self.V_t

        # 计算并返回最终结果
        delta_T_NLWR_t = [self.sigma * pow(self.T_0_t[_] + 273, 4) * (1 - B_r_t[_]) * (self.SVF - h) for _ in
                          range(len(B_r_t))]
        return delta_T_NLWR_t

    def cal_T_a(self):
        """
        :return: 计算并返回最终结果
        """
        delta_Ta_solar_t = self.cal_delta_Ta_solar_t()
        delta_T_NLWR_t = self.cal_delta_T_NLWR_t()
        assert len(self.T_0_t) == len(delta_Ta_solar_t) == len(delta_T_NLWR_t) == 24  # 保证三列表长度相同
        T_a = [self.T_0_t[_] + delta_Ta_solar_t[_] - delta_T_NLWR_t[_] for _ in range(len(self.T_0_t))]
        return T_a


if __name__ == '__main__':
    # 聂一蕾需求
    nie = YileiNie("nie.json")
    print(nie.cal_T_a())
    print("ok")
