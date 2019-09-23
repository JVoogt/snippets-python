'''
    inspect source from any lib
'''
import pandas as pd
import inspect

print(inspect.getsource(pd.read_csv))
