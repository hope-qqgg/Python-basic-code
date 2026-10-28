from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Book(BaseModel):
    title:str
    author:str
    price:float = 0.0

class BookOut(BaseModel):      
    id: int
    title: str
    author: str

books = [{"id": 1, "title": "Python编程", "author": "张三", "price": 59.9}]
next_id = 2

@app.get("/book",response_model=list[BookOut])
def list_books():
    return books

@app.post("/book",response_model=list[BookOut],status_code=201)
def add_book(book: Book):
    global next_id
    item = {"id": next_id, **book.model_dump()}
    books.append(item)
    next_id += 1
    return item


@app.get("/book/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int):
    for b in books:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail=f"没有 id={book_id} 的书")

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)