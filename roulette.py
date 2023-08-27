import random
from datetime import datetime, timedelta
from python.logo import logo
from python.setting import studysetting, changesetting
from python.writemd import writemd
from python.slowprint import slowprint, waiting

WEEKNAME = ["월", "화", "수", "목", "금", "토", "일"]
MEMBERS, MEETING_DATE = studysetting()
MEMBERS_COUNT = len(MEMBERS)
insp = lambda y : list(map(lambda x : x.strip(), input().split(y)))


logo()

titles = []
chapter = ""
while len(titles) < 3:
    title = insp("=")

    if title[0] == "exit":
        break

    elif title[0] == "0":
        titles = []
        print("멤버 변경 : 1")
        print("날짜 변경 : 2")
        if input() == "1":
            print("가입 혹은 탈퇴 멤버의 이름(쉼표로 구분) : ")
            memberlist = insp(",")
            for member in memberlist:
                if member in MEMBERS:
                    MEMBERS.remove(member)
                    MEMBERS_COUNT -= 1
                else:
                    MEMBERS.append(member)
                    MEMBERS_COUNT += 1
            changesetting(MEMBERS, MEETING_DATE)
        else:
            print("변경할 날짜(쉼표로 구분) : ")
            MEETING_DATE = insp(",")
            changesetting(MEMBERS, MEETING_DATE)
    
    elif title[0] == "1":
        print("챕터 명을 입력해주세요 : ")
        chapter = input().strip()
    
    elif title[0] == "2":
        print("발표할 요일을 한글자로 입력해주세요 : ")
        MEETING_DATE = [input().strip()]

    elif title[-1].isdigit():
        num = int(title[-1])
        if len(titles) + num > 3:
            print("너무 많습니다.")
        else:
            for i in range(1, num + 1):
                titles.append(title[0] + f" ({i}/{num})")

    else:
        titles.append(title[0])

if len(titles) == len(MEMBERS):
    today = datetime.now()
    nextdate = datetime.now()
    confirmdate = ""
    for i in range(1, 8):
        nextdate = today + timedelta(days=i)
        if WEEKNAME[nextdate.weekday()] in MEETING_DATE:
            break
    
    confirmdate = nextdate.strftime(format="%Y.%m.%d") + " " + WEEKNAME[nextdate.weekday()]
    while True:
        topics = random.sample(titles, 3)
        people = random.sample(MEMBERS, 3)
        waiting(waitingtime=5)
        print("#"*50 + "\n")
        print(f"{confirmdate}요일 스터디 일정")
        print("#"*50 + "\n")
        for i in range(MEMBERS_COUNT):
            slowprint(people[i], topics[i])
        print("\n" + "#"*50)
        print("\n이대로 진행할까요?")
        print("예 : 1")
        print("중단 : exit")
        crt = input()
        if crt == "1":
            writemd(people, topics, confirmdate.split()[0], chapter)
            break
        elif crt == "exit":
            break
