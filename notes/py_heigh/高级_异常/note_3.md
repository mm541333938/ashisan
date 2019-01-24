# 异常
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下，出现的问题
- 在python里，异常是一个类，可以处理和使用
# 异常处理
- 不能保证程序永远正确运行
- 但是，必须保证程序在最坏的情况下得到的问题被妥善处理
- python的异常处理模块全部语法为:
    try:
        尝试实现某个操作
        如果没有出现异常，任务可以完成
        如果出现异常，将异常从当前代码块扔出去尝试解决异常
    except 异常类型1:
        解决方案1：用于尝试在此处处理异常解决问题
    except 异常类型2:
        解决方案2：用于尝试在此处处理异常解决问题
    except :
        解决方案:所有异常的解决方案
    else:
        如果没有出现任何异常，将会执行此处代码
    finally:
        管你有没有异常都会执行的代码

- 流程
    1 执行try下面的语句
    2 如果出现异常，则在except语句里查找对应异常惊醒处理
    3 如果没有出现异常，执行else 
    4 最后不管时候出现异常，都要执行finally语句
    - 出except(最少一个)意外，else 和 finally可选

# 捕获异常
# 具体错误类往前放
try:

except ZeroDivisionError as e: # 异常实例化
    print(e)
except Exception as e:
    print(e)
    
[else :
    print("没异常")
finally:
    print("总是执行")
]
# 用户手动引发异常
- 当某些情况，用户希望自己引发一个异常的时候， 可以使用
- raise 关键字来引发异常

try:
    print("aaaaaaa")
    # 手动引发一个异常
    # 注意语法：raise ErrorClassName
    raise ValueError
    print("还没完")
    
except NameError as e:
    print("NameError")
except ValueError as e:
    print(e)
    
# 自定义异常
- 只要是raise 异常，推荐自定义异常
- 在自定义异常的时候，一般包含：
    - 自定义异常代码
    - 自定义异常发生提示
    - 自定义发生异常的行数
- 最终的目的，方便程序员定义异常位置

class AError(ValueError):
    pass
    
try:
    print("aaaaaaa")
    # 手动引发一个异常
    # 注意语法：raise ErrorClassName
    raise ValueError
    print("还没完")
    
except NameError as e:
    print("NameError")
except AError as e:# 如果没有会找父类的error
    print(e)
except ValueError as e:
    print(e)
    
