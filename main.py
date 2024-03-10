# main.py
from fastapi import FastAPI
import uvicorn
from app import router  # Importing router from app.py

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",  # Endpoint for OpenAPI schema
    docs_url="/api/v1/docs",  # Endpoint for Swagger UI
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
