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
    for row in codeSnippets:
        if row["vul"] == "1":
            vulnerableSegments.append(row)

#Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
with open("only_vulnerability.csv", "w", newline="", encoding="utf-8") as outFile:
    #Getting the key/value so I can actually store the info I need: https://www.w3schools.com/python/python_dictionaries_loop.asp
    #Also this to keep the label before each data point in the csv: https://stackoverflow.com/questions/75854002/writing-a-dictionary-to-a-csv-file-one-line-for-each-key-value-pair-one-cell
    #Another useful source for getting writing to work and add headers to the csv: https://dev.to/thumbone/dumping-data-with-pythons-csv-dictwriter-1g0
    labels = vulnerableSegments[0].keys()
    writer = csv.DictWriter(outFile, delimiter=",", fieldnames=labels)
    writer.writeheader()
    for rows in vulnerableSegments:
        writer.writerow(rows)