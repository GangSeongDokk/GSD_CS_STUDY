from os import makedirs
from urllib import parse

READMEDIR = "README.md"

def writemd(members, topics, meetingdate, chapter=""):
    lastchap = ""
    isnewline = False
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.readlines()
        if readme[-1][-1] == "\n":
            isnewline = True
        for linenum in range(len(readme) - 1, -1, -1):
            spline = readme[linenum].split()
            if spline and spline[0] == "##":
                lastchap = " ".join(spline[1:])
                break
    
    membercnt = len(members)
    with open(READMEDIR, "a+", encoding="utf-8") as f:
        
        if not isnewline:
            f.write("\n")
        
        if chapter:    
            f.write(f"\n## {chapter}\n\n")
            f.write("|내용|담당|발표일|\n|-|-|-|\n")
            makedirs(f"{chapter}")
            lastchap = chapter

        for i in range(membercnt):
            topicfile = topics[i]
            if "/" in topicfile:
                topicname = topics[i].split("(")
                topicfile = topicname[0].strip() + topicname[1].split("/")[0].strip()
            f1 = open(f"{lastchap}/{topicfile}.md", "w", encoding="utf-8")
            f1.close()
            lastchap2 = "%20".join(lastchap.split())
            topicfile2 = "%20".join(topicfile.split())

            f.write(f"|[{topics[i]}](./{lastchap2}/{topicfile2}.md)|{members[i]}|{meetingdate}|\n")