# 01_uv/uv_example.py

# UV is a super-fast ASGI server in Python, inspired by Node.js’ uvicorn.

from starlette.applications import Starlette
from starlette.responses import Response

application = Starlette()

@application.route('/')
async def homepage(request):
    return Response(status_code=200, content=b'Hello from uv!')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("uv_example:application", host="127.0.0.1", port=8000, reload=True)
