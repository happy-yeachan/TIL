def main():
    """dfadsf"""
    print("dsfa")


class test(object):
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return (
            "Get method called. -> self : {}, obj : {}, objtype : {}, name : {}".format(
                self, obj, objtype, self.name
            )
        )

    def __set__(self, obj, name):
        print("Set method called.", obj)
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")

    def __delete__(self, obj):
        print("Delete method called.")
        self.name = None


class Sample1(object):
    name = test()


s1 = Sample1()

# __set__ 호출
s1.name = "Descriptor Test1"

# 예외 발생
# s1.name = 10

# attr 확인
# __get__ 호출
print("Ex1 > ", s1.name)

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print("Ex1 > ", s1.name)

print("sdfasd")
