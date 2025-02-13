def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
kwargsAcceptFun(name="Yusuf", age=20, city="Tashkent")
