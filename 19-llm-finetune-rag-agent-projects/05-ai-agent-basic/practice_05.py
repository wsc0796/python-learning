"""
Day 5 练习：AI Agent 基础
完成后运行：python practice_05.py

目标：实现一个简版 ReAct Agent
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
# 第一组：定义 Agent 的工具
# ============================================================

# TODO 1：补全工具定义
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市"},
                    "date": {"type": "string", "description": "日期"},
                },
                "required": ["city", "date"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "数学计算",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "数学表达式"},
                },
                "required": ["expression"],
            }
        }
    },
    # TODO 2：加一个 search_pois 工具
    # 用于搜索指定城市的景点
]


# ============================================================
# 第二组：实现 Agent 工具执行
# ============================================================

def execute_tool(name: str, args: dict) -> str:
    """执行工具并返回结果"""
    if name == "get_weather":
        return json.dumps({
            "city": args["city"],
            "date": args["date"],
            "weather": "晴",
            "temperature": 25,
        })
    elif name == "calculate":
        try:
            # 注意：eval 不安全，这里仅用于演示
            result = eval(args["expression"])
            return json.dumps({"result": result})
        except Exception as e:
            return json.dumps({"error": str(e)})
    # TODO 3：处理 search_pois 的调用
    return json.dumps({"error": "unknown tool"})


# ============================================================
# 第三组：运行 Agent
# ============================================================

def run_agent(task: str, max_steps: int = 5) -> str:
    """简版 ReAct Agent"""
    messages = [{"role": "user", "content": task}]
    print(f"\n任务：{task}")

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                func = tc.function
                args = json.loads(func.arguments)
                print(f"  第{step+1}步：调 {func.name}({args})")

                result = execute_tool(func.name, args)
                print(f"  结果：{result[:80]}...")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                })
        else:
            return msg.content

    return "达到最大步数"


# 测试
task1 = "北京明天天气怎么样？顺便算一下 25×4+100 等于多少？"
result1 = run_agent(task1)
print(f"\n最终回答：{result1}")

# TODO 4：设计一个更复杂的任务，测试多步骤推理
# task2 = "..."

print("\n✅ Day 5 练习完成！")
print("ReAct 就是：推理 → 行动 → 观察 → 再推理 → 再行动...")
