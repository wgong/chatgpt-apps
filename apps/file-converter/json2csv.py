import csv
import json
import os

# Open the JSON file and read the contents
input_filename = 'data/books.json'
with open(input_filename, 'r') as json_file:
  data = json.load(json_file)

header = data[0].keys()
print(f"header: {header}")

file_path, file_ext = os.path.splitext(input_filename)
output_filename = f"{file_path}-v1.csv"
# Open a new file to write the CSV data
with open(output_filename, 'w') as csv_file:
  # Create a CSV writer object
  writer = csv.DictWriter(csv_file, fieldnames=header)
  
  # Write the column names
  writer.writeheader()
  
  # Loop through the data and write each row
  for row in data:
    writer.writerow(row)
