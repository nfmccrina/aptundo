import re
import sys

def parseLine(line):
    versionRegex = re.compile(r'\s+\(.*?\)(?:,\s+|\n)?')
    installRegex = re.compile(r'Install: ')

    return versionRegex.split(installRegex.sub('', line))[:-1]

def parseFile(fileContents):
    return list(filter(lambda l: re.search(r'^Install: ', l) != None, fileContents.splitlines()))

if __name__ == '__main__':
    fin = open('/var/log/apt/history.log', 'r')

    packageName = ''

    if (len(sys.argv) > 1):
        packageName = sys.argv[1]
    else:
        sys.exit()

    packageList = list(map(lambda x: ' '.join(parseLine(x)), filter(lambda x: x.find(packageName) > -1, parseFile(fin.read()))))

    if (len(packageList) > 0):
        print(packageList[0])
