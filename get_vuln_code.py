import csv

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

#https://docs.python.org/3/library/csv.html
with open("./MSR_data_cleaned./MSR_data_cleaned.csv", newline="", encoding="utf-8") as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=",")

    for row in codeSnippets:
        if row["vul"] == "1":
            print(row)
            break
            #Appending the write with 'a': https://docs.python.org/3/library/functions.html#open
            with open("only_vulnerability.csv", "a", newline="", encoding="utf-8") as outFile:
                fieldnames = [""]
                writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                writer.writerow(row)
