import csv
import json

# Open the CSV file and read the contents
with open('input.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  
  # Create an empty list to store the data
  data = []
  
  # Loop through the rows in the CSV file
  for row in csv_reader:
    # Add each row to the data list
    data.append(row)

# Open a new file to write the JSON data
with open('output.json', 'w') as json_file:
  # Write the data to the file as JSON
  json.dump(data, json_file)
