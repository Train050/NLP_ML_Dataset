from ollama import generate
import csv

#https://mimonirbd.medium.com/how-to-solve-python-csv-error-field-larger-than-field-limit-131072-error-320fa3c44a20
csv.field_size_limit(100000000)

llmModel = "deepseek-r1:8b"
csvFileName = ["./OnlyScoreColumn/gemma4OnlyScores.csv", "./OnlyScoreColumn/qwen2OnlyScores.csv", "./OnlyScoreColumn/llama3OnlyScores.csv"]
scoreFileName = ["./llmScores/gemma4Scores.csv", "./llmScores/qwen2Scores.csv", "./llmScores/llama3Scores.csv", "./llmScores/allScores.csv"]
#Used this source to format my prompt: https://medium.com/@the_manoj_desai/output-formatting-strategies-getting-exactly-what-you-want-how-you-want-it-8cebb61bad2d
llmPrompt = """There is a number located at the end of this string. Find the number and return only the number. Do not ask questions or explain what you are doing.
The number should be at most 100. Return only the number with no additional explanation."""

def findNumber(llmModel, iteration, scoreString):
    response = generate(model=llmModel, prompt=(llmPrompt + "\n" + scoreString),)
    output = {"llmModel" : llmModel, "iteration" : iteration, "score" : response.response}

    if(llmModel == "gemma4:e2b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(csvFileName[0], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

    elif(llmModel == "qwen2.5:3b"):
        with open(csvFileName[1], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

    elif(llmModel=="llama3.2:3b"):
        with open(csvFileName[2], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if timesCalled == 0:
                writer.writeheader()
            writer.writerow(output)

with open(scoreFileName[0], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = row["iteration"]
            scoreString = row["score"]
            findNumber(llmModel, iteration, scoreString)
            timesCalled += 1
            print(llmModel + " " + str(timesCalled))

with open(scoreFileName[1], newline="", encoding="utf-8") as qwenFile:
    llmCode = csv.DictReader(qwenFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = row["iteration"]
            scoreString = row["score"]
            findNumber(llmModel, iteration, scoreString)
            timesCalled += 1
            print(llmModel + " " + str(timesCalled))

with open(scoreFileName[2], newline="", encoding="utf-8") as llamaFile:
    llmCode = csv.DictReader(llamaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = row["iteration"]
            scoreString = row["score"]
            findNumber(llmModel, iteration, scoreString)
            timesCalled += 1
            print(llmModel + " " + str(timesCalled))
