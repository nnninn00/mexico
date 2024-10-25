import pandas as pd

#csv data to data dictionary
dataset_path = 'dataset.csv'
data_dict_path = 'data_dictionary.xlsx'

# Load the dataset
df = pd.read_csv(dataset_path)

# display first few rows of the dataset
df.head()

# age column check
data_dict = pd.read_excel(data_dict_path)

# data dictionary display
data_dict.head()

# desc age var
age_info = data_dict[data_dict['variable'].str.contains('AGE', case=False, na=False)]

##result
age_info

# names to age
df.columns[df.columns.str.contains('age', case=False, na=False)]

