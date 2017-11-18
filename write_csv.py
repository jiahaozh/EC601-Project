import pandas as pd

df = pd.DataFrame([[311.11324435763891, 459.35657654562112], [326.9993929036458, 488.02189410927855], [323.19149534625774, 455.74575749903551]]).T

df.columns = ['m1', 'm2', 'm3']
df.index = ['seq1', 'seq2']
df.to_csv("output.csv", )
