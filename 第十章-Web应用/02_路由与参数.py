from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python编程", "author": "张三"},
    {"id": 2, "title": "数据库原理", "author": "李四"},
    {"id": 3, "title": "计算机网络", "author": "王五"},
    {"id": 4, "title": "网络安全", "author": "赵六"},
]

@app.get("/book")
def get_book():
    return books

@app.get("/book/search")
def search_book(keyword:str = "",author:str = "", page:int = 1, size:int = 10):
    result = [b for b in books if keyword in b["title"] and author in b["author"]]
    start = (page - 1) * size
    return {"keyword": keyword, "author": author, "total": len(result), "data": result[start:start + size]}

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for b in books:
        if b["id"] == book_id:
            return b
    return {"message": f"没有 id={book_id} 的书"}

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
