"""
通讯录程序 —— 集成五大数据结构知识点

【知识点映射】
  dict           核心存储  {姓名: {详情}}
  list           搜索结果 + 操作日志
  tuple          联系人只读快照 (姓名, 手机, 邮箱)
  set            手机号查重
  string-methods 输入校验 isdigit/isalpha/strip/title
  slice          分页 + 手机号脱敏
"""
import sys, io, json, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============================================================
# 数据层
# ============================================================

# 【dict】核心存储 —— 嵌套字典
contacts: dict[str, dict] = {}         # {姓名: {"手机": str, "邮箱": str, "地址": str}}
phone_set: set[str] = set()            # 【set】手机号唯一集合，用于查重
history: list[tuple] = []              # 【list + tuple】操作日志：(操作类型, 姓名, 手机, 时间)

PAGE_SIZE = 3                          # 【slice】每页显示3条
SEARCH_DISPLAY_MAX = 5                 # 搜索最多显示条数
HISTORY_DISPLAY_MAX = 10              # 日志最多显示条数
DATA_FILE = "contacts.json"           # JSON持久化文件

# ============================================================
# 工具函数
# ============================================================

def validate_name(name: str) -> tuple[bool, str]:
    """校验联系人姓名是否合法。

    参数:
        name: 原始输入的姓名

    返回:
        (是否通过, 处理后的姓名或错误提示)
    """
    name = name.strip()                          # 【string-methods】去首尾空格
    if not name:
        return False, "姓名不能为空"
    if name.isdigit():                           # isdigit(): 纯数字不允许
        return False, "姓名不能是纯数字"
    if not name.replace(" ", "").isalpha():      # isalpha(): 去空格后是否为纯字母/中文
        return False, "姓名不能包含数字或特殊符号"
    if len(name) > 20:
        return False, "姓名太长（最多20字）"
    return True, name.title()                    # title(): 首字母大写


def validate_phone(phone: str, exclude_phone: str | None = None) -> tuple[bool, str]:
    """校验手机号格式与唯一性 —— isdigit + len + set查重

    参数:
        phone: 待校验的手机号
        exclude_phone: 排除的手机号（修改时传入旧号，避免自我冲突）

    返回:
        (是否通过, 处理后的手机号或错误提示)
    """
    phone = phone.strip()
    if not phone.isdigit():
        return False, "手机号只能包含数字"
    if len(phone) != 11:
        return False, f"手机号需要11位，你输入了{len(phone)}位"
    if phone != exclude_phone and phone in phone_set:  # 【set】排除自身后再查重
        return False, "该手机号已被其他联系人使用"
    return True, phone


def mask_phone(phone: str) -> str:
    """手机号脱敏，中间4位替换为星号。

    参数:
        phone: 11位手机号

    返回:
        脱敏后的字符串，如 138****8000
    """
    return phone[:3] + "****" + phone[7:]        # 【slice】切片拼接


def paginate(items: list, page: int) -> list:
    """用切片取当前页数据，自动处理末页越界。

    参数:
        items: 完整列表
        page: 页码（从1开始）

    返回:
        当前页的元素列表
    """
    start = (page - 1) * PAGE_SIZE
    return items[start:start + PAGE_SIZE]         # 【slice】切片自动处理越界


# ============================================================
# 持久化
# ============================================================

def load_data() -> None:
    """启动时从JSON文件加载通讯录数据"""
    global contacts, phone_set
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data: dict = json.load(f)
        contacts = data.get("contacts", {})
        phone_set = {info["手机"] for info in contacts.values()}
        print(f"[已加载 {len(contacts)} 位联系人]")
    except FileNotFoundError:
        pass  # 首次运行，无存档文件
    except json.JSONDecodeError:
        print("[警告] 存档文件损坏，将使用空通讯录")


def save_data() -> None:
    """退出时保存通讯录到JSON文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"contacts": contacts}, f, ensure_ascii=False, indent=2)
    print("[通讯录已保存]")


# ============================================================
# 业务功能
# ============================================================

def add_contact():
    """新增联系人 —— dict增 + string-methods校验 + set查重"""
    print("\n--- 新增联系人 ---")

    # 姓名校验
    name_raw = input("姓名：")
    ok, name = validate_name(name_raw)
    if not ok:
        print(f"[错误] {name}"); return

    # 检查重名
    old_phone = contacts.get(name, {}).get("手机")  # 如有旧号，用于校验时排除自身
    if name in contacts:                             # 【dict】key 存在性检查
        ans = input(f"「{name}」已存在，是否覆盖？(y/n)：")
        if ans.lower() != 'y':
            print("已取消"); return

    # 手机校验（先校验！传入旧号排除自身冲突）
    phone_raw = input("手机号：")
    ok, phone = validate_phone(phone_raw, exclude_phone=old_phone)
    if not ok:
        print(f"[错误] {phone}"); return

    # 校验通过后，再移除旧手机号
    if old_phone:
        phone_set.discard(old_phone)                # 【set】移除旧号

    # 邮箱、地址（可选）
    email = input("邮箱（可留空）：").strip()
    address = input("地址（可留空）：").strip()

    # 存储
    contacts[name] = {                            # 【dict】嵌套字典赋值
        "手机": phone,
        "邮箱": email,
        "地址": address,
    }
    phone_set.add(phone)                          # 【set】新手机号入集合

    # 记录日志
    history.append(("新增", name, phone, datetime.datetime.now().strftime("%m-%d %H:%M")))

    print(f"✅ 已添加：{name}  {mask_phone(phone)}")


def view_contacts():
    """查看联系人 —— dict遍历 + list + slice分页"""
    if not contacts:
        print("\n通讯录为空。"); return

    # 【list】将 dict 转为 (姓名, 详情) 的列表，方便分页
    contact_list = list(contacts.items())          # items() → 可迭代 → list

    total_pages = (len(contact_list) + PAGE_SIZE - 1) // PAGE_SIZE
    page = 1
    while True:
        print(f"\n--- 通讯录  第{page}/{total_pages}页 ---")

        # 【slice】切片取当前页
        page_items = paginate(contact_list, page)

        for name, info in page_items:
            # 【tuple】构造只读快照传给展示
            snapshot = (name, info["手机"], info["邮箱"])
            print(f"  📇 {snapshot[0]}  {mask_phone(snapshot[1])}  {snapshot[2]}")

        print(f"\n[N]下一页  [P]上一页  [Q]返回")
        cmd = input("> ").strip().lower()
        if cmd == 'n' and page < total_pages:
            page += 1
        elif cmd == 'p' and page > 1:
            page -= 1
        elif cmd == 'q':
            break
        else:
            print("无效操作或已到边界")


def search_contacts():
    """搜索联系人 —— string-methods + list结果集 + dict遍历"""
    keyword = input("\n输入搜索关键字（姓名或手机号）：").strip().lower()
    if not keyword:
        print("搜索关键字不能为空"); return

    # 【list】收集匹配结果
    results: list[tuple] = []

    for name, info in contacts.items():            # 【dict】遍历
        if keyword in name.lower():                # 【string-methods】lower 忽略大小写
            results.append((name, info["手机"], info["邮箱"], info["地址"]))
        elif keyword in info["手机"]:              # 按手机号匹配
            results.append((name, info["手机"], info["邮箱"], info["地址"]))

    if not results:
        print(f"未找到与「{keyword}」相关的联系人。")
        return

    # 【slice】如果结果很多，取前N个
    display = results[:SEARCH_DISPLAY_MAX]          # 切片限制展示数量
    print(f"\n找到 {len(results)} 条结果" +
          (f"（仅显示前{SEARCH_DISPLAY_MAX}条）" if len(results) > SEARCH_DISPLAY_MAX else "") + "：")
    for i, (name, phone, email, addr) in enumerate(display, 1):
        print(f"  {i}. {name} | {mask_phone(phone)} | {email} | {addr}")


def modify_contact():
    """修改联系人 —— dict更新 + set同步 + string-methods校验"""
    name = input("\n要修改的联系人姓名：").strip().title()   # 【string-methods】title
    if name not in contacts:                        # 【dict】key 检查
        print(f"「{name}」不存在。"); return

    info = contacts[name]                           # 【dict】取值（拿到引用）
    print(f"当前信息：{info['手机']} | {info['邮箱']} | {info['地址']}")
    print("留空则保持原值，输入「-」则清空该项")

    # 修改手机号
    new_phone = input(f"手机号 [{info['手机']}]：").strip()
    if new_phone and new_phone != '-':
        if new_phone == info["手机"]:               # 和旧号相同，无需修改
            print("手机号未变化")
        else:
            ok, result = validate_phone(new_phone, exclude_phone=info["手机"])
            if not ok:
                print(f"[错误] {result}，手机号未修改")
            else:
                phone_set.discard(info["手机"])      # 【set】移除旧号
                info["手机"] = result
                phone_set.add(result)               # 【set】加入新号

    # 修改邮箱
    new_email = input(f"邮箱 [{info['邮箱']}]：").strip()
    if new_email:
        info["邮箱"] = "" if new_email == '-' else new_email

    # 修改地址
    new_addr = input(f"地址 [{info['地址']}]：").strip()
    if new_addr:
        info["地址"] = "" if new_addr == '-' else new_addr

    history.append(("修改", name, info["手机"], datetime.datetime.now().strftime("%m-%d %H:%M")))
    print(f"✅ 已更新：{name}")


def delete_contact():
    """删除联系人 —— dict删 + set同步 + list回收站（选做）"""
    name = input("\n要删除的联系人姓名：").strip().title()
    if name not in contacts:
        print(f"「{name}」不存在。"); return

    info = contacts[name]
    ans = input(f"确认删除「{name}」({mask_phone(info['手机'])})？(y/n)：")
    if ans.lower() != 'y':
        print("已取消"); return

    phone_set.discard(info["手机"])                  # 【set】移除手机号
    del contacts[name]                               # 【dict】删除键值对
    history.append(("删除", name, info["手机"], datetime.datetime.now().strftime("%m-%d %H:%M")))
    print(f"✅ 已删除：{name}")


def export_contacts():
    """导出通讯录 —— dict遍历 + list排序 + tuple + slice"""

    # 【list + tuple】构建联系人快照列表
    snapshots: list[tuple] = [
        (name, info["手机"], info["邮箱"], info["地址"])
        for name, info in contacts.items()           # 【dict】遍历
    ]

    # 【list】按姓名排序
    snapshots.sort(key=lambda x: x[0])               # sort + key 参数

    print("\n--- 导出（按姓名排序）---")
    for s in snapshots:
        # s[0]=姓名 s[1]=手机 s[2]=邮箱 s[3]=地址  【tuple索引】
        print(f"  {s[0]} | {mask_phone(s[1])} | {s[2]} | {s[3]}")

    print(f"\n共 {len(snapshots)} 位联系人")


def show_history():
    """查看操作日志 —— list遍历 + tuple解包"""
    if not history:
        print("\n暂无操作记录。"); return

    # 【slice】取最近N条
    recent = history[-HISTORY_DISPLAY_MAX:]          # 负数索引切片
    print(f"\n--- 最近操作记录（共{len(history)}条）---")
    for i, (action, name, phone, ts) in enumerate(reversed(recent), 1):
        # 【tuple】解包
        print(f"  {i}. [{action}] {name}  {mask_phone(phone)}  {ts}")


# ============================================================
# 主循环
# ============================================================

def main():
    """通讯录主入口 —— 命令字典 + 异常保护 + 持久化"""
    load_data()  # 启动时加载存档

    # 【dict】命令字典 —— 替代冗长的 if-elif 分支
    commands: dict[str, tuple] = {
        "1": (add_contact,    "新增"),
        "2": (view_contacts,  "查看"),
        "3": (search_contacts, "搜索"),
        "4": (modify_contact, "修改"),
        "5": (delete_contact, "删除"),
        "6": (export_contacts, "导出"),
        "7": (show_history,   "日志"),
    }

    menu = """
┌──────────────────────────────┐
│        📱 手机通讯录           │
├──────────────────────────────┤
│  1. 新增   2. 查看   3. 搜索  │
│  4. 修改   5. 删除   6. 导出  │
│  7. 日志   0. 退出            │
└──────────────────────────────┘
> """
    try:
        while True:
            cmd = input(menu).strip()
            if cmd == '0':
                break
            if cmd in commands:
                commands[cmd][0]()  # 调取元组第一个元素（函数引用）
            else:
                print("无效选项，请重试")
    except (KeyboardInterrupt, EOFError):
        print("\n\n操作已取消")
    finally:
        save_data()  # 无论如何退出都保存
        print(f"通讯录共有 {len(contacts)} 位联系人，再见！")


if __name__ == "__main__":
    main()
