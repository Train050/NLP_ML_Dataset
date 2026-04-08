from ollama import generate
from ollama import chat
import time
import pandas as pd
import csv

llmModels = ["gemma4:e2b", "deepseek-r1:1.5b", "llama3.2:3b"]
llmPhrase = "You are an senior level programmer. You will be provided a segment of code that has bugs within them. Do not provide context for the fix, only fix the code segment and respond with the fixed version of the code."

#Helpful resource I followed for my approach: https://medium.com/@jonigl/using-ollama-with-python-a-simple-guide-0752369e1e55
#Time resource used: https://docs.python.org/3/library/time.html

def runGemma(bugCode, fixedCode, prompt):
    startTime = time.time()
    response = chat(model="gemma4:e2b", messages=[{"role": "user", "content": prompt + "\n" + bugCode}],)
    stopTime = time.time()
    return response

def runDeepseek(bugCode, fixedCode, prompt):
    startTime = time.time()
    response = chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt + bugCode}],)
    stopTime = time.time()

def runLlama(bugCode, fixedCode, prompt):
    startTime = time.time()
    response = chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt + bugCode}],)
    stopTime = time.time()

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

#https://docs.python.org/3/library/csv.html
with open("./MSR_data_cleaned./MSR_data_cleaned.csv", newline="", encoding="utf-8") as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=",")

    for row in codeSnippets:
        if row["vul"] == "1":
            buggyCode = row["func_before"]
            fixedCode = row["func_after"]
            print("Initial prompt")
            print(llmPhrase)
            print("Bug Code snippet")
            print(buggyCode)
            print("LLM Response")
            print(runGemma(buggyCode, fixedCode, llmPhrase))
            break
        else:
            continue

    #print(response.message.content)