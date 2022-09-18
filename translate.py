import os
import requests
import time
import re

# test - 주석 해제
# import environ
#
# environ.environ()

MAX_CAPACITY = 8000


# translate text with papago API
def translateWithPapagoAPI(text):
    # Header Info
    client_id = os.getenv('X_NAVER_CLIENT_ID')
    client_secret = os.getenv('X_NAVER_CLIENT_SECRET')

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

    # read README Text
    for line in lines:
        # get Path
        currentFilePath = line.split("(")[1].replace(")", "").rstrip()
        originFilePath = "./originHIG-markdown" + currentFilePath[1:]

        # for Log
        logFilePath = currentFilePath

        # find last log file
        if currentFilePath == lastLogFilePath:
            findLastLogFile = True

        # if find last log file and file is exist
        if findLastLogFile and os.path.isfile(currentFilePath):

            # open origin File and current File
            originFile = open(originFilePath, 'r')
            originData = originFile.readlines()
            currentPathFile = open(currentFilePath, 'a')

            # empty file
            if len(originData) < 2:
                break

            # read Origin Text Data
            for i in range(len(originData)):
                # if find last log file line
                if findLastLogFileLine:
                    if originData[0] != '|' and originData[i].strip() != '' and originData[i][0] != '!' and i != 0:

                        # remove Sharp and Asterisk
                        originText = originData[i].strip()
                        text = originText.replace('#', '').replace('*', '')

                        # check link and replace text
                        for repl in re.findall('\[(.*?)\]\((.*?)\)', text):
                            originText = originText.replace(repl[1], repl[1].replace(
                                "https://developer.apple.com/design/human-interface-guidelines", ".."))
                            text = text.replace("[" + repl[0] + "](" + repl[1] + ")", repl[0])

                        # translate
                        if len(text.split(' ')) > 3:
                            if capacity + len(originData[i]) > MAX_CAPACITY:
                                finished = True
                                break

                            translatedText = translateWithPapagoAPI(text)

                            if translatedText == 'error':
                                finished = True
                                break

                            capacity += len(originData[i])
                            currentPathFile.write(originText + '\n')

                            currentPathFile.write(
                                (('> ' + translatedText + '\n>\n\n') if translatedText[0] != '-' else (
                                        '- > ' + translatedText[1:])) + '\n\n')

                        else:
                            currentPathFile.write(originText + '\n')

                    elif i == 0:
                        currentPathFile.write('\n') # title

                    else:
                        currentPathFile.write(originData[i].strip() + '\n') # image or empty

                # for log
                logLine = i

                # find last log file line
                if i >= lastLogFileLine:
                    findLastLogFileLine = True

            # open Files to Write & write
            originFile.close()
            currentPathFile.close()

            if finished:
                break

    logsFile.write(
        time.strftime('%Y-%m-%d %H:%M:%S') + ' | ' + logFilePath + ' | ' + str(logLine) + ' | ' + str(capacity) + '\n')
    logsFile.close()


translate()
