# Reading from TEXT FILES

with open('welcome.txt') as text_file:
  text_data = text_file.read()                      # read() method Reads the content of the file     
  print(text_data)



with open('how_many_lines.txt') as lines_doc:
  lines = lines_doc.readlines()                     # readLines() method fetches all the lines of the file in a list through which we can iterate
  print(lines)
  for line in lines:
    print(line)

with open('millay_sonnet.txt') as sonnet_doc:       #readline() method reads a single line from the file
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)


# writing and appending to TEXT FILES
with open('generated_file.txt', 'w') as gen_file:   
  gen_file.write("What an incredible file!")

with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")









# Reading from CSV FILES
import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row)

#writing to CSV FILES
big_list = [{'name': 'James Willo', 'userid': 3242, 'is_admin': False},
            {'name': 'Robert Henry', 'userid': 2525942, 'is_admin': False}, 
            {'name': 'Henry Gale', 'userid': 15890235, 'is_admin': False}, 
            {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)










# Reading from JSON FILE
import json

with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)

print(purchase_data['user'])

#writing to JSON FILE

origin_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

import json

with open('output.json', 'w') as target_json_file:
  json.dump(origin_json, target_json_file)