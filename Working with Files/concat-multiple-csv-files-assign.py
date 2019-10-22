import os
from glob import glob
import pandas as pd

path = r'.'
files = sorted(glob(os.path.join(path, "*.txt")))

df = pd.concat((pd.read_csv(file).assign(filename=os.path.basename(file)) for file in files), ignore_index=True)

print(df.head())