print("欢迎使用收银台程序")
is_vip = input("请输入您的卡号：")

is_vip  = True if is_vip == "123" else False

price = float(input("请输入商品的单价："))
count = int(input("请输入商品的数量："))

total_price = price * count * 0.8 if is_vip == True else price * count

print("你的付款金额为：" + str(total_price))
