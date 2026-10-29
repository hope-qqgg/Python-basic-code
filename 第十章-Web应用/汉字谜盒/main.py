# 基础环境搭建
from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 挂载静态文件的存放目录
app.mount("/static", StaticFiles(directory="static"), name="static")
# 任何以/static开头的路径都会交到这里处理

# 定义路径操作函数 ---> http://127.0.0.1:8000/
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)