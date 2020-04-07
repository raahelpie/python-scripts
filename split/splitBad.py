fileName = input("File to split: ")
linesForEachFile = int(input("Lines for each file: "))
fileNumber = 1
with open(fileName, 'r') as rf:
    alllines = rf.readlines()
    count = 0
    i = 0
    endOfFile = False
    while i < len(alllines):
        while count < linesForEachFile and i < len(alllines):
            wf = open(f'file{fileNumber}', 'a+')
            # try:
            #     wf.write(alllines[i])
            # except IndexError:
            #     endOfFile = True
            #     break
            wf.write(alllines[i])
            i += 1
            count += 1
        if endOfFile:
            break
        wf.close()
        fileNumber += 1
        count = 0

