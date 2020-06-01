# -*- coding: utf-8 -*-
#fix in ubuntu14
#forth edit, pycharm test git
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# y_true和y_scores分别是gt label和predict score
recall = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
precision = np.array([0.956, 0.892, 0.847, 0.816, 0.785, 0.732, 0.649, 0.559, 0.400, 0.197, 0])

recall2 = np.array([0, 0.19, 0.9, 0.39, 0.49, 0.59, 0.69, 0.799, 0.89, 0.99, 1])
precision2 = np.array([0.956, 0.892, 0.847, 0.816, 0.785, 0.732, 0.649, 0.559, 0.400, 0.197, 0])

plt.figure()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid(True)
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.plot(recall, precision, lw=0.7, label='本文方法')  # ,encoding='UTF-8')
plt.plot(recall2, precision2, lw=0.7, label='2')
plt.title('Precision-Recall')
plt.legend(loc="lower left")
plt.show()

