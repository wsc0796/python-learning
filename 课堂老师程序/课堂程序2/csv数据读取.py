csv_file=open('score.csv',encoding='utf-8')
lines=[]
for line in csv_file:           # 依次读取一行数据
    line=line.replace('\n','')  # 把该行数据的'\n'替换成空串
    lines.append(line.split(','))  # 把','分隔的子列表追加到line列表中
print(lines)
csv_file.close()