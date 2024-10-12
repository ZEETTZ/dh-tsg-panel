from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 定义版本信息和下载地址
version_info = {
    "version": "1.0.0",
    "download_url": "https://example.com/download"
}

@app.get("/version")
async def get_version():
    """
    返回当前应用的版本号和下载地址。
    """
    return version_info

if __name__ == "__main__":
    # 配置Uvicorn并启动应用
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)