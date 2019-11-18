import sys


def readFile(file_path):
    try:
        f = open(file_path, 'r')
        return f.read()
    except IOError:
        print(f"Arquivo {file_path} não existe")
        sys.exit()


def writeFile(file_path, content):
    f = open(file_path, 'w')
    return f.write(content)
