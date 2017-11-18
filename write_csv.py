import pandas as pd

df = pd.DataFrame(m).T

df.columns = ['m1', 'm2', 'm3']
df.index = ['seq1', 'seq2']
df.to_csv("output.csv", )
