charge = 0.0
elec = input("请输入您本月的用电量:")
elec = float(elec)

if elec >= 1 and elec <= 240:
    charge = elec * 0.4883
elif elec > 241 and elec  <= 400 :
    charge = 240 * 0.4883 + (elec - 240) * 0.5383
else:
    charge = 240 * 0.4883 + 160 * 0.5383 + (elec - 400) * 0.7883

print("您本月的电费为：" + str(charge))

