# - One of the fastest python framework, leveraging async programming to handle multiple request at a time.
# Starlette and Pydantic Based: Uses Starlette for web features (routing, middleware, WebSockets) and Pydantic for type-based validation and parsing.   
# Auto API Docs: Generates interactive documentation (Swagger UI, ReDoc) automatically for easy testing.
# Async-First Design: Built around async/await for high concurrency, suitable for real-time and scalable applications.


# Installation for FastAPIs

# step 1:
# pip instal fastapi

# step 2:
# FastAPI needs and ASGI server to run. The most common recommended one is UVICORN.
# pip install "uvicorn[standard]"

# step 3:
# First FastAPI App:

from fastapi import FastAPI

# creating FastAPI app instance
app = FastAPI()

# simple get API.
@app.get("/")
def read_root():
    return{"hello, I'm FastAPI"}