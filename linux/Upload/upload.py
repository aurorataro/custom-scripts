import sys
import requests
import os
import time

# 推送到nonebot钩子


def push_nonebot(push_title, push_desp):
    data = {"token": "xxxxxxxx", "title": push_title, "content": push_desp,
            "send_to": "xxxxxxxxxx", "send_to_group": "xxxxxxxx"
            }
    requests.post('http://xxx.xxx.xxx.xxx:10010/xxxxxxxxx', json=data)
    return


# 处理传参
file_num = len(sys.argv) - 1
file_path_first = str(sys.argv[1])
file_path = str(sys.argv[1])
x = 1
while x < file_num:
    x = x + 1
    file_path = file_path + ' ' + str(sys.argv[x])
# 循环结束，file_path 已经是完整的格式化过的多个文件路径

# 获得第一个文件文件名
(Temp, file_name_first) = os.path.split(file_path_first)

push_title = "🎥录像开始上传至BILIBILI"
push_desp = file_name_first+' 等...\n共' + \
    str(file_num)+'P\n' + \
    str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

push_nonebot(push_title, push_desp)

# 调用biliup-rs
Commandname_bili = '/root/biliuprs/biliup upload --copyright 1 --cover "/root/biliuprs/livecover.jpg" --desc "@流云心Aurora 的FF14录像" --line qn --no-reprint 1 --tag "直播录像","FF14" --tid 65 --title "【流云心】title xx-xx-xx [FFXIV]"'
Command = Commandname_bili + ' ' + file_path
code = os.system(Command)

if code == 0:
    push_title = "✔️成功上传至📺BILIBILI✔️"
    push_desp = "请等待审核👀和机器人推送🤖\n" + \
        str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
else:
    push_title = "❌上传出现问题❌"
    push_desp = "错读代码为"+str(code)+"\n请检查日志👀\n" + \
        str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

push_nonebot(push_title, push_desp)

push_title = "🎥开始上传至Tarocloud Folders"
push_desp = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

push_nonebot(push_title, push_desp)

# 调用OnedriveUploader
Command = '/root/1drive/onedriveuploader -f -c "/root/1drive/auth.json" -skip -s' + ' ' + '"' + file_path + '"' + '-r "Public/Media/Record"'
code = os.system(Command)

if code == 0:
    push_title = "✔️成功上传至📺od✔️"
    push_desp = "请等待审核👀和机器人推送🤖\n" + \
        str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
else:
    push_title = "❌上传出现问题❌"
    push_desp = "错读代码为"+str(code)+"\n请检查日志👀\n" + \
        str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

push_nonebot(push_title, push_desp)