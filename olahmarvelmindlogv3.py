import pandas as pd

# Load the CSV file
df = pd.read_csv('mm_log.csv')

df = df[df.iloc[:, 5] != 'na']
df = df[df.iloc[:, 5] != '5.264']
df = df[df.iloc[:, 5] != '2.025']
df = df[df.iloc[:, 5] != '-1.276']
df = df[df.iloc[:, 5] != '1.462']
# Function to edit the column value
def modify_column_value(value):
    # Remove the part before the first double underscore
    value = value.split('__', 1)[1]
    # Remove all remaining underscores
    value = value.replace('_', '.')
    return value

# Apply the function to the specific column
df['T2024_08_29__155130_272'] = df['T2024_08_29__155130_272'].apply(modify_column_value)


# Save the modified DataFrame back to a CSV
df.to_csv('modified_file5.csv', index=False)