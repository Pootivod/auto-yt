from __future__ import unicode_literals
import psutil
import time
import ctypes
import sys
from mitmproxy import http
from bs4 import BeautifulSoup
from download import download_list
from history import *
from yt_dlp import YoutubeDL

def monitoring():
    print("Tw every music enjoyer hello :)")
    #while True:
    connections = psutil.net_connections(kind="inet")
    for conn in connections:
        print (conn)
        if conn.status == 'ESTABLISHED' and conn.raddr:
            print(f"Local address: {conn.laddr}, Remote address: {conn.raddr}, PID: {conn.pid}")
    time.sleep(1)

def get_admin():
        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            print("I'm admin faster")
            return
        else:
            script = sys.argv[0]
            params = " ".join(sys.argv[1:])
            # Запуск того же скрипта с правами администратора
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            sys.exit(0)
            print("I'm admin slower")
            return
    
if __name__ == "__main__":
    if input("Do you want to update tracks?: ") != "":
        data = upadte_history()
    else:
        data = read_json()
    download_list(data)