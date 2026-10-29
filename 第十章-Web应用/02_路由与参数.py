from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python编程", "author": "张三"},
    {"id": 2, "title": "数据库原理", "author": "李四"},
    {"id": 3, "title": "计算机网络", "author": "王五"},
    {"id": 4, "title": "网络安全", "author": "赵六"},
    {"id": 5, "title": "Python编程", "author": "张三"},
    {"id": 6, "title": "Python编程", "author": "张三"},
    {"id": 7, "title": "Python编程", "author": "张三"},
    {"id": 8, "title": "数据库原理", "author": "李四"},
    {"id": 9, "title": "数据库原理", "author": "李四"},
    {"id": 10, "title": "计算机网络", "author": "王五"},
    {"id": 11, "title": "网络安全", "author": "赵六"},
    {"id": 12, "title": "网络安全", "author": "赵六"},
    {"id": 13, "title": "网络安全", "author": "赵六"},
]

# 查询所有图书
@app.get("/books")
def get_books():
    return books

# 搜索指定图书
@app.get("/book/search")
def get_books(title = "", author = "", page:int = 1, size:int = 10):
    """
    搜索指定图书(不传入参数就是所有书)
    :param title: 书名
    :param author: 作者
    :param page: 页数
    :param size: 每页展示几本书
    :return: 书名；作者；符合搜索条件书本的数量；符合搜索条件书本
    """
    result = [b for b in books if title in b["title"] and author in b["author"]]
    start = (page - 1) * size
    return {"title": title, "author": author, "total": len(result), "data": result[start:start + size]}

# 通过id查询指定书籍
@app.get("/book/{book_id}")
def get_book(book_id:int):
    for b in books:
        if b["id"] == book_id:
            return b
    return {"message": f"没有 id = {book_id} 的书"}

# 🔴🔴 本文件最重要的一条：这段必须写在下面 /book/{book_id} 的「前面」！
#
#    FastAPI 是按「从上往下」的顺序去匹配路由的。
#    你把这两段调换位置，访问 /book/search 时，"search" 会先被
#    /book/{book_id} 抓走，然后框架试着把 "search" 转成 int，转不动，回 422。
#    实测原话长这样：
#      {"detail":[{"type":"int_parsing","loc":["path","book_id"],
#        "msg":"Input should be a valid integer, unable to parse string as an integer",
#        "input":"search"}]}
#
#    口诀：越「具体」的网址，越要排在越前面。

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
