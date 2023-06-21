<<<<<<< HEAD
import zipfile
import glob


total = 0

myfolder=glob.glob("./sample/*[13579]_kgu.txt")
for myfile in myfolder:
    with open(myfile, encoding='utf-8') as file:
        try:
            number=int(file.readline())
        except ValueError :
            continue
        total += number


print("奇数ファイルの数字の合計:",total )
=======
import zipfile
import glob


total = 0

myfolder=glob.glob("./sample/*[13579]_kgu.txt")
for myfile in myfolder:
    with open(myfile, encoding='utf-8') as file:
        try:
            number=int(file.readline())
        except ValueError :
            continue
        total += number


print("奇数ファイルの数字の合計:",total )
>>>>>>> origin/main
