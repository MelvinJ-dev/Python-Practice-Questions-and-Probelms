def escape(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


escape(echo = "~(0||0)")