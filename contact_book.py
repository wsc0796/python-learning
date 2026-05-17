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
import sys, io, json, datetime, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============================================================
# 数据层
# ============================================================

contacts: dict[str, dict] = {}
phone_set: set[str] = set()
history: list[tuple] = []

PAGE_SIZE = 3
SEARCH_DISPLAY_MAX = 5
HISTORY_DISPLAY_MAX = 10

# 【改进1】数据文件路径固定在脚本所在目录，防止从其他目录运行时创建/读取错误位置
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "contacts.json")


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
    name = name.strip()
    if not name:
        return False, "姓名不能为空"
    if name.isdigit():
        return False, "姓名不能是纯数字"

    # 【改进2】折叠连续空格，"张  三" → "张三"，避免存储多余空格
    name = " ".join(name.split())

    if not name.replace(" ", "").isalpha():
        return False, "姓名不能包含数字或特殊符号"
    if len(name) > 20:
        return False, "姓名太长（最多20字）"
    return True, name.title()


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
    if phone != exclude_phone and phone in phone_set:
        return False, "该手机号已被其他联系人使用"
    return True, phone


def validate_email(email: str) -> tuple[bool, str]:
    """【新增】校验邮箱格式。

    参数:
        email: 原始输入的邮箱

    返回:
        (是否通过, 处理后的邮箱或错误提示)
    """
    email = email.strip()
    if not email:
        return True, ""  # 可选字段，留空通过
    # 简单校验：包含 @，且 @ 后面有 .
    if "@" not in email:
        return False, "邮箱格式无效（缺少 @）"
    if "." not in email.split("@")[-1]:
        return False, "邮箱格式无效（@ 后面需要域名，如 .com）"
    return True, email


def mask_phone(phone: str) -> str:
    """手机号脱敏，中间4位替换为星号。

    参数:
        phone: 11位手机号

    返回:
        脱敏后的字符串，如 138****8000
    """
    return phone[:3] + "****" + phone[7:]


def paginate(items: list, page: int) -> list:
    """用切片取当前页数据，自动处理末页越界。

    参数:
        items: 完整列表
        page: 页码（从1开始）

    返回:
        当前页的元素列表
    """
    start = (page - 1) * PAGE_SIZE
    return items[start:start + PAGE_SIZE]


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
        phone_set = {info["手机"] for info in contacts.values()
                     if isinstance(info.get("手机"), str)}
        print(f"[已加载 {len(contacts)} 位联系人]")
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("[警告] 存档文件损坏，将使用空通讯录")


def save_data() -> None:
    """退出时保存通讯录到JSON文件"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"contacts": contacts}, f, ensure_ascii=False, indent=2)
        print("[通讯录已保存]")
    except Exception as e:
        print(f"[保存失败] {e}")


# ============================================================
# 业务功能
# ============================================================

def add_contact():
    """新增联系人"""
    print("\n--- 新增联系人 ---")

    name_raw = input("姓名：")
    ok, name = validate_name(name_raw)
    if not ok:
        print(f"[错误] {name}")
        return

    old_phone = contacts.get(name, {}).get("手机")
    if name in contacts:
        ans = input(f"「{name}」已存在，是否覆盖？(y/n)：")
        if ans.lower() != 'y':
            print("已取消")
            return

    phone_raw = input("手机号：")
    ok, phone = validate_phone(phone_raw, exclude_phone=old_phone)
    if not ok:
        print(f"[错误] {phone}")
        return

    email_raw = input("邮箱（可留空）：")
    ok, email = validate_email(email_raw)
    if not ok:
        print(f"[错误] {email}")
        return

    address = input("地址（可留空）：").strip()

    # 【改进3】校验全部通过后再操作集合和存储
    if old_phone and old_phone != phone:
        phone_set.discard(old_phone)
    if old_phone != phone or name not in contacts:
        phone_set.add(phone)

    contacts[name] = {
        "手机": phone,
        "邮箱": email,
        "地址": address,
    }

    history.append(("新增", name, phone,
                    datetime.datetime.now().strftime("%m-%d %H:%M")))
    print(f"✅ 已添加：{name}  {mask_phone(phone)}")


def view_contacts():
    """查看联系人"""
    if not contacts:
        print("\n通讯录为空。")
        return

    contact_list = list(contacts.items())
    total_pages = (len(contact_list) + PAGE_SIZE - 1) // PAGE_SIZE
    page = 1
    while True:
        print(f"\n--- 通讯录  第{page}/{total_pages}页 ---")
        page_items = paginate(contact_list, page)

        for name, info in page_items:
            snapshot = (name, info["手机"], info.get("邮箱", ""))
            print(f"  {snapshot[0]}  {mask_phone(snapshot[1])}  {snapshot[2]}")

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
    """搜索联系人"""
    keyword = input("\n输入搜索关键字（姓名或手机号）：").strip().lower()
    if not keyword:
        print("搜索关键字不能为空")
        return

    results: list[tuple] = []

    for name, info in contacts.items():
        if keyword in name.lower():
            results.append((name, info["手机"], info.get("邮箱", ""), info.get("地址", "")))
        elif keyword in info["手机"]:
            results.append((name, info["手机"], info.get("邮箱", ""), info.get("地址", "")))

    if not results:
        print(f"未找到与「{keyword}」相关的联系人。")
        return

    display = results[:SEARCH_DISPLAY_MAX]
    print(f"\n找到 {len(results)} 条结果" +
          (f"（仅显示前{SEARCH_DISPLAY_MAX}条）" if len(results) > SEARCH_DISPLAY_MAX else "") + "：")
    for i, (name, phone, email, addr) in enumerate(display, 1):
        print(f"  {i}. {name} | {mask_phone(phone)} | {email} | {addr}")


def modify_contact():
    """修改联系人"""
    name = input("\n要修改的联系人姓名：").strip().title()
    if name not in contacts:
        print(f"「{name}」不存在。")
        return

    info = contacts[name]
    print(f"当前信息：{info['手机']} | {info.get('邮箱', '')} | {info.get('地址', '')}")
    print("留空则保持原值，输入「-」则清空该项")

    # 修改手机号
    new_phone = input(f"手机号 [{info['手机']}]：").strip()
    if new_phone and new_phone != '-':
        if new_phone == info["手机"]:
            print("手机号未变化")
        else:
            ok, result = validate_phone(new_phone, exclude_phone=info["手机"])
            if not ok:
                print(f"[错误] {result}，手机号未修改")
            else:
                phone_set.discard(info["手机"])
                info["手机"] = result
                phone_set.add(result)
    elif new_phone == '-':
        print("手机号不支持清空，保持原值")

    # 修改邮箱
    new_email = input(f"邮箱 [{info.get('邮箱', '')}]：").strip()
    if new_email:
        if new_email == '-':
            info["邮箱"] = ""
        else:
            # 【新增】修改时也校验邮箱
            ok, result = validate_email(new_email)
            if not ok:
                print(f"[错误] {result}，邮箱未修改")
            else:
                info["邮箱"] = result
                print("邮箱已更新")

    # 修改地址
    new_addr = input(f"地址 [{info.get('地址', '')}]：").strip()
    if new_addr:
        info["地址"] = "" if new_addr == '-' else new_addr

    history.append(("修改", name, info["手机"],
                    datetime.datetime.now().strftime("%m-%d %H:%M")))
    print(f"✅ 已更新：{name}")


def delete_contact():
    """删除联系人"""
    name = input("\n要删除的联系人姓名：").strip().title()
    if name not in contacts:
        print(f"「{name}」不存在。")
        return

    info = contacts[name]
    ans = input(f"确认删除「{name}」({mask_phone(info['手机'])})？(y/n)：")
    if ans.lower() != 'y':
        print("已取消")
        return

    phone_set.discard(info["手机"])
    del contacts[name]
    history.append(("删除", name, info["手机"],
                    datetime.datetime.now().strftime("%m-%d %H:%M")))
    print(f"✅ 已删除：{name}")


def export_contacts():
    """导出通讯录"""

    snapshots: list[tuple] = [
        (name, info["手机"], info.get("邮箱", ""), info.get("地址", ""))
        for name, info in contacts.items()
    ]
    snapshots.sort(key=lambda x: x[0])

    print("\n--- 导出（按姓名排序）---")
    for s in snapshots:
        print(f"  {s[0]} | {mask_phone(s[1])} | {s[2]} | {s[3]}")
    print(f"\n共 {len(snapshots)} 位联系人")


def show_history():
    """查看操作日志"""
    if not history:
        print("\n暂无操作记录。")
        return

    recent = history[-HISTORY_DISPLAY_MAX:]
    print(f"\n--- 最近操作记录（共{len(history)}条）---")
    for i, (action, name, phone, ts) in enumerate(reversed(recent), 1):
        print(f"  {i}. [{action}] {name}  {mask_phone(phone)}  {ts}")


# ============================================================
# 主循环
# ============================================================

def main():
    """通讯录主入口"""
    load_data()

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
                commands[cmd][0]()
            else:
                print("无效选项，请重试")
    except (KeyboardInterrupt, EOFError):
        print("\n\n操作已取消")
    finally:
        save_data()
        print(f"通讯录共有 {len(contacts)} 位联系人，再见！")


if __name__ == "__main__":
    main()
