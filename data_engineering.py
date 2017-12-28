#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
import importlib
import sys
importlib.reload(sys)


def count_row_col_null():
    data = pd.read_csv("d_train.csv")
    n, m = data.shape  # 行数，列数
    col_null = n - data.count()
    row_null = m - data.count(axis=1)
    data["row_null"] = row_null
    data.loc[n + 1] = col_null
    data.to_csv("d_train_null.csv", index=None)


def get_correlation():
    data = pd.read_csv("d_train.csv")
    sex_mapping = {u'男': 0, '女': 1}
    data[u'性别'] = data['性别'].map(sex_mapping)
    data = data.drop(["id", u"乙肝表面抗原", u"乙肝表面抗体", u"乙肝e抗原", u"乙肝e抗体", u"乙肝核心抗体", u"体检日期"], axis=1)
    corr_relation = data.corr()
    corr_relation.to_csv("d_correlation.csv")
    # data = pd.read_csv("d_correlation.csv")
    # sns.barplot(x='Unnamed: 0', y=u"血糖", data=data)
    # plt.show()


def select_data():
    data = pd.read_csv("d_correlation.csv")
    data[u"血糖"] = abs(data[u"血糖"])
    data = data.sort_values(by=u"血糖")
    select_columns = ["id"]
    for i in data[u"血糖"].index:
        print(data["Unnamed: 0"][i], '\t', data[u"血糖"][i])
        if data[u"血糖"][i] > 0.1:
            select_columns.append(data["Unnamed: 0"][i])
    new_data = pd.read_csv("d_train.csv")
    select_data = new_data[select_columns]
    select_data.to_csv("d_train_select.csv", index=None)


if __name__ == '__main__':
    get_correlation()
    select_data()
