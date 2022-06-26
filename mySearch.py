import re

def quickSearch(keyword):
    f = open("ezKeylogger/logs/log.txt", "r")


    reg = re.compile(keyword)
    index = 0

    for line in f:
        index += 1
        flag = reg.search(line)
        if flag != None:
            return index
    
    return -1