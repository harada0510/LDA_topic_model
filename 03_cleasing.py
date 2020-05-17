# coding: utf-8

a = open("university.txt", "r")
b = open("document.txt", "r")
c = open("university_fix.txt", "w")
d = open("document_fix.txt", "w")

#中身のない行を検知してその行番号をリスト化
num = 0
delete_row = []

for i in b:
    num += 1
    i = i.rstrip()
    if i == "":
        print(num)
        delete_row.append(num)
    else:
        d.write(i+"\n")
print(delete_row)

b.close()
d.close()

#リストに含まれる行番号の大学名を取り除く
num = 0
for i in a:
    i = i.rstrip()
    num += 1
    if num in delete_row:
        print("hit!")
    else:
        c.write(i+"\n")

a.close()
c.close()
