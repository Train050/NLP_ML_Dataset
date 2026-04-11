from ollama import generate
import time
import pandas as pd
import csv

#Getting rid of deepseek-r1:1.5b since it has too few parameters, and replacing it with qwen3.5:2b
llmModels = ["gemma4:e2b", "qwen2.5:3b", "llama3.2:3b"]
csvFileName = ["./llmResponses/gemma4.csv", "./llmResponses/qwen2.csv", "./llmResponses/llama3.csv"]
llmPhrase = """You are an senior level programmer. You will be provided a segment of code that has bugs in them. 
Do not provide context for your fix or any dialogue describing how you fixed the program. Only fix the code segment and respond with the fixed version of the code.
Only respond with the entire corrected code segment that includes your code changes and any unaltered code."""

#Helpful resource I followed for my approach: https://medium.com/@jonigl/using-ollama-with-python-a-simple-guide-0752369e1e55
#Time resource used: https://docs.python.org/3/library/time.html

#https://www.cohorte.co/blog/using-ollama-with-python-step-by-step-guide
#https://www.geeksforgeeks.org/python/g-fact-41-multiple-return-values-in-python/
def runModel(llmNum, bugCode, fixedCode, prompt, trial, vulnSeverity, programLang, vulnType):
    startTime = time.time()
    response = generate(model=llmModels[llmNum], prompt=(prompt + "\n" + bugCode),)
    stopTime = time.time()
    output = {"llmModel" : llmModels[llmNum], "execTime": (stopTime - startTime), "programLang" : programLang, "vulnType" : vulnType, "vulnSeverity" : vulnSeverity, "iteration" : trial, "llmFixCode": response.response, "csvFixCode": fixedCode}

    #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
    with open(csvFileName[llmNum], "a+", newline="", encoding="utf-8") as outFile:
        writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
        if currentTrial == 0:
                writer.writeheader()
        writer.writerow(output)

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

#https://docs.python.org/3/library/csv.html
with open("only_vulnerability.csv", newline="", encoding="utf-8") as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=",")
    currentTrial = 0
    for row in codeSnippets:
        buggyCode = row["func_before"]
        fixedCode = row["func_after"]
        vulnSeverity = row["Score"]
        programLang = row["lang"]
        vulnType = row["Vulnerability Classification"]

        #Gemma
        runModel(0, buggyCode, fixedCode, llmPhrase, currentTrial, vulnSeverity, programLang, vulnType)
        #Qwen2
        runModel(1, buggyCode, fixedCode, llmPhrase, currentTrial, vulnSeverity, programLang, vulnType)
        #Llama3.2
        runModel(2, buggyCode, fixedCode, llmPhrase, currentTrial, vulnSeverity, programLang, vulnType)
        currentTrial += 1
        print(currentTrial)