# 构造函数
# 在对象实例化时，系统自动调用的一个一个函数，叫构造函数，通常用来对实例对象初始化

# 如果子类中没有构造函数，则自动向上找，直到找到

# 首先找C的构造函数，如果没找到，往上导，按照MRO的顺序往上找

class Person:
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "Noname"

    name = property(fget, fset, fdel, "描述")


p1 = Person()
p1.name = "my name "
print(p1.name)




