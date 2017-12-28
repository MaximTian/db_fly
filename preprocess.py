# coding:utf-8
# @Time : 2017/12/27 19:23
# @Author : yuy


import pandas as pd
import matplotlib.pyplot as plt
import math
from evaluation import Evaluation


class DataProcess(object):
    """对数据进行一些预处理和清洗工作

    """
    def baseline(self):
        """baseline结果
        采用mean进行预测 2.38
        采用median进行预测 2.50

        清洗之后的数据 mean 0.557
                      median 0.575


        :return:
        """
        df = pd.read_csv("new_d_train.csv", encoding="utf-8")
        df_y = pd.DataFrame(df[u"血糖"])
        y_true = df[u"血糖"].values
        y_predict = [df_y.mean().values[0]] * len(df)
        print y_true
        print y_predict
        return Evaluation.get_errors(y_predict, y_true)

    def get_y_range(self):
        """对于血糖进行一些处理

        :return:
        """
        df = pd.read_csv("d_train.csv", encoding="utf-8")
        df_y = pd.DataFrame(df[u"血糖"])
        num1 = len(df_y)
        # 画图发现血糖的分布满足高斯分布
        print math.floor(df_y.min()) * 10
        print math.ceil(df_y.max()) * 10
        df_y.hist(bins=[obj * 0.1 for obj in range(int(math.floor(df_y.min())) * 10, int(math.ceil(df_y.max()) * 10),  1)])
        plt.show()
        # 计算出高斯分布的均值mean和标准差std，从而计算范围区间
        g_mean = df_y.mean().values[0]
        g_std = df_y.std().values[0]
        # 清洗之后的数据集
        # 原来的数据分布是5642条
        # 按照高斯分布进行清洗之后，数据的条数是5427条
        # 血糖浓度范围 2.54 -8.72样本
        # 超出
        g_max = g_mean + 2 * g_std
        g_min = g_mean - 2 * g_std
        print g_max, g_min
        new_df = df[(df[u"血糖"] >= g_min) & (df[u"血糖"] <= g_max)]
        print new_df
        new_df.to_csv("new_d_train.csv", encoding="utf-8")


if __name__ == "__main__":
    d = DataProcess()
    print d.get_y_range()