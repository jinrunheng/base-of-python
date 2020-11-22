num = format(123456.789, '0.2f')  # 小数保留2位
print(num)
print(type(num))

amt = 322000.5
print(format(amt, ","))  # 转换为货币形式
print(format(amt, "0,.2f"))  # 将其转换为货币形式并且小数部分保留两位

account = "8810381"
amt = 123445.5
print("请您向{}账户转账¥{:0,.2f}元".format(account, amt))

"""
早期的格式化输出
"""
print("My name is %s, and I am %d years old. My weight is %.2f" % ("Kim", 25, 143.2))

# 制表符与换行符
table = "姓名\t性别\t年龄\n张三\t男\t35"
print(table)
