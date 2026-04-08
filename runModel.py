from ollama import generate
from ollama import chat
import time

llmModels = ['gemma4:e2b', 'deepseek-r1:1.5b', 'gemma4:e2b']

#Helpful resource I followed for my approach: https://medium.com/@jonigl/using-ollama-with-python-a-simple-guide-0752369e1e55
#Time resource used: https://docs.python.org/3/library/time.html
startTime = time.time()
response = chat(model='gemma4:e2b', messages=[{'role': 'user', 'content': 'Hello'}],)
stopTime = time.time()

print(response.message.content)