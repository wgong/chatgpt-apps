import csv
import json
import os

# Open the CSV file and read the contents
input_filename = 'data/books.csv'
with open(input_filename, 'r', encoding='utf-8') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  
  # Create an empty list to store the data
  data = []
  
  # Loop through the rows in the CSV file
  for row in csv_reader:
    # Add each row to the data list
    data.append(row)

file_path, file_ext = os.path.splitext(input_filename)
output_filename = f"{file_path}.json"
# Open a new file to write the JSON data
with open(output_filename, 'w', encoding='utf-8') as json_file:
  # Write the data to the file as JSON
  json.dump(data, json_file)
