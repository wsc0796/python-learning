try:
    with open("aa.flac","rb")as f1:
        with open("ee.flac",'wb')as f2:
            chunk=1000*1024
            while True:
                context=f1.read(chunk)
                if not context:
                    break
                f2.write(context)
except FileNotFoundError as e:
    print(e)








