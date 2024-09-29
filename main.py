from fastapi import FastAPI

app = FastAPI()

# 1. GET route for greeting
@app.get("/hello")
async def read_hello():
    return {"message": "Hello, You are a Nigesh...."}

# 2. GET route to fetch an item by its ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# To run this FastAPI app:
# Install FastAPI and Uvicorn if you haven't: pip install fastapi uvicorn
# Run the app using the command: uvicorn <filename>:app --reload
