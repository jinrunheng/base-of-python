# print("nice to meet you".find("ee"))
# print("nice to meet you".find("ee",0,7))

str = "nice to meet you,I need your help"
print(str.find("ee")) # 返回第一个找到的位置
print(str.find("ee",11,len(str) - 1))

is_exist = "ee" in str
print(is_exist)

str1 = "hello world"
print(str1.replace("world","kim"))
print(str1.replace("o","O",2))