---
aliases:
  - 07-pydantic
---
# 07 — Pydantic 数据校验

> 相关笔记：[类型转换与格式化](../19-type-conversion/theory_19_type_conversion.md) · [类型提示进阶/DI](../08-typing-di/theory_08_typing_di.md)

## 一句话

Pydantic = Java 的 DTO + `@Valid` 合体。定义一个模型类，传入的数据自动校验，不对就报错。

## 1. BaseModel：定义数据模型

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

# 传合法的数据 → 自动创建对象
p = Product(id=1, name="鼠标", price=99.9)
print(p)  # id=1 name='鼠标' price=99.9

# 传非法数据 → 自动报错
# Product(id="abc", name="鼠标", price=99.9)  # 类型错误！
```

## 2. Field：加约束

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str = Field(min_length=1)           # 至少1字符
    price: float = Field(gt=0)                 # 必须大于0
    stock: int = Field(ge=0, default=0)        # >=0，默认0
    category: str = "未分类"                   # 有默认值就是可选
```

对照 Java：
```java
public class ProductDTO {
    @NotNull @NotBlank
    private String name;
    
    @DecimalMin("0.01")
    private double price;
}
```

## 3. 序列化：模型 ↔ 字典/JSON

```python
p = Product(id=1, name="鼠标", price=99.9)

# 转字典
print(p.model_dump())        # {'id': 1, 'name': '鼠标', 'price': 99.9}

# 转 JSON 字符串
print(p.model_dump_json())   # {"id": 1, "name": "鼠标", "price": 99.9}

# 从字典创建
data = {"id": 2, "name": "键盘", "price": 299.0}
p2 = Product(**data)         # 解包字典传参
```

## 4. 嵌套模型

```python
class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str
    category: Category        # 嵌套另一个模型

p = Product(id=1, name="鼠标", category={"id": 1, "name": "外设"})
print(p)  # 自动把 dict 转成 Category 对象
```

## 5. FastAPI 中的应用（预告）

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int = Field(ge=18)

@app.post("/employees")
def create_emp(emp: Employee):   # FastAPI 自动用 Pydantic 校验
    return emp                    # 返回 Pydantic 模型 = 自动 JSON
```

## 对照 Java

| Java | Pydantic |
|------|----------|
| `@NotBlank` | `Field(min_length=1)` |
| `@Min(0)` | `Field(ge=0)` |
| `@Max(100)` | `Field(le=100)` |
| `@Pattern(regexp="...")` | `Field(pattern=r"...")` |
| `@Valid` 嵌套 | 直接写子模型类型 |
| DTO → JSON | `model_dump_json()` |
