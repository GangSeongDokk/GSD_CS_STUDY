def studysetting():
    with open("roulette/setting.txt", "r", encoding="utf-8") as f:
        members = f.readline().split()
        meetingdate = f.readline().split()
        return [members, meetingdate]

def changesetting(members, meetingdate):
    with open("roulette/setting.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(members) + "\n")
        f.write(" ".join(meetingdate))