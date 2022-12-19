import csv
import json
from time import process_time


csvFilePath = '/gitlabrepo/TESTIDATA/2021-05.csv'
jsonFilePath = '/gitlabrepo/TESTIDATA/converted.json'

def convert(csvFilePath, jsonFilePath):
    data = []
    count = 0
    with open(csvFilePath, 'r', encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        fields = next(csvReader)

        for rows in csvReader:
            
            dataRow = {fields[0]: rows[0], fields[1]: rows[1], fields[2]: rows[2],fields[3]: rows[3],
            fields[4]: rows[4], fields[5]: rows[5], fields[6]: rows[6],fields[7]: rows[7]}

            with open(jsonFilePath, 'a', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(dataRow, indent=4))

            print(count)
            count += 1
            
            # if count >= 1000:
            #     print(process_time())
            #     break

convert(csvFilePath, jsonFilePath)
print(process_time())