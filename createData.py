import csv

special_chars = ['@', '&', '#', '-', '!']

def dataRead(path):
    """
     Reads CSV files
    """
    # Import the data
    out_data = []
    with open(path, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile)
        for  row in input_file:
           
            #print(row)

            out_data.append(row)
            
    return out_data

def dataWrite(path, column_keys, out_data):
    """
        Writes CSV Files
    """
    with open(path, "w", encoding="utf-8") as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=column_keys)
        w.writeheader()
        for row in (out_data):
            w.writerow(row)

    return None

def readURL(out_data):
    """
        Extracts URLs
    """
    url = []
    # Read the data
    for row in out_data:
        # Read every row
        for key in row:
            # If the key has source URL
            if('Url' in key):
                curr_url = row[key]
                url.append(curr_url.split('/')[-1])
    return url

        # If the key has Log
        # if('Log' in key):
            # stat = row[key]

            # if(stat == "Failed"):
                # status.append(0)
            # elif(stat == 'Success'):
                # status.append(1)
            # else:
                # print("Unknown Log type")

def findSpecialChars(url, special_chars):
    is_special_char = []

    # Check for special characters
    for u in url:
        flag = "No"
        for special_char in special_chars:
            if(special_char in u):
                flag = "Yes"
        is_special_char.append(flag)
        #print(u,flag)

    return is_special_char

def addNewRow(out_data, is_special_char):
    for idx,row in enumerate(out_data):
            row['Special Char'] = is_special_char[idx]

    return out_data

def main(readPath, writePath):

    print("Reading CSV File\n")

    # read CSV file
    out_data = dataRead(readPath)

    # Get the URLS
    url = readURL(out_data)

    # Find Special Chars
    is_special_char = findSpecialChars(url, special_chars)

    # Add new column
    out_data = addNewRow(out_data, is_special_char)

    # Get the headers
    column_keys = out_data[0].keys()

    print("Writing CSV Files\n")

    # Write new CSV
    dataWrite(writePath, column_keys, out_data)

    print("Success!")

main("Siteinfo2010.csv", "test_11.csv")

