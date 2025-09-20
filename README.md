# TSG海杀网页管理面板

一个基于 Flask 的网页管理面板，用于管理游戏服务器。

## 功能特性

- 通过网页界面管理游戏服务器配置
- 启动/停止游戏服务器进程
- 实时查看服务器日志
- 黑名单管理
- 监控服务器状态
- 用户认证和登录保护

## 技术栈

- 后端: Python + Flask
- 前端: HTML + CSS + JavaScript + jQuery
- 依赖库: 
  - flask
  - flask_session
  - requests
  - psutil

## 安装说明

1. 克隆或下载本项目
2. 安装依赖:
```bash
pip install flask flask_session requests psutil
```
3. 运行应用:
```bash
python DhApi.py
```
4. 在浏览器中访问 `http://localhost:5000` (默认端口)

## 使用说明

1. 首次访问需要设置登录密码
2. 登录后可以修改服务器配置参数
3. 可以启动/停止游戏服务器
4. 查看实时日志和玩家信息

## 许可证

本项目采用 MIT 许可证，详情请见 [LICENSE](LICENSE) 文件。

```
The MIT License (MIT)

Copyright (c) 2025 TSG海杀网页管理面板

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目。