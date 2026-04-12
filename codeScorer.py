from xml.etree.ElementTree import tostring

from ollama import generate
import csv

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

llmModel = "deepseek-r1:8b"
csvFileName = ["./llmResponses/gemma4.csv", "./llmResponses/qwen2.csv", "./llmResponses/llama3.csv"]
scoreFileName = ["./llmScores/gemma4Scores.csv", "./llmScores/qwen2Scores.csv", "./llmScores/llama3Scores.csv", "./llmScores/allScores.csv"]
#Used this source to format my prompt: https://medium.com/@the_manoj_desai/output-formatting-strategies-getting-exactly-what-you-want-how-you-want-it-8cebb61bad2d
llmPrompt = """You are an expert programmer. Your goal is to perfectly score a code snippet that attempts to fix a bug, given the code snippet that was actually used, and return your calculated score. 

Think through this step by step:
1. First, recieve two code snippet inputs following this prompt.
2. Then, grade the first code snippet out of 30 points  based on if it successfully changed only the bug-prone lines of code which is observed in the second code snippet.
3. Next, grade the first code snippet out of 70 points, depending on how accurately the first code snippet functionally matches the second code snippet. Do not deduct points out of the 70 if the code snippets are functionally identical but programmed differently.
4. After, add the scores for each section to get a final score, which is at most 100 points.
5. Finally, output only the summed total score.
Your output should only be your summed total score.

Return only the scored output with no additional explanation."""

def evaluateModel(llmModel, execTime, programLang, vulnType, vulnSeverity, iteration, llmFixCode, csvFixCode, timesCalled):
    response = generate(model=llmModel, prompt=(llmPrompt + "\n" + llmFixCode + "\n" + csvFixCode),)
    output = {"llmModel" : llmModel, "execTime": execTime, "programLang" : programLang, "vulnType" : vulnType, "vulnSeverity" : vulnSeverity, "iteration" : iteration, "llmFixCode": llmFixCode, "csvFixCode": csvFixCode, "score" : response.response}

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
        llmModel = row["llmModel"]
        execTime = row["execTime"]
        programLang = row["programLang"]
        vulnType = row["vulnType"]
        vulnSeverity = row["vulnSeverity"]
        iteration = row["iteration"]
        llmFixCode = row["llmFixCode"]
        csvFixCode = row["csvFixCode"]
        evaluateModel(llmModel, execTime, programLang, vulnType, vulnSeverity, iteration, llmFixCode, csvFixCode, timesCalled)
        timesCalled += 1
        print(llmModel + " " + str(timesCalled))

with open(csvFileName[1], newline="", encoding="utf-8") as qwenFile:
    llmCode = csv.DictReader(qwenFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        llmModel = row["llmModel"]
        execTime = row["execTime"]
        programLang = row["programLang"]
        vulnType = row["vulnType"]
        vulnSeverity = row["vulnSeverity"]
        iteration = row["iteration"]
        llmFixCode = row["llmFixCode"]
        csvFixCode = row["csvFixCode"]
        evaluateModel(llmModel, execTime, programLang, vulnType, vulnSeverity, iteration, llmFixCode, csvFixCode, timesCalled)
        timesCalled += 1
        print(llmModel + " " + str(timesCalled))

with open(csvFileName[2], newline="", encoding="utf-8") as llamaFile:
    llmCode = csv.DictReader(llamaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        llmModel = row["llmModel"]
        execTime = row["execTime"]
        programLang = row["programLang"]
        vulnType = row["vulnType"]
        vulnSeverity = row["vulnSeverity"]
        iteration = row["iteration"]
        llmFixCode = row["llmFixCode"]
        csvFixCode = row["csvFixCode"]
        evaluateModel(llmModel, execTime, programLang, vulnType, vulnSeverity, iteration, llmFixCode, csvFixCode, timesCalled)
        timesCalled += 1
        print(llmModel + " " + str(timesCalled))
