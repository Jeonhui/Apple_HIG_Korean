import os


def makeTranslatedFile():
    # open README.md & get Lines containing paths
    f = open('./README.md', 'r')
    lines = list(filter(lambda line: line.strip()[:3] == '- [', f.readlines()))

    for line in lines:
        # get file path & direcotry path
        path = line.split("(")[1].replace(")", "").rstrip()
        directory = "/".join(path.split("/")[:2]).rstrip()
        subDirectory = "/".join(path.split("/")[:3]).rstrip() if len(path.split("/")) == 4 else None

        # file is not exist
        if not os.path.isfile(path):
            # if direcotry dose not exist, make directory.
            if not os.path.exists(directory):
                os.makedirs(directory)
            if subDirectory is not None and not os.path.exists(subDirectory):
                os.makedirs(subDirectory)


            # open Files to Write & write
            wf = open(path, 'a')
            category = path.split("/")[1] if subDirectory is None else path.split("/")[1] + '-' + path.split("/")[2]
            name = path.split("/")[-1].split(".")[0]
            wf.write("# **[" + category + "] " + name + "**")
            wf.close()
    f.close()

makeTranslatedFile()