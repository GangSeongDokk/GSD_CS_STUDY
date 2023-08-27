from time import sleep, time
import random

def slowprint(*printobj):
    for each in printobj:
        for i in each:
            sleep(0.2)
            print(i, end="", flush=True)
        if printobj[-1] != each:
            sleep(0.2)
            print(" : ", end="", flush=True)
    print()

def waiting(waitingstr="룰렛이 돌아가고 있습니다...", waitingtime=3):
    strlen = len(waitingstr)
    start = time()
    strlist = []
    spin = "\\|/-"
    spinlen = len(spin)
    for i in range(strlen):
        strlist.append(waitingstr[i:] + waitingstr[:i])
    print()
    while True:
        for n, i in enumerate(strlist):
            sleep(0.1)
            print(f"\r {spin[n % spinlen]}   {i}", end="", flush=True, sep="")
            if time() - start > waitingtime:
                print("\n")
                return