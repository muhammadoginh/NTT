import csv

# Sample data generation using two for loops
num_columns = 3
num_rows = 4

data = [['Column {}'.format(i) for i in range(1, num_columns + 1)]]

for i in range(num_rows):
    row_data = []
    for j in range(1, num_columns + 1):
        row_data.append(i * j)
    data.append(row_data)

# Specify the file name
file_name = 'data_generated.csv'

# Write data to CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Generated data saved successfully to", file_name)
