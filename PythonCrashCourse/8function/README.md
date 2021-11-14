

# function

## 注释风格

Google 版本

```python
def func(path, field_storage, temporary):
    '''基本描述

    详细描述

    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor
    '''
    pass
```


### 位置实参

传递参数时，一一对应形参


### 关键字形参

指定形参需要传递的参数，类似字典的结构，与位置无关

```python
function(parameter = value)
```

### 默认参数

形参指定默认参数

给形参指定默认值时，等号两边不要有空格：

def function_name(parameter_0,parameter_1='default value')

对于函数调用中的关键字实参，也应遵循这种约定：

function_name(value_0,parameter_1='value')

### notice

列表传递的时候，相当于传递的是引用，修改时会影响到外面

function(list)

传递副本

function(list[:])

### 传递变参

变参为元组类型

```python
def funtion(*param): 
    '''param is tuple type'''
    pass
```

综合 变参和形参，将变参放置在最后

```python
def function(param_1, *param_2):
    pass

# 传递变参，字典类型
def function(**args):
    pass

# 使用
# 字典形式传入 args
function(key_1 = value_1, key_2 = value_2)
```

### module

```
模块导入的方法：
1、导入整个模块：  
    1）、当要导入的模块和当前执行的程序在同一个路径时，直接使用import语句导入
        import 模块名      
        调用函数时，需指定模块名，格式如下：       
        模块名.函数名（参数）
        如：
            import time
            time.sleep(1)#time即模块名，sleep即函数名，括号里的1为参数
    2）、当要导入的模块与当前执行的程序不在同一路径，需要添加模块完整路径：
        import 模块名
        模块名.path.append('该模块的完整路径')
2、导入模块中特定函数：       
    from 模块名 import 函数名1，函数名2...        
    调用函数时，无需指定模块名，直接使用函数名调用即可
3、导入模块中的全部函数：      
    from 模块名 import*        
    调用时直接使用函数名即可调用，但因为导入的函数名与项目中的某些变量名重复，最好不要使用该方法。
4、为避免上述导入模块或模块中的函数名与当前程序中某些变量名重复，或导入的模块名过长的，调用不方便的问题，可以使用as将导入的模块或函数指定另外的别名：
    如：
        from 模块名 import A函数 as B #从模块导入函数A并重命名为B
        import A模块 as B #导入模块A并重命名为B
```

