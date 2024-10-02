from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import time
import hashlib
import psutil
import glob
import subprocess
import requests
import zipfile
from io import BytesIO
from datetime import datetime
from collections import defaultdict
from werkzeug.utils import secure_filename
app = Flask(__name__)




####################################轮子#############################################
def get_config_value(key, default=None):
    try:
        with open('webconfig.json', 'r') as f:
            config = json.load(f)
        return config.get(key, default)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def check_exe_exists(exe_name):
    return os.path.exists(exe_name)
def check_process_exists(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def 结束进程(process_name):
    # 遍历获取到的所有运行中的进程
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == process_name:
                print(f"找到进程 {process_name}，PID: {proc.info['pid']}，正在终止...")
                proc.terminate()  
                proc.wait() 
                print(f"进程 {process_name} 已成功终止。")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  

#下载
def download_and_extract(url, extract_to):

    response = requests.get(url)
    response.raise_for_status()  


    zip_file = zipfile.ZipFile(BytesIO(response.content))

    zip_file.extractall(extract_to)
    zip_file.close()

####################################变量#############################################


def update_global_variables():
    #刷新全部全局变量
    global port1
    global port2
    global ip
    global mapa
    global playermax
    global thralls
    global dayminutes
    global daysbeforeblizzard
    global predatordamage
    global coalburnrate
    global hungerrate
    global coldintensity
    
    port1 = get_config_value('port1', '')
    port2 = get_config_value('port2', '')
    ip = get_config_value('IP', '')
    mapa = get_config_value('map', '')
    playermax = get_config_value('playermax', '')
    thralls = get_config_value('thralls', '')
    dayminutes = get_config_value('dayminutes', '')
    daysbeforeblizzard = get_config_value('daysbeforeblizzard', '')
    predatordamage = get_config_value('predatordamage', '')
    coalburnrate = get_config_value('coalburnrate', '')
    hungerrate = get_config_value('hungerrate', '')
    coldintensity = get_config_value('coldintensity', '')
    


#从Config获取全局变量
port1 = get_config_value('port1', '')
port2 = get_config_value('port2', '')
ip = get_config_value('IP', '')
mapa = get_config_value('map', '')
playermax = get_config_value('playermax', '')
thralls= get_config_value('thralls', '')
dayminutes= get_config_value('dayminutes', '')
daysbeforeblizzard= get_config_value('daysbeforeblizzard', '')
predatordamage= get_config_value('predatordamage', '')
coalburnrate= get_config_value('coalburnrate', '')
hungerrate= get_config_value('hungerrate', '')
coldintensity= get_config_value('coldintensity', '')
isport = port1




####################################路由#############################################
@app.route('/')
def home():
    update_global_variables()
    exe_exists = check_exe_exists('DreadHungerServer.exe')
    return render_template('home.html', exe_exists=exe_exists, 
                           tsg = 检测TSG插件(),)

@app.route('/up')
def up():
    return render_template('up.html')
@app.route('/process_status')
def process_status():
    process_name = 'DreadHungerServer'
    exists = check_process_exists(process_name)
    return jsonify({'exists': exists})

@app.route('/port')
def process_status_port():
    global isport
    return jsonify({'port': isport})
#配置网页
@app.route('/config')
def config_page():
    
    return render_template('config.html', port1=port1,
                           port2=port2,
                           ip=ip,
                           playermax=playermax,
                           
                           thralls=thralls,
                           dayminutes=dayminutes,
                           daysbeforeblizzard=daysbeforeblizzard,
                           predatordamage=predatordamage,
                           coalburnrate=coalburnrate,
                           hungerrate=hungerrate,
                           coldintensity=coldintensity,
                           map=mapa,
                           filenames = 读取补丁目录(),
                           jspatches = 读取TSG补丁JS(),
                           binpatches = 读取TSG补丁Bin()
                           )
#保存配置
@app.route('/save_config', methods=['POST'])
def save_config():
    config_data = request.form.to_dict()
    with open('webconfig.json', 'w') as f:
        json.dump(config_data, f)
        
    return redirect(url_for('home'))

@app.route('/save_game_config', methods=['POST'])
def save_game_config():
    config_data = request.form.to_dict()
    with open('Gameconfig.json', 'w') as f:
        json.dump(config_data, f)
    return redirect(url_for('home'))

#文件

#删除文件
@app.route('/delete', methods=['GET'])
def delete_file():
    filename = request.args.get('filename')
    
    if not filename:
        return jsonify({'success': False, 'message': '缺少文件名参数'})

    directories = [
        r'DreadHunger\Binaries\Win64\Pacthes',
        r'JsPlugin',
        r'TSGPlugin'
    ]
    
    success = True
    messages = []

    for directory in directories:

        file_path = os.path.join(directory, filename)
        
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                messages.append(f'在{directory}下的文件{filename}已成功删除')
            else:
                messages.append(f'在{directory}下找不到文件{filename}')
        except Exception as e:
            success = False
            messages.append(f'在{directory}删除文件{filename}时出错: {str(e)}')

    return jsonify({
        'success': success,
        'message': '\n'.join(messages) 
    })




@app.route('/DownPaches', methods=['GET'])
def Down_Paches():
    url = 'http://vps3.elfidc.com:52018/d/%E5%85%B6%E4%BB%96%E6%96%87%E4%BB%B6/Win64.zip'
    extract_to = r'DreadHunger\Binaries\Win64'
    download_and_extract(url, extract_to)
    return redirect(url_for('home'))




UPLOAD_FOLDER = r'DreadHunger\Binaries\Win64\Pacthes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "上传失败"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "上传失败"}), 400
    if file:

        filename = secure_filename(file.filename)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({"message": f"文件 {filename} 成功上传."}), 200


@app.route('/save_default_config', methods=['POST'])
def save_default_config():
    config_data = request.form.to_dict()
    with open('Defaultconfig.json', 'w') as f:
        json.dump(config_data, f)
    return redirect(url_for('home'))




@app.route('/save_tsg_config', methods=['POST'])
def save_tsg_config():
    config_data = request.form.to_dict()
    with open('Tsgconfig.json', 'w') as f:
        json.dump(config_data, f)
    return redirect(url_for('home'))
####################################路由#############################################

####################################服务器相关########################################
# 全局变量用于控制自动重启循环是否继续
global should_stop_auto_restart
should_stop_auto_restart = False

global global_process
global_process = None


@app.route('/start_server')
def start_server():
    run_program("DreadHungerServer.exe",mapa + 
                "?playermax=" + playermax + 
                "?thralls=" + thralls +
                "?dayminutes=" + dayminutes +
                "?daysbeforeblizzard=" + daysbeforeblizzard +
                "?predatordamage=" + predatordamage +
                "?coalburnrate=" + coalburnrate +
                "?hungerrate=" + hungerrate +
                "?coldintensity=" + coldintensity,
                "-port="+ port1,
                "-log",
                )
    return redirect(url_for('home'))

@app.route('/stop_server')
def stop_server():

    global should_stop_auto_restart
    should_stop_auto_restart = True  
    if global_process:
        global_process.terminate()  
    结束进程("DreadHungerServer.exe")
    结束进程("DreadHungerServer-Win64-Shipping.exe")
    return redirect(url_for('home'))
@app.route('/stop_server/auto')
def stop_server_auto():
    结束进程("DreadHungerServer.exe")
    结束进程("DreadHungerServer-Win64-Shipping.exe")
    return redirect(url_for('home'))


@app.route('/start_server/auto')
def start_server_auto():
    global should_stop_auto_restart
    should_stop_auto_restart = False 
    global isport

    run_program_auto("DreadHungerServer.exe")
    return redirect(url_for('home'))

def run_program(program_path, *args):
    try:
        subprocess.Popen([program_path] + list(args))
        print(f"成功启动程序: {program_path} 参数: {args}")
    except FileNotFoundError:
        print(f"错误：找不到程序 {program_path}")
    except Exception as e:
        print(f"启动程序时发生错误: {e}")

def run_program_auto(program_path):
    
    # 他妈的这里真是 狗屎中狗屎
    # 第一次asgs不读的 进循环没了
    # 用全局变量他妈的也有问题
    # 我真的草了
    
    global should_stop_auto_restart
    global global_process
    global isport
    
    try:
        
        args = [
            mapa + 
            "?playermax=" + playermax + 
            "?thralls=" + thralls +
            "?dayminutes=" + dayminutes +
            "?daysbeforeblizzard=" + daysbeforeblizzard +
            "?predatordamage=" + predatordamage +
            "?coalburnrate=" + coalburnrate +
            "?hungerrate=" + hungerrate +
            "?coldintensity=" + coldintensity,
            "-port="+ isport,
            "-log",
        ]
        

        global_process = subprocess.Popen([program_path] + list(args))
        

        while not should_stop_auto_restart:
            
            if global_process.poll() is not None:
                
                if isport == port1:
                    isport = port2 
                else:
                    isport = port1
                    
                args = [
                    mapa + 
                    "?playermax=" + playermax + 
                    "?thralls=" + thralls +
                    "?dayminutes=" + dayminutes +
                    "?daysbeforeblizzard=" + daysbeforeblizzard +
                    "?predatordamage=" + predatordamage +
                    "?coalburnrate=" + coalburnrate +
                    "?hungerrate=" + hungerrate +
                    "?coldintensity=" + coldintensity,
                    "-port="+ isport,
                    "-log",
                ]    
                
                print(f"成功启动程序: {program_path} 参数: {args} {isport}")
            

                global_process = subprocess.Popen([program_path] + list(args))
            else:
                time.sleep(1) 
        
    except FileNotFoundError:
        print(f"错误：找不到程序 {program_path}")
    except Exception as e:
        print(f"启动程序时发生错误: {e}")

def end_process(process_name):
    import psutil
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            p = psutil.Process(proc.info['pid'])
            p.terminate()

####################################服务器相关##########################################

######################################补丁################################################

def 读取补丁目录():
    directory = r'DreadHunger\Binaries\Win64\Pacthes'
    js_files = glob.glob(os.path.join(directory, '*.js'))
    filenames = [os.path.basename(file) for file in js_files]
    return filenames

def 读取TSG补丁JS():
    directory = r'JsPlugin'
    js_files = glob.glob(os.path.join(directory, '*.js'))
    filenames = [os.path.basename(file) for file in js_files]
    return filenames

def 读取TSG补丁Bin():
    directory = r'TSGPlugin'
    js_files = glob.glob(os.path.join(directory, '*.bin'))
    filenames = [os.path.basename(file) for file in js_files]
    return filenames



def MD5计算(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def 检测TSG插件():
    expected_md5 = "2b91b31cf72f7b0a484ca6e810b5a608"
    md5 = MD5计算(r"DreadHungerServer.exe")
    return md5 == expected_md5





######################################补丁################################################



######################################日志#############################################
#读取日志
@app.route('/get_log')
def display_connection_info():
    global current_port
    log_files = get_log_files()

    all_cheat_summaries = defaultdict(lambda: {'count': 0, 'cheats': set()})

    for filename in log_files:
        summary = get_cheat_summary(filename)

        if isinstance(summary, dict):
            for player, details in summary.items():
                all_cheat_summaries[player]['count'] += details['count']
                all_cheat_summaries[player]['cheats'].update(details['cheats'])

    return render_template('log.html', log_files=log_files, cheat_summaries=all_cheat_summaries)
#检测玩家作弊
def get_cheat_summary(filename):
    try:
        with open(os.path.join(r'.\DreadHunger\Saved\Logs', filename), 'r', encoding='utf-8') as log_file:
            log_content = log_file.read()

        filtered_lines = [line for line in log_content.split('\n') if 'LogDHAntiCheat' in line]

        cheat_summary = defaultdict(lambda: {'count': 0, 'cheats': set()})
        for line in filtered_lines:
            parts = line.split('Warning: ')
            if len(parts) > 1:
                player_name = parts[1].split(' was found')[0].strip()
                cheat_type_start = parts[1].find('[')
                cheat_type_end = parts[1].find(']')
                if cheat_type_start != -1 and cheat_type_end != -1:
                    cheat_type_english = parts[1][cheat_type_start+1:cheat_type_end].strip()
                    cheat_type_chinese = cheat_types_mapping.get(cheat_type_english, cheat_type_english) 
                    cheat_summary[player_name]['count'] += 1
                    cheat_summary[player_name]['cheats'].add(cheat_type_chinese)

        if not cheat_summary:
            return "未发现作弊者"
        else:
            return cheat_summary

    except FileNotFoundError:
        return f"日志文件'{filename}'未找到"
    except Exception as e:
        return f"处理'{filename}'时出现错误: {str(e)}"
 
#中文翻译    
cheat_types_mapping = {
    'Speed Hacking': '[极低]游戏加速',
    'Item Hoovering': ' [低]长距离交互',
    'Shot Bullet Through Wall': '[中]子弹穿墙',
    'Long Range Interacts': '[低]远距离交互',
    'Shot Arrow Through Wall':'[中]弓箭穿墙',
    'Fast Reloads': '[中]快速换弹',
}   
#遍历目录
def get_log_files(directory=r'.\DreadHunger\Saved\Logs'):
    log_files_with_path = glob.glob(os.path.join(directory, '*.log'))
    
    log_files_dict = {}
    for file_path in log_files_with_path:
        modification_time = os.path.getmtime(file_path)
        time_stamp_datetime = datetime.fromtimestamp(modification_time)
        file_name = os.path.basename(file_path)
        log_files_dict[file_name] = time_stamp_datetime
    
    if not log_files_dict:
        return "错误：未找到任何.log文件。"
    else:
        sorted_log_files = sorted(log_files_dict, key=log_files_dict.get, reverse=True)
        return sorted_log_files
#读取目录
@app.route('/log/<filename>')
def view_log_file(filename):
    directory = r'.\DreadHunger\Saved\Logs'
    try:
        for encoding in ['utf-8', 'gbk']:
            try:
                with open(os.path.join(directory, filename), 'r', encoding=encoding) as log_file:
                    log_content = log_file.read()
                    break
            except UnicodeDecodeError:
                pass  

        filtered_lines = [line for line in log_content.split('\n') if 'LogDHAntiCheat' in line]

        if not filtered_lines:
            filtered_lines = [line for line in log_content.split('\n') if 'LogDHAntiCheat' in line]

        cheat_summary = defaultdict(lambda: {'count': 0, 'cheats': set()})
        for line in filtered_lines:
            parts = line.split('Warning: ')
            if len(parts) > 1:
                player_name = parts[1].split(' was found')[0].strip()
                cheat_type_start = parts[1].find('[')
                cheat_type_end = parts[1].find(']')
                if cheat_type_start != -1 and cheat_type_end != -1:
                    cheat_type_english = parts[1][cheat_type_start+1:cheat_type_end].strip()
                    cheat_type_chinese = cheat_types_mapping.get(cheat_type_english, cheat_type_english) 
                    cheat_summary[player_name]['count'] += 1
                    cheat_summary[player_name]['cheats'].add(cheat_type_chinese)
        summary_content = ""
        if not cheat_summary:
            summary_content = "未发现作弊者"
        else:
            summary_content = ""
            for player, info in cheat_summary.items():
                cheats_chinese = '|'.join([cheat_types_mapping.get(cheat, cheat) for cheat in info['cheats']])
                summary_content += f"{player}: 次数 {info['count']}次, 作弊信息:{cheats_chinese}\n"

        return render_template('logs.html', filename=filename, summary_content=summary_content, log_content=log_content)

    except FileNotFoundError:
        return "日志文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500  

######################################日志################################################

if __name__ == '__main__':
    app.run(debug=True)