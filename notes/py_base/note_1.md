# 利用多继承来实现的一种设计模式Minxin
# 要表示一个单一的功能
# 职责必须单一，如果有多个功能，则写多个Minxin
# Minxin 不能依赖于子类实现
# 类的相关函数
class A:
    pass

issubclass(a, b) a是不是b 的子类
isinstance(a, b) a是不是b的实例
hasattr(A, "name") 检测一个成员是不是在类中
getattr:get attr
setattr:set attr
delattr:delete attr
dir（A）获取对象的成员列表

-OOP 类的成员描述符（属性）

# 创建Student类描述学生类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def intro(self):
        print("my name is {0}".format(self, name))
    
s1 = Student("A", 19)
s1.intro()
类的成员描述符：为了在类的成员属性进行相关操作而创建的一种方式
get set delete
三种操作
使用类的描述符：
    使用类实现描述器
    使用属性修饰符
    使用property函数
    property(fget, fset, fdel, doc)

__dict__:以字典的方式显示类的成员组成
__doc__:获取类的文档信息
__name__:获取类的名称，如果在模块中使用，获取模块的名称
__bases__:获取某个类的所有弗雷，以元组的方式显示


--魔术方法
- 魔术方法就是不需要人为调用的方法，基本时在特定的时刻自动触发
- 魔术方法的同意的特征，方法名被前后各两个下划线包裹
__init__:构造函数
__new__:对象实例化方法，此函数比较特殊，一般不需要使用
- __call__ 对象当函数函数使用的时候触发
- __str__ 当对象被当作字符串使用的时候调用
__repr__ 放回字符串，跟__str__具体区别百度。。。
class A:
    def __init__(self, name = 0):
        print('init'')
    def __call__(self):
        print('call')
a = A()
a()


- __str__

class A:
    def __init__(self, name = 0):
        print('init'')
    def __call__(self):
        print('call')
    def __str__(self):
        return "kyo"
a = A()
print(a)

- 描述符相关
 - __set__
__get__
__delete__

- 属性操作相关

__getattr__:访问一个不存在的属性时触发
__setattr__对成员属性进行设置的时候触发
 - 参数: self用来获取当前对象
          被设置的属性名称，以字符串形式出现
          需要对属性名称设置值
   作用，进行属性设置的时候惊醒验证或修改
   注意：在该方法中不能对属性直接进行赋值操作，否则死循环   案例中
- 运算分类相关魔术方法
    __gt__:进行大于判断的时候触发的函数
        参数：self 
               第二个参数时第二个对象
               返回值可以是任意值，推荐返回布尔值
               

   

# __getattr__
class A:
    name = "a"
    age = 18
     def __getattr__(self, name):
        print("getattr")
        print(name)
        
a = A()
print(a.name)
print(a.attr)

# setattr
class Person:
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性:{0}.format(name))
        # 下面会导致死循环、
        # self.name = value
        # 为了避免死循环，规定统一调用父类的魔法函数
        super().__setattr__(name,value)
        
p = Person()
print(p.__dict__)
p.age = 18

# __gt__

class Student():
    def __init__(self, name):
        self._name = name
    def __gt__(self, obj):
        print("{0}会比{1}大么?".format(self, obj))
        return self._name > obj._name
        
s1 = Student("one")
s2 = Student("two")

print(s1 > s2)


# 类和对象的三种方法
实例方法
    需要实例化对象才能使用的方法，使用过程中可能需要截至对象的其他对象的方法完成
    
静态方法
    不需要实例化，通过类直接调用
类方法
    不需要实例化
    
# 案例
class Person：
    #实例方法
    def eat(self):
        print(self)
        print("eating")
    
    #类方法
    #类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("play")
    
    #静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("say")
        
        
p = Person()

#实例方法
p.eat()
# 类方法
Person.play()
p.play()
#静态方法
Person.say()
p.say()

具体区别百度


# 变量的三种用法

class A:
    def __init__(self):
        self.name = "haha"
        self.age = 18

a = A()
# 属性的三种方法
赋值
读取
删除
    
# 类属性 property
# 应用场景:对变量除了普通的三种操作，还想增加一些附加的操作，可以用perperty
class A:
    def __init__(self):
        self.name = "haha"
        self.age = 18
    # 此功能，对变量进行读取操作的时候用过执行的函数共呢个
    def fget(self):
        print("我被读取了")
    
    def fset(self, name):
        print("我被写入了)
        self.name = "a" + name
    
    def fdel(self):
        pass
    
    # property 的四个参数顺序是固定的
    # 第一个参数代表读取
    # 第二个写入
    # 第三个是删除
    name2 = porperty(fget,fset,fdel,"这是说明文档")

a= A()
print(a.name)

print(a.name2)
print()


# 抽象类
抽象方法 ：没有具体实现内容的方法称为抽象方法
抽象方法的主要意义是贵方了子类的行为和接口
抽象类的使用需要借助abc模块
    抽象类可以包含抽象方法，也可以包含具体方法
    抽象类中可以有方法也可以有属性
    抽象类不预序直接实例化
    必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
    假定子类没有实现所有继承的抽象方法，则子类也不能实例化
    抽象类的主要作用是设定类的标准，以便于开发的时候有统一的规范
import abc

class Animal:
    def sayHello(self):
        pass
        
class Dog(Animal):
    def sayHello(self):
        print("闻一下")

class Person(Animel):
    def sayHello(self):
        print("111")
        
        
# 抽象类的实现
import abc 
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
       
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

# 函数名可以当变量使用

def sayHello(name):
    print("{0}你好".format(name))
    
sayHello("ye")

# 自己组装一个类

class A:
    pass

def say(self):
    print("say")
    
A.say = say
a = A()
a.sya()


from types import MethodType

class A：
    pass

def say(self):
    print("say")
    
a = A()
a.say = MethodType(say, A)
a.say()

自定义类:
    类其实是一个类定义和各种方法的自由组合
    可以定义类和函数，然后自己通过类直接赋值
    可以借助于MethodType实现
    借助于type 实现
    利用元类实现 - MetaClass
        元类是类
        被用来创造别的类
        
    
# type
def say(self):
    print("say")
    
def talk(self):
    print("talk")
    
#用type 来创建一个类
 A = type("AName, (object, ),{"class_say":say,"class_talk":talk})
 
 
 # 元类
 # 元类写法是固定的，必须继承自type
 # 原来一般命名以MetaClass结尾
 class XuMetaClass(type):
    def __new__(cls, name, bases, attr):
        # 自己的业务处理
        print("haha")
        attrs['id'] = '000000'
        attrs['addr'] = "北京"
        return type.__new__(cls, name, bases, attr)
        
        
 # 元类定义完就可以使用，使用注意写法
 
 class Teacher(object, metaclass = XuMetaClass):
    pass
    
t = Teacher()
t.__dict__
t.id