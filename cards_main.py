import cards_tools
while True:  # 无限循环语句，有用户决定什么时候退出系统
    #  显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作 ")
    print("你选择的操作是 [%s]" %action_str)
    if action_str in["1", "2", "3"]:
        # 新建名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查看全部名片
        elif action_str == "3":
            cards_tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # pass ，可以先占个位置。
    else:
        print("你输入的内容错误,请重新输入：")

