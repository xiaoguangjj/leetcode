import subprocess

# 利用subprocess模板，创建子进程，打开.mp3和解压文件
proc = subprocess.Popen(
    ["start", "./datas/.mp3"],
    shell=True
)
proc.communicate()

proc = subprocess.Popen(
    [r"C:\Progress Files\7-Zip\7z.exe",
     "x",
     "./datas/7z_test.7z",
     "-o./datas/extract_7z",
     "-ace"],
    shell=True
)

proc.communicate()