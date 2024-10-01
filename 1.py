import subprocess

# 程序路径和参数
program_path = "DreadHungerServer.exe"
arguments = ["-log", "-loglevel", "trace"]

# 启动进程，并将stdout和stderr重定向到管道
# 使用universal_newlines=True和bufsize=1来禁用输出缓冲
process = subprocess.Popen([program_path] + arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1)

# 循环读取并打印日志
try:
    # 使用iter函数来逐行读取日志
    for line in iter(process.stdout.readline, ''):
        print(line.strip())
finally:
    # 确保进程已经结束
    process.stdout.close()
    process.wait()