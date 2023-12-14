import numpy as np
import pandas as pd

df = pd.read_json('cars_submissions.ndjson', lines=True)
#df2 = pd.read_json('cars_comments.ndjson', lines=True)

def delcoms(df):
    for index, row in df.iterrows():
        comment = row['selftext']
        if comment.lower() not in {'[removed]', '[deleted]', ''}:
            yield index, row

# Filter the DataFrame using the generator
filtered_indices = []
filtered_rows = []

for index, row in delcoms(df):
    filtered_indices.append(index)
    filtered_rows.append(row)

# Create a new DataFrame with filtered rows
filtered_dataframe = pd.DataFrame(filtered_rows, index=filtered_indices)

print(filtered_dataframe)