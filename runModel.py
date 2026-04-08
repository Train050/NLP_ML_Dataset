from ollama import generate
from ollama import chat
import time
import pandas as pd
import csv

llmModels = ['gemma4:e2b', 'deepseek-r1:1.5b', 'llama3.2:3b']
llmPhrase = 'You are an senior level programmer. '

#Helpful resource I followed for my approach: https://medium.com/@jonigl/using-ollama-with-python-a-simple-guide-0752369e1e55
#Time resource used: https://docs.python.org/3/library/time.html

#https://docs.python.org/3/library/csv.html
with open('./MSR_data_cleaned./MSR_data_cleaned.csv', newline='') as csvfile:
    codeSnippets = csv.DictReader(csvfile, delimiter=',')
    for row in codeSnippets:
        print(row['func_before'])
        print(row['func_after'])
        
    startTime = time.time()
    #response = chat(model='gemma4:e2b', messages=[{'role': 'user', 'content': 'Hello'}],)
    stopTime = time.time()
    #print(response.message.content)
    