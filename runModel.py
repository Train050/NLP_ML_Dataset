from ollama import generate
import time
import pandas as pd
import csv

llmModels = ["gemma4:e2b", "deepseek-r1:1.5b", "llama3.2:3b"]
llmPhrase = "You are an senior level programmer. You will be provided a segment of code that has bugs within them. Do not provide context for the fix, only fix the code segment and respond with the fixed version of the code."

#Helpful resource I followed for my approach: https://medium.com/@jonigl/using-ollama-with-python-a-simple-guide-0752369e1e55
#Time resource used: https://docs.python.org/3/library/time.html

#https://www.cohorte.co/blog/using-ollama-with-python-step-by-step-guide
def runModel(lllModel, bugCode, fixedCode, prompt):
    startTime = time.time()
    response = generate(model=lllModel, prompt=(prompt + "\n" + bugCode),)
    stopTime = time.time()
    return lllModel + "\n" + response["response"]

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

#https://docs.python.org/3/library/csv.html
with open("only_vulnerability.csv", newline="", encoding="utf-8") as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=",")
    for row in codeSnippets:
        buggyCode = row["func_before"]
        fixedCode = row["func_after"]

        print(runModel(llmModels[0], buggyCode, fixedCode, llmPhrase))
        print(runModel(llmModels[1], buggyCode, fixedCode, llmPhrase))
        print(runModel(llmModels[2], buggyCode, fixedCode, llmPhrase))
        break
    #print(response.message.content)