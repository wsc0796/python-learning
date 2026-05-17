# FastAPI → Spring Boot 对照表

## 路由

| Spring Boot | FastAPI |
|------------|---------|
| `@RestController` | `app = FastAPI()` |
| `@RequestMapping("/api")` | `app = FastAPI(root_path="/api")` |
| `@GetMapping("/employees")` | `@app.get("/employees")` |
| `@PostMapping("/employees")` | `@app.post("/employees")` |
| `@PathVariable Long id` | `id: int` |
| `@RequestParam String name` | `name: str` |
| `@RequestBody EmployeeDTO dto` | `dto: EmployeeDTO` |

## 数据校验

| Spring Boot | FastAPI |
|------------|---------|
| DTO 类 + `@Valid` + `@NotBlank` | Pydantic `BaseModel` + `Field(min_length=1)` |
| `@JsonProperty("user_name")` | `Field(alias="user_name")` |
| `ResponseEntity<Result<Employee>>` | 直接返回 dict / Pydantic 模型 |
| `@ExceptionHandler` | `@app.exception_handler` |

## 依赖注入

| Spring Boot | FastAPI |
|------------|---------|
| `@Autowired` | `Depends()` |
| `@Component` / `@Service` | 普通函数 + `def get_db() -> Session` |
| `@Scope("request")` | `Depends()` 默认就是请求级别的 |

## 对比示例：员工查询

**Spring Boot：**
```java
@RestController
@RequestMapping("/api/employees")
public class EmployeeController {
    @Autowired
    private EmployeeService employeeService;

    @GetMapping("/{id}")
    public ResponseEntity<Result<EmployeeVO>> getById(@PathVariable Long id) {
        EmployeeVO vo = employeeService.getById(id);
        return ResponseEntity.ok(Result.success(vo));
    }
}
```

**FastAPI：**
```python
@app.get("/api/employees/{id}")
def get_employee(id: int, service: EmployeeService = Depends()):
    vo = service.get_by_id(id)
    return {"code": 200, "data": vo}
```

FastAPI 省掉了 5 行样板代码（`@Autowired`、`ResponseEntity`、`@PathVariable` 等）。
