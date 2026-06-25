__author__ = '86131'
li=[]
try:
    with open("score.csv",encoding="utf-8")as f:
        for i in f:
            s=i.replace("\n","")
            li.append(s.split(","))
except FileNotFoundError as e:
    print(e)
print(li)
li[0].append("总分")
for i in range(1,len(li)):
    sum=0
    for j in range(1,len(li[i])):
         sum+=int(li[i][j])
    li[i].append(str(sum))
print(li)
with open("count.csv","w",encoding="utf-8")as f2:
    for line in li:
        f2.write(','.join(line)+"\n")



