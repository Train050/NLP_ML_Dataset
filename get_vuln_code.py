import csv

#Suggestion to avoid errors from printing out csv file: https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
import sys
sys.stdout.reconfigure(encoding="utf-8")

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)
vulnerableSegments = []

#https://docs.python.org/3/library/csv.html
with open("./MSR_data_cleaned./MSR_data_cleaned.csv", newline="", encoding="utf-8") as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=",")
    count = 0
    for row in codeSnippets:
        if row["vul"] == "1":
            vulnerableSegments.append(row)
            #print(row)
            count += 1
            if count == 2:
                break

#Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
with open("only_vulnerability.csv", "w", newline="", encoding="utf-8") as outFile:
    writer = csv.DictWriter(outFile, delimiter=",")
    
    #Getting the key/value so I can actually store the info I need: https://www.w3schools.com/python/python_dictionaries_loop.asp
    #Also this to keep the label before each data point in the csv: https://stackoverflow.com/questions/75854002/writing-a-dictionary-to-a-csv-file-one-line-for-each-key-value-pair-one-cell
    for rows in vulnerableSegments:
        for key, value in rows.items():
            writer.write([key, value])


""" with open("only_vulnerability.csv", newline="", encoding="utf-8") as test:
    codeSnippets = csv.DictReader(test, delimiter=",")
    for row in codeSnippets:
        print(row) """