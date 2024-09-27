import os

os.system("clear")
myDic = {"name": None, "url": None, "desc": None, "rating": None}

def printDic():
  for name, value in myDic.items():
    print(f"{name}: {value}")
  

for name, value in myDic.items():
  myDic[name] = input(f"{name}: ")

print()
printDic()