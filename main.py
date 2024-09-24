from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import subprocess

app = FastAPI()

# 定义数据模型
class UserCredentials(BaseModel):
    userid: str
    password: str

# 检测一下是否安装完毕
@app.post("/start")
async def start(user_data: UserCredentials):

    file_exists = os.path.isfile('DreadHungerServer.exe')
    
    # 返回值
    code = 0 if file_exists else 1
    message = f""
    if file_exists:
        message += ", DreadHungerServer.exe 存在"
    else:
        message += ", DreadHungerServer.exe 不存在"
    
    return {"code": code, "message": message}

# 启动服务器并附带参数
@app.post("/create")
async def create(user_data: UserCredentials):
    file_exists = os.path.isfile('DreadHungerServer.exe')
    if not file_exists:
        return {"code": 1, "message": f"DreadHungerServer.exe 不存在"}

    command = ['DreadHungerServer.exe', '-port','-log']
    
    try:
        # 启动
        subprocess.Popen(command)
        return {"code": 0, "message": f"成功启动"}
    except Exception as e:
        return {"code": 1, "message": f"启动失败: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)