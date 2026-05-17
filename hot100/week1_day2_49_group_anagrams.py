"""
49. 字母异位词分组 (Group Anagrams)

====================================================
Step 1 — 解题思路
====================================================

问题：给一堆字符串，把"字母组成相同"的分到一组。
  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
  输出: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

核心技巧：排序 → 哈希分组
  1. 对每个单词，把字母排序 → 得到标准形式（归一化key）
  2. 用字典 dict[key] = [word1, word2, ...]
  3. 最后把字典的所有 values 转成列表返回

  例子：
    "eat" 排序 → "aet"  → {"aet": ["eat"]}
    "tea" 排序 → "aet"  → {"aet": ["eat", "tea"]}
    "tan" 排序 → "ant"  → {"aet": [...], "ant": ["tan"]}
    ...

时间复杂度：O(n × k log k)，n=单词数，k=最长单词长度
空间复杂度：O(n × k)

====================================================
Step 2 — 带标注的代码（跟着读一遍）
====================================================
"""


def group_anagrams_1(strs: list[str]) -> list[list[str]]:
    """方法1：排序法 — 最简单直观"""
    # ① 创建一个空字典，key=排序后的字符串，value=原始单词列表
    groups: dict[str, list[str]] = {}

    for word in strs:                          # ② 遍历每个单词
        # ③ sorted(word) 返回 ['a','e','t']，需要 ''.join 拼回 "aet"
        key = "".join(sorted(word))            # ④ 归一化：排序后拼成字符串
        if key not in groups:                  # ⑤ 这个key第一次出现？
            groups[key] = []                   # ⑥ 初始化空列表
        groups[key].append(word)               # ⑦ 把原始单词加入对应组

    return list(groups.values())               # ⑧ 返回所有分组


# ============================================
# Step 3 — 一行行看图说话
# ============================================

"""
① groups: dict[str, list[str]] = {}
   ┌─────────────────────────────────────────────┐
   │ 字典结构示意：                                │
   │   "aet" → ["eat", "tea", "ate"]              │
   │   "ant" → ["tan", "nat"]                     │
   │   "abt" → ["bat"]                            │
   │ key是排序后的字符串，value是原始单词组成的list  │
   └─────────────────────────────────────────────┘

② for word in strs:
   逐个处理："eat" → "tea" → "tan" → "ate" → "nat" → "bat"

③ sorted("eat") → ['a', 'e', 't']
   注意！sorted 返回的是 list，不是字符串
   所以需要 ''.join(...) 把字母拼回去

④ key = "".join(sorted(word))
   拆解这个表达式（从内向外读）：
     sorted("eat")           → ['a', 'e', 't']     ← 排序
     "".join(['a','e','t'])  → "aet"               ← 拼合
   所以 key 最终是 "aet"

⑤ if key not in groups:
   如果 "aet" 还没在字典里 → 初始化一个空列表

⑦ groups[key].append(word)
   把原始单词（"eat"）加入列表
   Python 中 dict[key] 返回对应的列表，直接 .append() 即可
"""


# ============================================
# Step 4 — 另一种写法：defaultdict（更Pythonic）
# ============================================

from collections import defaultdict

def group_anagrams_2(strs: list[str]) -> list[list[str]]:
    """方法2：用defaultdict避免隐式检查"""
    groups = defaultdict(list)    # ① 访问不存在的key时自动创建空list

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)  # ② 不需要 if key not in ... 了

    return list(groups.values())


"""
defaultdict 原理：
  groups = defaultdict(list)
  等价于：每次访问 groups[不存在的key] 时，自动执行 groups[key] = list()
  所以不用手动判断 key 存不存在
"""


# ============================================
# Step 5 — 破坏实验区（动手改一改）
# ============================================

if __name__ == "__main__":
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("=== 方法1：普通字典 ===")
    result1 = group_anagrams_1(test)
    print(result1)

    print("\n=== 方法2：defaultdict ===")
    result2 = group_anagrams_2(test)
    print(result2)

    # ┌──────────────────────────────────────────────┐
    # │ TODO-1: 破坏实验                              │
    # │ 把 sorted(word) 改成 sorted(word, reverse=True)│
    # │ 结果会变吗？为什么不会？                       │
    # └──────────────────────────────────────────────┘

    # ┌──────────────────────────────────────────────┐
    # │ TODO-2: 验证理解                              │
    # │ 在下面写一个函数 is_anagram(s1, s2)，          │
    # │ 判断两个字符串是否是异位词。                    │
    # │ 提示：直接复用 sorted 的思路                   │
    # └──────────────────────────────────────────────┘
