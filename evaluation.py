# coding:utf-8
# @Time : 2017/12/27 19:17
# @Author : yuy


import numpy as np


class Evaluation(object):
    """模型评测函数

    """
    @staticmethod
    def get_errors(y_predict, y_true):
        y_predict = np.array(y_predict)
        y_true = np.array(y_true)
        result = sum((y_predict - y_true) * (y_predict - y_true)) * 1.0/ len(y_predict)
        return result


if __name__ == "__main__":
    y_true = [1, 1, 0, 1]
    y_predict = [0, 0, 0, 0]
    print Evaluation.get_errors(y_true, y_predict)