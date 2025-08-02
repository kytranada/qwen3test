PREDEFINED_PROMPTS = {
    "Function + Edge Cases": """Write a Python function called `calculate_discounted_price` that:
- Accepts original price, discount %, and tax rate
- Applies discount, then tax, and returns final price
Also return test cases for edge conditions:
- 0% discount, 0% tax
- 100% discount
- Negative price
""",

"Multi-step Code Reasoning": """I have a CSV file containing product inventory like this:

product_id,name,stock,cost
1,Widget,3,12.99
2,Gadget,0,9.99
3,Doohickey,8,14.99

Write a Python script that:
- Reads the CSV
- Filters for items with stock = 0
- Logs those items to a separate file
- Sends a Slack message if any item is out of stock
""",

    "Debug Code + Explain": """The following function has a bug. Fix it and explain what went wrong:
```python
def is_palindrome(word):
    return word == word.reverse()
```""",

    "FastAPI Middleware Review": """I’ve written this API using FastAPI. Please:
1. Describe what each route does
2. Identify any inefficiencies
3. Suggest improvements

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"Request took {duration} seconds")
    return response

@app.get("/")
def read_root():
    return {"msg": "Hello!"}

@app.get("/health")
def health_check():
    return "OK"
```"""
}
