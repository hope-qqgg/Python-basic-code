# GET /materials（支持 keyword）、GET /materials/{mid}（404）、POST /materials（201）、DELETE /materials/{mid}（404）。
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Material(BaseModel):
    name:str
    stock:int

class MaterialOut(BaseModel):
    id: int
    name: str
    stock: int

materials = [
    {"id":1,"name":"钳子","stock":3},
    {"id":2,"name":"卷尺","stock":2},
    {"id":3,"name":"六角扳手","stock":5}
]
next_id = 4

@app.get("/")
def get_hello():
    return "Hello World"

@app.get("/material",response_model=list[MaterialOut])
def get_material():
    return materials

@app.get("/material/search")
def search_material(keyword:str = "", page:int = 1, size:int = 10):
    result = [b for b in materials if keyword in b["name"]]
    start = (page - 1) * size
    return {"keyword": keyword, "total": len(result), "data": result[start:start + size]}

@app.post("/material/add",response_model=MaterialOut,status_code=201)
def add_material(material: Material):
    global next_id
    item = {"id": next_id, **material.model_dump()}
    materials.append(item)
    next_id += 1
    return item

@app.get("/material/{material_id}", response_model=MaterialOut)
def get_material_by_id(material_id: int):
    for b in materials:
        if b["id"] == material_id:
            return b
    raise HTTPException(status_code=404, detail=f"没有 id={material_id} 的工具")

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)