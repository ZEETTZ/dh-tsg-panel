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

本项目采用 CC BY-NC 4.0 许可证，详情请见 [LICENSE](LICENSE) 文件。

```
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

Copyright (c) 2025 TSG Team

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial — You may not use the material for commercial purposes.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For full license text, see: https://creativecommons.org/licenses/by-nc/4.0/legalcode

--------------------

创作共用（CC BY-NC 4.0）非商业许可

版权所有 (c) 2025 TSG Team

您可以自由：
- 分享 — 在任何媒介或格式上复制、发行本作品
- 演绎 — 混合、转换和基于本作品创作新作品

但须遵守以下条件：
- 署名 — 必须给予适当的署名，提供许可证链接，并说明是否进行了修改。
- 非商业性使用 — 不能将本作品用于商业目的。

无其他限制 — 不得施加法律条款或技术措施，从法律上禁止他人做许可允许的事情。

完整许可文本参见：https://creativecommons.org/licenses/by-nc/4.0/legalcode
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目。
