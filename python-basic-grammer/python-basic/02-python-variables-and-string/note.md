## Python变量与字符串

#### 1. python函数与print函数的使用

函数就是python程序提前准备好的功能

每个函数都有对应的功能，函数的使用方式为：函数名(参数)

print函数

- print用于向控制台输出字符串
- `print("hello")`,`print(3)`

#### 2. python注释

python的两种注释方式：

1. 单行注释

```python
# 这是一段注释
```

2. 块注释

```python
"""
这是一段多行注释
"""
```

#### 3. 变量的定义与使用

定义变量与赋值

```python
name = "kim"
salary = 1900.1
is_weekend = True
```

#### 4. 变量的命名要求

1. 变量名要求见名知意
2. 变量名只能包含字母，下划线与数字，并且要求不能以数字开头
3. 变量不能不能python的关键字重名

和Java驼峰式命名不同，变量的命名单词小写，多个单词之间使用下划线进行连接

#### 5. 变量的数据类型

1. 变量在赋值时会自动判断数据的类型

2. python最常用的有四种数据类型

   1. 字符串：str(string)
   2. 整数：int(integer)
   3. 浮点数：float
   4. 布尔型：bool(boolean)

3. type函数

   1. type函数用于得到变量的数据类型
   2. 语法为：变量 = type(变量名)

   

```python
# 字符串类型
name = "Kim"
# 整数类型
age = 28
# 浮点数类型
weight = 143.5
# 布尔型
is_boy = True

print(name)
print(age)
print(weight)
print(is_boy)

# type函数用于得到变量的数据类型
type_of_name = type(name)
type_of_age = type(age)
type_of_weight = type(weight)
type_of_is_boy = type(is_boy)

print(type_of_name)
print(type_of_age)
print(type_of_weight)
print(type_of_is_boy)
```



#### 6. 基本运算符的使用

| 运算符 | 说明     |
| ------ | -------- |
| +      | 加       |
| -      | 减       |
| *      | 乘       |
| /      | 除       |
| //     | 除法取整 |
| %      | 取模     |
| **     | 幂       |

示例：

```python
# 加
print(3 + 3)
# 减
print(10 - 7)
# 乘
print(3 * 2.5)
# 浮点数除
print(10 / 2)
# 除法取整
print(10 // 2)
# 取模
print(8 % 3)
# 幂
print(2 ** 3)
```

#### 7. input函数的应用

input函数可以使用接收用户的输入

语法格式：`变量 = input("提示信息")`

示例：

```python
mobile = input("请输入您的手机号: ")
# 在用户输入完毕后，会自动将用户输入的结果保存到mobile这个变量中
print("您的手机号为: " + mobile)
```

在控制台中输入的数据类型为字符串，字符串和数字可以进行相互转换

- 字符串 -> 数字 : `int(字符串),float(字符串)`
- 数字 -> 字符串：`str(数字)`

示例：

```python
num = input("请输入一个数字: ")
print("这个数字乘以2的结果为: " + str(int(num) * 2))
```



#### 8. 程序的调试

- pycharm提供了debug功能
- 调试功能允许程序单步执行，方便开发者跟踪运行结果

#### 9. 字符串的创建与拼接

字符串就是一系列的字符；字符串可以使用单引号，也可以使用双引号

```python

# 字符串的创建
str1 = "hello"
str2 = 'Hello World'
str3 = "I told my girl friend 'She is beautiful'"
str4 = 'I told my girl friend "She is beautiful"'
print(str1)
print(str2)
print(str3)
print(str4)
```

字符串的拼接使用 “+” 处理；和Java不同，非字符串类型不能自动通过加号进行转换

```python

# 字符串的拼接
str5 = "Hello"
str6 = "World"
print(str5 + str6)
str1 = "my age is "
str2 = 27
print(str1 + str(str2))

```

#### 10. 字符串大小写转换

在python中字符串提供了大量函数，允许让我们对字符串进行加工

在python3中，有五个大小写函数

| 函数名            | 说明               |
| ----------------- | ------------------ |
| str.lower()       | 转换为小写         |
| str.upper()       | 转换为大写         |
| str.capitalize(0) | 字符串首字母大写   |
| str.title()       | 每个单词首字母大写 |
| str.swapcase()    | 大小写互换         |

示例：

```python
print("Hello".lower())

print("hello".upper())

print("hello".capitalize())

print("hello world".title())

print("hELLO wORLD".swapcase())
```



#### 11. 格式化字符串

```python
str.format()
```

示例：

```python
print("{} {} you".format("I","love"))
```

上述程序的输出为

```
I love you
```

format函数也提供了按照位置格式化的功能，例如：

```python
print("{3}{2}.{1}.{0}".format("com","bilibili","www","https://"))
info = "My name is {p1},{p2} years old. I love {p3}".format(p1=name, p2=age, p3="Marry")
print(info)
```

上述程序的输出为:

```
https://www.bilibili.com
My name is Kim,26 years old. I love Marry
```

#### 12. 数字格式化输出

format函数支持数字格式化,以及国际货币形式的格式化

示例：

```python
num = format(123456.789, '0.2f')  # 小数保留2位
print(num)
```

需要注意的是，num的类型为str

在字符串格式化输出时，如遇需要格式化输出的数字，则需要在{}内增加`:`前缀，之后写上数字格式化语句

示例：

```python
print(format(amt,",")) # 转换为货币形式
print(format(amt,"0,.2f")) # 将其转换为货币形式并且小数部分保留两位

account = "8810381"
amt = 123445.5
print("请您向{}账户转账¥{:0,.2f}元".format(account,amt))
```

#### 13. 早期的字符串格式化

早期的字符串格式化使用`%s`,`%d`,`%f`来格式化字符串

示例：

```python
print("My name is %s, and I am %d years old. My weight is %.2f"%("Kim",25,143.2))
```

#### 14.  制表符与换行符

制表符:`\t`

换行符: `\n`

```python
table = "姓名\t性别\t年龄\n张三\t男\t35"
print(table)
```

输出如下：

```
姓名	性别	年龄
张三	男	35
```

#### 15. 删除字符串中的空白

python提供了如下函数来删除字符串中的空白,这个函数并不能改变原字符串

| 函数名       | 说明                 |
| ------------ | -------------------- |
| str.strip()  | 删除字符串两端的空白 |
| str.lstrip() | 删除字符串左侧的空白 |
| str.rstrip() | 删除字符串右侧的空白 |

```python
# 字符串删除空白
str1 = " hello "

print(str1)
print(len(str1))
# 去除两端的空格
print(str1.strip())
print(len(str1.strip()))
# 去除左侧的空格
print(str1.lstrip())
print(len(str1.lstrip()))
# 去除右侧的空格
print(str1.rstrip())
print(len(str1.rstrip()))
```

#### 16. 查找与替换字符串

查找字符串

`str.find()`用于获取子字符串出现的位置(严格来说返回第一个出现的位置，如果没有出现过则返回-1)

语法为:

```python
str.find(目标字符串,[开始位置],[结束位置])
```

示例程序：

```python
print("nice to meet you".find("ee"))
print("nice to meet you".find("ee",0,7))
```

返回结果:

```
9
-1
```

判断某个字符串是否出现过使用`in`

```python
str = "nice to meet you,I need your help"
print(str.find("ee")) # 返回第一个找到的位置
print(str.find("ee",11,len(str) - 1))

is_exist = "ee" in str
print(is_exist)
```

字符串替换

`str.replace()` 函数用于字符串替换;这个函数并不会改变字符串的值

语法为：

```python
str.replace(原始字符串,目标字符串,[替换次数])
```

示例程序:

```python
str1 = "hello world"
print(str1.replace("world","kim"))
print(str1.replace("o","O",2))
```

输出结果：

```
hello kim
hellO wOrld
```



