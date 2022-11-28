# testing to add scores/save them

def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])
    if last < int(score):
        f.close()
        file = open('scores.txt','w')
        file.write(str(score))
        file.close()
        return score
    return last