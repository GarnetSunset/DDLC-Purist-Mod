import os
import sys

owd = os.getcwd()

directory_list = list()
for root, dirs, files in os.walk(owd+"/itch.io-downloader", topdown=False):
    for name in dirs:
        if "DDLC" in name:
            directory_list.append(name)
DDLCDir = ''.join(directory_list)
VersionStart = DDLCDir.index("DDLC")
VersionEnd = DDLCDir.index("pc")

DDLCVer = DDLCDir[VersionStart+5:VersionEnd-1]

if not os.path.isfile("DDLCModVer.ini"):
    modVer = open("DDLCModVer.ini", "w")
    modVer.write(DDLCVer)
    modVer.close()
else:
    with open("DDLCModVer.ini", 'r') as myfile:
        listVer = myfile.readlines()
        CurVer = ''.join(listVer)
        if CurVer != DDLCVer:
            print("Time To Check The Diffs!")
        else:
            print("You're up to date!")
