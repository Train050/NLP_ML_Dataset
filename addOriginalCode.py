import csv

csv.field_size_limit(100000000)

originalCSVFile = "only_vulnerability.csv"
csvFileName = ["./llmResponses/gemma4.csv", "./llmResponses/qwen2.csv", "./llmResponses/llama3.csv"]
csvCorrectedFiles = ["./fixedLLMResponse/gemma4Fix.csv", "./fixedLLMResponse/qwen2Fix.csv", "./fixedLLMResponse/llama3Fix.csv"]

def fixOutput(currentRow):
    if(currentRow["llmModel"] == "gemma4:e2b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(csvCorrectedFiles[0], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=currentRow.keys())
            writer.writerow(currentRow)

    elif(currentRow["llmModel"] == "qwen2.5:3b"):
        with open(csvCorrectedFiles[1], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=currentRow.keys())
            writer.writerow(currentRow)

    elif(currentRow["llmModel"] == "llama3.2:3b"):
        with open(csvCorrectedFiles[2], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=currentRow.keys())
            writer.writerow(currentRow)

with open(csvFileName[0], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    next(llmCode)
    timesCalled = 0
    for row in llmCode:
        with open("only_vulnerability.csv", "r", newline="", encoding="utf-8") as originalFile:
            rowNames = list(row.keys())
            rowNames.append("csvOriginalCode")
            #print(rowNames)
            vcfReader = csv.DictReader(originalFile, delimiter=",", fieldnames=rowNames)
            if(timesCalled >= 2):
                break
            if(timesCalled == 0):
                #Converting the keys to a list: https://www.geeksforgeeks.org/python/python-get-dictionary-keys-as-a-list/
                with open(csvCorrectedFiles[0], "a+", newline="", encoding="utf-8") as outFile:
                    writer = csv.DictWriter(outFile, delimiter=",", fieldnames=rowNames)
                    writer.writerow(rowNames)
            else:
                correctOutput = row
                print(vcfReader)
                #correctOutput.update({"csvOriginalCode" : next(vcfReader)})
                #fixOutput(correctOutput)
            timesCalled += 1
            print(timesCalled)
