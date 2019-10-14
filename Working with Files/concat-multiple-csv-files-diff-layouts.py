import os
import glob
import pandas as pd
import ast
from os import getenv

'''
    Function to Create list of lists from list
'''
def merge(list1, list2):     
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 

'''
    walk through OS to find all files in path
'''
path = r'.'
all_files = glob.glob(os.path.join(path, "*.txt"))
names = [os.path.basename(x) for x in glob.glob(path+'\*.txt')]
df = pd.DataFrame()
full = merge(all_files,names)

'''
    Read files into a Dataframe, then add the Dataframe to a list of DataFrames
'''
df_list = []
for path, name in full:
    file_df = pd.read_excel(path)
    file_df['file_name'] = name
    df_list.append(file_df)

'''
    Create a list of only the headers of the DataFrames
'''
headers = []
for i in df_list:
    headers.append(str(list(i.columns)))

'''
    Turn Headers List into Dict to remove duplicates
'''
header_set = dict((i, headers.count(i)) for i in headers)

'''
    Turn string representation of list into list
'''
d = list(header_set.keys())
mList = []

for i in d:
    mList.append(ast.literal_eval(i))

'''
    Use Namespace to create a Datframe for each file layout
'''
namespace = globals()

for i in range(len(mList)):
    namespace['df%s'%i] = pd.DataFrame(columns=mList[i])
    for data in df_list:
        if set(mList[i]).issubset(data.columns):
            df = pd.DataFrame(data.values, columns=mList[i])
            namespace['df%s'%i] = namespace['df%s'%i].append(df)