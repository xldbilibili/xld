# 要求 根据生日判断星座
print("this system was made by xld")
month = int(input("请输入出生月份"))
day = int(input("请输入出生日期"))
birthday = 100*month + day

if  (int(birthday) >= 120 and int(birthday) <= 218) :
    print("水瓶座")
elif (int(birthday) >= 219 and int(birthday) <= 320) :
    print("双鱼座")
elif (int(birthday) >= 321 and int(birthday) <= 419) :
    print("白羊座")
elif (int(birthday) >= 420 and int(birthday) <= 520) :
    print("金牛座")
elif (int(birthday) >= 521 and int(birthday) <= 621) :
    print("双子座")
elif (int(birthday) >= 622 and int(birthday) <= 722) :
    print("巨蟹座")
elif (int(birthday) >= 723 and int(birthday) <= 822) :
    print("狮子座")
elif (int(birthday) >= 823 and int(birthday) <= 922) :
    print("处女座")
elif (int(birthday) >= 923 and int(birthday) <= 1023) :
    print("天秤座")
elif (int(birthday) >= 1024 and int(birthday) <= 1122) :
    print("天蝎座")
elif(int(birthday) >= 1123 and int(birthday) <= 1221) :
    print("射手座")
elif((int(birthday) >= 1222 and int(birthday) <= 1230 )
        or (int(birthday) >= 0 and int(birthday) <= 119)):
    print("摩羯座")
else :
    print("你找bug是吧")