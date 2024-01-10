class ParentEX1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value
    
class ChildEx1(ParentEX1):
    pass

c1 = ChildEx1()
p1 = ParentEX1()

print(c1.get_value())
print(p1.get_value())