# python 高级
# 1. 模块
- 一个模块就是一个包含python代码的文件，后缀.py，模块就是一个python文件
- 为什么用模块
    - 程序太大，编写维护不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名控件使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，任何代码可以直接书写
    - 规范
        - 函数(单一功能)
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name 
        - import 模块 as 别名
        - from module_name import func_name, class_name, *（导入模块所有内容）
     
     if __name__ == 'main': 的使用
        可以有效避免模块代码被导入的时候被动执行的问题
        建议所有程序的入口都已此代码为入口

# 模块搜索路径
- 什么是模块搜索路径
    - 加载模块的时候，系统会在那些地方寻找此模块
系统默认的模块搜索路径
package_name . path
-添加搜索路径
    sys.path.append(dir)
- 模块的加载顺序
    1 上搜索内存中已经加载好的模块
    2 搜索python的内置模块
    3 搜索sys.path 路径
    
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的机构
    |- - -包
    |- - -|- - - __init__.py 包的标志
    |- - -|- - - 模块1
    
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式
                package_name.func_name
                package_name.class_name.func_name()
                
        - import package_name as p
            - 具体用法跟作用方式，跟简单导入一致
            - 注意的是此种方法是默认对__init__.py内容的导入
            
        - import package.module [as p]
            - 导入包中某一个具体的模块
            - 使用方法
                package.module.func_name
                package.module.class.func()
                package.module.class.var
                
        - from package import module1, module2....*
        - 此种导入方法不执行__init__的内容
        - from package import * 
            - 导入当前包__init__.py 文件中的所有的函数和类
            使用方法
                func_name()
                class_name.func()
                class_name.var
        - from package.module import *
            - 导入包中指定的模块的所有内容

        - 在开发环境中经常会用其他模块，可以在当前包中直接导入其他模块中的内容
        - import 完整的包或模块路径
        __all__的用法
            - 在使用from package import * 时，* 可以导入的内容
            - __init__.py中如果文件为空，或者没有__all__ 那么只可以吧initz中的导入
            - init 如果设置了all的值，