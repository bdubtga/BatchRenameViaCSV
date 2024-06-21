import os
import pandas as pd

# Path to the folder containing the .weps files
folder_path = 'input'

# Path to the CSV file
csv_file_path = 'cardlist.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    current_name = str(row['mrk']) + '.webp'    
    new_name = row['nameeng'] + '.webp'  # Assuming column B contains the new base name without extension
    current_path = os.path.join(folder_path, current_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Check if the current file exists
    if os.path.exists(current_path):
        # Rename the file
        os.rename(current_path, new_path)
        print(f'Renamed "{current_name}" to "{new_name}"')
    else:
        print(f'File "{current_name}" does not exist.')