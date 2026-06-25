__author__ = '86131'
try:
    with open("text2.txt",encoding="utf-8")as f1:
        with open("text3.txt",'w',encoding="utf-8")as f2:
            chunk=100
            while True:
                context=f1.read(chunk)
                if not context:
                    break
                f2.write(context)
except FileNotFoundError as e:
    print(e)