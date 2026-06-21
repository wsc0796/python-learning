"""
实验 3：好友关系系统（选做）。

功能：
1. 添加好友
2. 删除好友
3. 备注好友
4. 展示好友
5. 好友分组
0. 退出

运行：python EXAM_PREP/lab_oop_report/friend_manager.py
"""


friends: list[str] = []
groups: dict[str, list[str]] = {}


def show_menu() -> None:
    print("\n====== 好友管理系统 ======")
    print("1. 添加好友")
    print("2. 删除好友")
    print("3. 备注好友")
    print("4. 展示好友")
    print("5. 好友分组")
    print("0. 退出")


def add_friend() -> None:
    name = input("请输入要添加的好友：").strip()
    if not name:
        print("好友姓名不能为空")
        return
    if name in friends:
        print("好友已存在")
        return
    friends.append(name)
    print("好友添加成功")


def delete_friend() -> None:
    name = input("请输入删除好友姓名：").strip()
    if name not in friends:
        print("好友不存在")
        return

    friends.remove(name)
    for group_friends in groups.values():
        if name in group_friends:
            group_friends.remove(name)
    print("删除成功")


def rename_friend() -> None:
    old_name = input("请输入要修改的好友姓名：").strip()
    if old_name not in friends:
        print("好友不存在")
        return

    new_name = input("请输入修改后的好友姓名：").strip()
    if not new_name:
        print("新姓名不能为空")
        return
    if new_name in friends:
        print("新姓名已存在")
        return

    index = friends.index(old_name)
    friends[index] = new_name

    for group_friends in groups.values():
        for i in range(len(group_friends)):
            if group_friends[i] == old_name:
                group_friends[i] = new_name

    print("备注成功")


def show_friends() -> None:
    print("1. 展示所有好友")
    print("2. 展示分组好友")
    choice = input("请选择展示方式：").strip()

    if choice == "1":
        if not friends:
            print("暂无好友")
        else:
            print("所有好友：")
            for friend in friends:
                print(friend)
    elif choice == "2":
        group_name = input("请输入分组名：").strip()
        if group_name not in groups:
            print("分组不存在")
            return
        if not groups[group_name]:
            print("该分组暂无好友")
            return
        print(f"{group_name} 分组好友：")
        for friend in groups[group_name]:
            print(friend)
    else:
        print("输入无效")


def manage_group() -> None:
    choice = input("是否创建新的分组？(y/n)：").strip().lower()
    if choice == "y":
        group_name = input("请输入新分组名：").strip()
        if not group_name:
            print("分组名不能为空")
            return
        if group_name in groups:
            print("分组已存在")
        else:
            groups[group_name] = []
            print("分组创建成功")

    friend_name = input("请输入要分组的好友姓名：").strip()
    if friend_name not in friends:
        print("好友不存在，请先添加好友")
        return

    group_name = input("请输入目标分组名：").strip()
    if group_name not in groups:
        print("分组不存在")
        return

    if friend_name not in groups[group_name]:
        groups[group_name].append(friend_name)
    print("好友分组成功")


def main() -> None:
    while True:
        show_menu()
        choice = input("请输入您的选项：").strip()

        if choice == "1":
            add_friend()
        elif choice == "2":
            delete_friend()
        elif choice == "3":
            rename_friend()
        elif choice == "4":
            show_friends()
        elif choice == "5":
            manage_group()
        elif choice == "0":
            print("已退出好友管理系统")
            break
        else:
            print("输入无效，请重新输入")


if __name__ == "__main__":
    main()

