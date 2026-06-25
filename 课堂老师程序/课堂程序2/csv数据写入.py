__author__ = '86131'
csv_file=open('score.csv',encoding='utf-8')
file_new=open('count.csv','w+',encoding='utf-8')
lines=[]
for line in csv_file:
    line=line.replace('\n','')  # 把该行数据的'\n'替换成空串
    lines.append(line.split(','))  # 把','分隔的子列表追加到line列表中
print(lines)
# 添加表头字段
lines[0].append('总分')
# 添加总分
for i in range(1,len(lines)):
    # idx=i+1
    sun_score=0
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():  # 如果该行元素是整数
            sun_score+=int(lines[i][j])
    lines[i].append(str(sun_score)) # 累加和追加到该行末尾
for line in lines:
    print(line)
    file_new.write(','.join(line)+'\n')# 用','分隔数据形成字符串
csv_file.close()
file_new.close()
