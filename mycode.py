import pandas as pd
import os


data = {
  'Name': ['Alice','khaja','Mubashir','Arsalan'],
  'Age' : [22,21,43,55],
  'city' : ['new york', 'Nirmal', 'Adilabad','Hyderabad']
}

df = pd.DataFrame(data)


# adding new row to check dvc is tracking or not

new_row = {'Name':'nashu','Age':20,'city':'city'}
df.loc[len(df.index)] = new_row

# ensuring data directory shouldn't available at root level

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Define file path

file_path = os.path.join(data_dir,'simple_data.csv')

# save data into csv file

df.to_csv(file_path,index=False)
print(f"csv file saved in {file_path}")