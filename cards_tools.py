#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#
#
#
#
# 记录所有的名片字典
card_list = []

def show_menu():

    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出菜单")
    print("*" * 50)

def new_card():
    print("-" * 50)
    print("新增名片")
#     1，提示用户详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ:")
    email_str = input("请输入邮箱：")

#  2，使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
# 3，将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
# 4，提示用户添加成功
    print("添加 %s 的名片成功"% name_str)

def show_all():
    print("-" * 50)
    print("显示所有")
    if len(card_list) == 0:
        print("当前没有名片记录，请使用新增功能添加名片！")

        return
    for name in ["姓名",           "电话",   "QQ",   "email"]:
        print(name, end="\t\t")
    print("")
    print("="*50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["qq"],
                                      card_dict["email"]))

def search_card():
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名： ")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\temail")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到%s" %find_name)

def deal_card(find_dict):
    print(find_dict)
    action_str = input("请输入对名片的操作："
                       "[1] 修改 [2] 删除 [0] 返回上一级菜单")
    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq:")
        find_dict["email"] = input_card_info(find_dict["email"], "email:")
        print("修改名片")
    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片")

def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)

    if len(result_str) == 0:
        return dict_value
    else:
        return result_str

