import csv

csvFileName = ["./OnlyScoreColumn/gemma4OnlyScores.csv", "./OnlyScoreColumn/qwen2OnlyScores.csv", "./OnlyScoreColumn/llama3OnlyScores.csv"]
adjustedScoreNames = ["./finalFixedScores/gemma4FinalScores.csv", "./finalFixedScores/qwen2FinalScores.csv", "./finalFixedScores/llama3FinalScores.csv"]

def writeToFile(llmName, iteration, newScore):
    output = {"llmModel" : llmName, "iteration" : iteration, "finalScore" : newScore}
    if(llmModel == "gemma4:e2b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(adjustedScoreNames[0], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if iteration == 0:
                writer.writeheader()
            writer.writerow(output)
    elif(llmModel == "qwen2.5:3b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(adjustedScoreNames[1], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if iteration == 0:
                writer.writeheader()
            writer.writerow(output)
    elif(llmModel=="llama3.2:3b"):
        #Writing to file that's cleared each time: https://docs.python.org/3/library/functions.html#open
        with open(adjustedScoreNames[2], "a+", newline="", encoding="utf-8") as outFile:
            writer = csv.DictWriter(outFile, delimiter=",", fieldnames=output.keys())
            if iteration == 0:
                writer.writeheader()
            writer.writerow(output)

with open(csvFileName[0], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = int(row["iteration"])
            scoreString = row["score"]
            correctedScore = 0
            if(scoreString.isdigit()):
                if(int(scoreString) >= 100):
                    correctedScore = 100
                else:
                    correctedScore = int(scoreString)
            else:
                correctedScore = 0
            timesCalled += 1
            writeToFile(llmModel, iteration, correctedScore)
with open(csvFileName[1], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = int(row["iteration"])
            scoreString = row["score"]
            correctedScore = 0
            if(scoreString.isdigit()):
                if(int(scoreString) >= 100):
                    correctedScore = 100
                else:
                    correctedScore = int(scoreString)
            else:
                correctedScore = 0
            timesCalled += 1
            writeToFile(llmModel, iteration, correctedScore)

with open(csvFileName[2], newline="", encoding="utf-8") as gemmaFile:
    llmCode = csv.DictReader(gemmaFile, delimiter=",")
    timesCalled = 0
    for row in llmCode:
        if(int(row["iteration"]) >= timesCalled):
            llmModel = row["llmModel"]
            iteration = int(row["iteration"])
            scoreString = row["score"]
            correctedScore = 0
            if(scoreString.isdigit()):
                if(int(scoreString) >= 100):
                    correctedScore = 100
                else:
                    correctedScore = int(scoreString)
            else:
                correctedScore = 0
            timesCalled += 1
            writeToFile(llmModel, iteration, correctedScore)
