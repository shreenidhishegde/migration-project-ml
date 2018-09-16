import csv

# Import the data
input_file = csv.DictReader(open("test.csv"))

data = []
status = []

# Read the data
for row in input_file:
    # Read every row
    for key in row:
        # If the key has source URL
        if('Source URL' in key):
            data.append(row[key])
        # If the key has Log
        if('Log' in key):
            stat = row[key]

            if(stat == "Failed"):
                status.append(0)
            elif(stat == 'Success'):
                status.append(1)
            else:
                print("Unknown Log type")

url = []
# Process the data
for d in data:
    url.append(d.split('/')[-1])

special_chars = ['@', '&', '#']
# Check for special characters
for u in url:
    for special_char in special_chars:
        if(special_char in u):
            print("Special Characters found")
            print(u)

