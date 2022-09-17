import os
import requests
import time
import re

# test - 주석 해제
import environ

environ.environ()

MAX_CAPACITY = 800


# translate text with papago API
def translateWithPapagoAPI(text):
    # Header Info
    client_id = os.getenv('X_Naver_Client_Id')
    client_secret = os.getenv('X_Naver_Client_Secret')

    # Post Url
    url = "https://openapi.naver.com/v1/papago/n2mt"

    # Header
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    # Data
    data = {'source': 'en', 'target': 'ko', 'text': text}

    # Post
    response = requests.post(url, headers=headers, json=data)

    # return response data
    if response.status_code == 200:
        return response.json()['message']['result']['translatedText']
    else:
        return 'error'


def translate():
    # get last log
    logsFile = open('./logs', 'r+')
    logs = list(filter(lambda log: log.strip() != '', logsFile.readlines()))

    # check last log
    lastLog = logs[-1] if len(logs) > 0 else None
    lastLogFilePath = lastLog.split("|")[1].strip() if lastLog is not None else None
    lastLogFileLine = int(lastLog.split("|")[2].strip()) if lastLog is not None else 0

    # open README.md & get Lines containing paths
    README = open('./README.md', 'r')
    lines = list(filter(lambda line: line[:2] == '- ', README.readlines()))
    README.close()

    # for New log
    logFilePath = ""
    logLine = 0

    # Translate Capacity
    capacity = 0

    # Find last Position
    findLastLogFile = False if lastLog is not None else True
    findLastLogFileLine = False if lastLog is not None else True

    finished = False

    for line in lines:
        currentFilePath = line.split("(")[1].replace(")", "").rstrip()
        originFilePath = "./originHIG-markdown" + currentFilePath[1:]

        logFilePath = currentFilePath

        if currentFilePath == lastLogFilePath:
            findLastLogFile = True

        if findLastLogFile and os.path.isfile(currentFilePath):
            originFile = open(originFilePath, 'r')
            originData = originFile.readlines()
            currentPathFile = open(currentFilePath, 'a')

            if len(originData) == 1:
                break

            for i in range(len(originData)):
                if findLastLogFileLine:
                    if originData[i].strip() != '' and originData[i][0] != "!" and i != 0:
                        capacity += len(originData[i])

                        originText = originData[i].strip()
                        text = originText.replace('#', '').replace('*', '')

                        for repl in re.findall('\[(.*?)\]\((.*?)\)', text):
                            originText = originText.replace(repl[1], repl[1].replace(
                                "https://developer.apple.com/design/human-interface-guidelines", ".."))
                            text = text.replace("[" + repl[0] + "](" + repl[1] + ")", repl[0])

                        if len(text.split(' ')) > 3:
                            if capacity > MAX_CAPACITY:
                                finished = True
                                break
                            currentPathFile.write(originText + '\n')
                            translatedText = translateWithPapagoAPI(text)
                            currentPathFile.write(
                                (('> ' + translatedText + '\n>\n\n') if translatedText[0] != '-' else (
                                        '- > ' + translatedText[1:])) + '\n\n')
                        else:
                            currentPathFile.write(originText + '\n')

                    elif i == 0:
                        currentPathFile.write('\n')

                    else:
                        currentPathFile.write(originData[i] + '\n')

                logLine = i

                if i >= lastLogFileLine:
                    findLastLogFileLine = True

            # open Files to Write & write
            originFile.close()
            currentPathFile.close()

            if finished:
                break

    logsFile.write(time.strftime('%Y-%m-%d %H:%M:%S') + ' | ' + logFilePath + ' | ' + str(logLine) + '\n')
    logsFile.close()


translate()
