import os


def makeTranslatedFile():
    # open README.md & get Lines containing paths
    f = open('./README.md', 'r')
    lines = list(filter(lambda line: line[0:2] == '- ', f.readlines()))

    for line in lines:
        # get file path & direcotry path
        path = line.split("(")[1].replace(")", "").rstrip()
        directory = "/".join(path.split("/")[:2]).rstrip()

        # file is not exist
        if not os.path.isfile(path):
            # if direcotry dose not exist, make directory.
            if not os.path.exists(directory):
                os.makedirs(directory)

            # open Files to Write & write
            wf = open(path, 'a')
            category = path.split("/")[1]
            name = path.split("/")[2].split(".")[0]
            wf.write("# **[" + category + "] " + name + "**")
            wf.close()
    f.close()
