"""
Day 4 练习：Function Call
完成后运行：python practice_04.py

目标：理解函数定义、参数生成、调用流程
"""
import sys
import os
import json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


# ============================================================
# 第一组：定义一个天气查询工具
# ============================================================

# TODO 1：补全 tools 定义
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名"
                    },
                    # TODO: 加一个 date 参数
                },
                # TODO: 标记 required
            }
        }
    }
]

# 测试：让 LLM 选择函数
test_messages = [
    {"role": "user", "content": "北京明天天气怎么样？"}
]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=test_messages,
    tools=tools,
    tool_choice="auto",
)

print("=" * 50)
print("函数调用结果")
print("=" * 50)

msg = response.choices[0].message
if msg.tool_calls:
    for tc in msg.tool_calls:
        func = tc.function
        print(f"选择的函数：{func.name}")
        print(f"生成的参数：{func.arguments}")
else:
    print("模型没有调用函数")
    print(f"直接回答：{msg.content}")


# ============================================================
# 第二组：理解 Function Call 的完整流程
# ============================================================

# 模拟函数执行
def execute_function(name: str, args: dict) -> str:
    """模拟执行函数并返回结果"""
    if name == "get_weather":
        return json.dumps({
            "city": args.get("city"),
            "temperature": 26,
            "weather": "晴",
            "humidity": "45%"
        })
    return json.dumps({"error": "unknown function"})


# 完整的 Function Call 流程
print("\n" + "=" * 50)
print("完整 Function Call 流程")
print("=" * 50)

# Step 1: 用户提问
user_input = "北京明天天气怎么样？适合出去玩吗？"
messages = [{"role": "user", "content": user_input}]
print(f"用户：{user_input}")

# Step 2: LLM 选择函数
resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

msg = resp.choices[0].message
if msg.tool_calls:
    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        print(f"LLM 选择：{tc.function.name}({args})")

        # Step 3: 执行函数
        result = execute_function(tc.function.name, args)
        print(f"函数返回：{result}")

        # Step 4: 把结果给 LLM 组织回答
        messages.append(msg)
        messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": result,
        })

        final = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
        )
        print(f"最终回答：{final.choices[0].message.content}")


print("\n✅ Day 4 练习完成！")
print("Function Call 三要素：定义函数 → 模型选函数 → 程序执行")
