import psutil

def 获取端口(process_name):
    """获取指定进程名称开启的所有端口"""
    opened_ports = []
    
    # 遍历所有活动进程
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 如果找到匹配的进程名
            if process_name.lower() in proc.info['name'].lower():
                # 获取进程的网络连接信息
                connections = proc.net_connections()
                for conn in connections:
                    if conn.status == psutil.CONN_LISTEN:  # 只关心监听状态的端口
                        opened_ports.append(conn.laddr.port)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return opened_ports

# 示例使用
process_name = "DreadHungerServer-Win64-Shipping.exe"  # 替换为实际的进程名称
exists = 获取端口(process_name)
print(f"进程 {process_name} 开启的端口有: {exists}")