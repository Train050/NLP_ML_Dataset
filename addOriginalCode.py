import csv

csv.field_size_limit(100000000)

llmModel = "deepseek-r1:8b"
csvFileName = ["./llmResponses/gemma4.csv", "./llmResponses/qwen2.csv", "./llmResponses/llama3.csv"]
csvCorrectedFiles = ["./fixedLLMResponse/gemma4Fix.csv", "./fixedLLMResponse/qwen2Fix.csv", "./fixedLLMResponse/llamaFix.csv"]
llmPrompt = """You are an senior level programmer. You will be provided two segments of code. The first code input is an attempt to fix the bugs within a code snippet.
 The second code input is the actual fix for the code snippet that was put into production. You are tasked with grading the first code input.
 Only return a score out of 100, where 70 potential points are for if the first code is functional and 30 potential points are for how identical the code snippets are.
  The format for your output should be EARNED POINTS / 100"""

def fixOutput(currentRow, originalCode, currentRowNumber):

    if(llmModel == "gemma4:e2b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(scoreFileName[0], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

    elif(llmModel == "qwen2.5:3b"):
        with open(scoreFileName[1], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

    elif(llmModel=="llama3.2:3b"):
        with open(scoreFileName[2], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

with open(csvFileName[0], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        fixOutput()
        timesCalled += 1

with open(csvFileName[1], newline="", encoding="utf-8") as qwenFile:
    llmCode = csv.DictReader(qwenFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        fixOutput()
        timesCalled += 1

with open(csvFileName[2], newline="", encoding="utf-8") as llamaFile:
    llmCode = csv.DictReader(llamaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        fixOutput()
        timesCalled += 1