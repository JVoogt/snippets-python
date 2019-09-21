'''
    insert pandas dataframe into SQL Server
'''
import sqlalchemy as sa
import pyodbc
import numpy as np
import pandas as pd

dates = pd.date_range('20170101', periods=100, freq="W" )
data = pd.DataFrame(np.random.randn(100, 5), index=dates, columns=list('ABCDE'))

engine = sa.create_engine("mssql+pyodbc://SOMESERVER/MYDATABASE?driver=SQL+Server+Native+Client+11.0")
data.to_sql("TableName", con=engine)