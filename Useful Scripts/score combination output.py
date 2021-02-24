import itertools 
import csv

#Define all Variables and their respective possiblities
score_values = {
    "all_numevertades_points" : [0,1,2,3],
    "crc_numevertades_points" : [0,1,2,3,4],
    "rcg_numevertades_points" : [0,1,2,3,5],
    "sec_numevertades_points" : [0,1,2,3,6,7,8,9]
}

#Create and empty list to combine the above lists from the Dict
all_lists = []

for key, value in score_values.items():
    all_lists.append(value)

#Usign itertools-> Prduct to find all possible permutations of the above lists
res = list(itertools.product(*all_lists)) 

cols = list(score_values.keys())
cols.append("score")

results = []

#Add the final score and output to a file for use in SQL
for permutation in res:
    score = sum(permutation)
    t = permutation + (score,)
    values = list(t)
    res = {cols[i]: values[i] for i in range(len(cols))}     
    results.append(res)

#Create CSV File
keys = results[0].keys()
with open('score_permutations.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)