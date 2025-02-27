dbfilename = 'test3_2.dat'

def readScoreDB():
    try:
        fH = open(dbfilename)
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    else:
        print("Open DB: ", dbfilename)

    scdb = []
    for line in fH:
        dat = line.strip()
        person = dat.split(",")
        record = {}
        for attr in person:
            kv = attr.split(":")
            record[kv[0]] = kv[1]
        scdb += [record]
    fH.close()
    return scdb


def writeScoreDB(scdb):
    fH = open(dbfilename, 'w')
    for p in scdb:
        pinfo = []
        for attr in p:
            pinfo += [attr + ":" + p[attr]]
        line = ','.join(pinfo)
        fH.write(line + '\n')
    fH.close()


def doScoreDB(scdb, scab=None):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age' : parse[2], 'Score' : parse[3]}
                scdb += [record]
            except:
                print("Invalid Commend")
        elif parse[0] == 'del':
            try:
                dummy = scdb.copy()
                for p in dummy:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except:
                print("Put the Name")
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'find':
            try:
                for k in scdb:
                    if k['Name'] == parse[1]:
                        print("Name:" + k['Name'] + ' ' + "Age:" + k['Age'] + ' ' + "Score:" + k['Score'])
            except:
                print("Syntax error")
        elif parse[0] == 'inc':
            try:
                plusscore = int(parse[2])
                for j in scdb:
                    if j['Name'] == parse[1]:
                        score = int(j['Score'])
                        score += plusscore
                        j['Score'] = str(score)
            except:
                print("syntax error")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)