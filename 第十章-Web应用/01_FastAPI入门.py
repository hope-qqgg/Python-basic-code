from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()

# 定义API接口 ---> 改函数的返回值表示API接口的返回数据，接口访问路径为/，请求方式为GET
@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/users")
def get_users():
    return [
        {"id":1,"name":"张三"},
        {"id":2,"name":"李四"},
        {"id":3,"name":"王五"}
    ]

# 启动服务 ---> uvicorn：Python中的轻量级Web服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)

"""
    在终端启动服务：
        1.fastapi dev "01_FastAPI入门.py"  
        2.uvicorn 01_FastAPI入门:app --reload
"""