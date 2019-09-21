'''
    conda install pandas-profiling
    pip install pandas-profiling
    https://github.com/pandas-profiling/pandas-profiling
'''
import numpy as np
import pandas as pd
import pandas_profiling as pp

dates = pd.date_range('20170101', periods=100, freq="W" )
data = pd.DataFrame(np.random.randn(100, 5), index=dates, columns=list('ABCDE'))

profile = pp.ProfileReport(data, title='Pandas Profiling Report')
profile.to_file("output.html")