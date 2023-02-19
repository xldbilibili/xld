import random  # 导入工具
user_date = int(input("出啥？（石头1 剪刀2 布3）"))
pc_date = random.randint(1, 3)
if ((user_date == 1 and pc_date == 2)  # 判断逻辑
        or (user_date == 2 and pc_date == 3)
        or (user_date == 3 and pc_date == 1)):
    print("玩家获胜")
elif user_date == pc_date:
    print("平局")
else:
    print("玩家失败")
