from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML endpoint
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("api.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

if __name__ == "__main__":
    # Use '0.0.0.0' to listen on all available network interfaces
    uvicorn.run(
        app,
        host="91.102.161.166",  # Change this to '0.0.0.0'
        port=5645,
        log_level="debug"
    )