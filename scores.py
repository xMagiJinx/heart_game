# testing to add scores/save them
import time
def add_scores():
    """Trying to make the score change based off of time"""
    clock = .001 * time.time()

    clock1 = .001 * time.time() + .005
    difference = clock1 - clock
    return difference


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