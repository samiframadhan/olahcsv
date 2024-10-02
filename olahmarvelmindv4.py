import pandas as pd
import math

# Load the CSV file
df = pd.read_csv('log26Sept2024.csv')

df = df[df.iloc[:, 5] != 'na']
df = df[df.iloc[:, 3] != '18']
df = df[df.iloc[:, 2] != '1']
# df = df[df.iloc[:, 5] != '5.264']
# df = df[df.iloc[:, 5] != '2.025']
# df = df[df.iloc[:, 5] != '-1.276']
# df = df[df.iloc[:, 5] != '1.462']
# Function to edit the column value
prev_x = 0.0
prev_y = 0.0

def point_distance(x1 :float, y1 :float, x2 :float, y2 :float):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    result = (x2-x1)**2 + (y2-y1)**2
    result = math.sqrt(result)
    return result
    
def distance_point_to_line(A : float, B : float, C : float, x1 : float, y1 : float):
    """
    Calculate the perpendicular distance from a point to a line.

    Parameters:
    A, B, C: coefficients of the line equation Ax + By + C = 0
    x1, y1: coordinates of the point (x1, y1)

    Returns:
    float: The perpendicular distance from the point to the line
    """
    A = float(A)
    B = float(B)
    C = float(C)
    x1 = float(x1)
    y1 = float(y1)
    # Calculate the numerator of the distance formula
    numerator = abs(A * x1 + B * y1 + C)
    
    # Calculate the denominator of the distance formula
    denominator = math.sqrt(A**2 + B**2)
    
    # Calculate and return the distance
    distance = numerator / denominator
    return distance

def modify_column_value(value):
    # Remove the part before the first double underscore
    value = value.split('__', 1)[1]
    # Remove all remaining underscores
    value = value.replace('_', '.')
    return value

def add_column_dist_to_line_1(row):
    # print(row['x_point'])
    # print(type(row['x_point']))
    res = distance_point_to_line(A=-0.6167, B=1, C=-1.3256478, x1=row['x_point'], y1=row['y_point'])
    return res

def add_column_dist_to_line_2(row):
    res = distance_point_to_line(A=-0.61670, B=1, C=0.0218208, x1=row['x_point'], y1=row['y_point'])
    return res

def add_column_dist_to_line_3(row):
    res = distance_point_to_line(A=-(1/0.61670), B=1, C=0.648837198, x1=row['x_point'], y1=row['y_point'])
    return res

def add_column_dist_to_line_4(row):
    res = distance_point_to_line(A=-(1/0.61670), B=1, C=0.760304524, x1=row['x_point'], y1=row['y_point'])
    return res

def add_column_dist_to_beacon_1(row):
    res = point_distance(x1=1.462, y1=3.996, x2=row['x_point'], y2=row['y_point'])
    return res

def add_column_dist_to_beacon_2(row):
    res = point_distance(x1=2.025, y1=-1.618, x2=row['x_point'], y2=row['y_point'])
    return res

def add_column_dist_to_beacon_3(row):
    res = point_distance(x1=-1.276, y1=2.282, x2=row['x_point'], y2=row['y_point'])
    return res

def add_column_dist_to_beacon_4(row):
    res = point_distance(x1=5.264, y1=2.282, x2=row['x_point'], y2=row['y_point'])
    return res

def add_zerr_1(row):
    res = float(row['z_point']) - 0.6
    return res

def add_zerr_2(row):
    res = float(row['z_point']) - 0.3
    return res

def add_drastic_changes(row):
    global prev_y, prev_x
    curr_x = row['x_point']
    curr_x = float(curr_x)
    curr_y = row['y_point']
    curr_y = float(curr_y)
    res = point_distance(x1=curr_x, y1=curr_y, x2=prev_x, y2=prev_y)
    prev_x = curr_x
    prev_y = curr_y
    return res

# Apply the function to the specific column
df['timestamp'] = df['timestamp'].apply(modify_column_value)

df['distance_to_line_1'] = df.apply(add_column_dist_to_line_1, axis=1)
df['distance_to_line_2'] = df.apply(add_column_dist_to_line_2, axis=1)
df['distance_to_line_3'] = df.apply(add_column_dist_to_line_3, axis=1)
df['distance_to_line_4'] = df.apply(add_column_dist_to_line_4, axis=1)
df['distance_to_beacon_1'] = df.apply(add_column_dist_to_beacon_1, axis=1)
df['distance_to_beacon_2'] = df.apply(add_column_dist_to_beacon_2, axis=1)
df['distance_to_beacon_3'] = df.apply(add_column_dist_to_beacon_3, axis=1)
df['distance_to_beacon_4'] = df.apply(add_column_dist_to_beacon_4, axis=1)
df['z_err1'] = df.apply(add_zerr_1, axis=1)
df['z_err2'] = df.apply(add_zerr_2, axis=1)
df['drastic_changes'] = df.apply(add_drastic_changes, axis=1)

# Save the modified DataFrame back to a CSV
df.to_csv('modified_file9.csv', index=False)