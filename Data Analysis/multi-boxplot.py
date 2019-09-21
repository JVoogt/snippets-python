'''
    conda install pandas-profiling
    pip install pandas-profiling
    https://github.com/pandas-profiling/pandas-profiling
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20170101', periods=100, freq="W" )
data = pd.DataFrame(np.random.randn(100, 5), index=dates, columns=list('ABCDE'))

plt.figure(1, figsize=(20, 5))
for i in range(1, 5):
    plt.subplot(1, 5, i)
    plt.boxplot(data[data.columns[i]])
    plt.title(data.columns[i])
plt.show()
data.iloc[:, :].describe()