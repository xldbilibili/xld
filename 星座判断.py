# 要求 根据生日判断星座
print("this system was made by xld")
month = int(input("请输入出生月份"))
day = int(input("请输入出生日期"))
birthday = 100*month + day

if 120 <= int(birthday) <= 218:
    print("水瓶座")
elif 219 <= int(birthday) <= 320:
    print("双鱼座")
elif 321 <= int(birthday) <= 419:
    print("白羊座")
elif 420 <= int(birthday) <= 520:
    print("金牛座")
elif 521 <= int(birthday) <= 621:
    print("双子座")
elif 622 <= int(birthday) <= 722:
    print("巨蟹座")
elif 723 <= int(birthday) <= 822:
    print("狮子座")
elif 823 <= int(birthday) <= 922:
    print("处女座")
elif 923 <= int(birthday) <= 1023:
    print("天秤座")
elif 1024 <= int(birthday) <= 1122:
    print("天蝎座")
elif 1123 <= int(birthday) <= 1221:
    print("射手座")
elif((1222 <= int(birthday) <= 1230)
        or (0 <= int(birthday) <= 119)):
    print("摩羯座")
else:
    print("你找bug是吧")
