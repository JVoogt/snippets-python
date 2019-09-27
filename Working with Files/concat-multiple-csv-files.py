import os
import glob
import pandas as pd

path = r'.'
all_files = glob.glob(os.path.join(path, "*.txt"))
names = [os.path.basename(x) for x in glob.glob(path+'\*.txt')]
df = pd.DataFrame()

for file_ in all_files:
    file_df = pd.read_csv(file_, index_col=0, header=0)
    file_df['file_name'] = file_
    df = df.append(file_df)
print(df)