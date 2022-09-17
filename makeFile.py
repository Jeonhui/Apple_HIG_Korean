import os


def makeFile():
    f = open('./README.md', 'r')
    lines = list(filter(lambda line: line[0:2] == '- ', f.readlines()))
    for line in lines:
        path = line.split("(")[1].replace(")", "").rstrip()
        directory = "/".join(path.split("/")[:2]).rstrip()

        if not os.path.isfile(path):
            if not os.path.exists(directory):
                os.makedirs(directory)
            wf = open(path, 'a')
            category = path.split("/")[1]
            name = path.split("/")[2].split(".")[0]
            wf.write("# **[" + category + "] " + name + "**")
            wf.close()
    f.close()


makeFile()
