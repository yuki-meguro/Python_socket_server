# coding: utf-8
"""
    Released under the Apache 2.0 License.
    Yuki Meguro
    https://github.com/yuki-meguro
"""

import configparser
import sys
import socket
import datetime

"""
ソケット通信用 基本関数
"""


def sock_main(s_data, conn_flg):
    # メイン
    try:
        ip, port, buf_size = sock_conf()
        if conn_flg == True:
            sock_open(ip, port)
        try:
            g_data = receive_data_int(buf_size)
            senddata(s_data)
        finally:
            pass
    except KeyboardInterrupt:
        print('\nプログラムを終了しました。\n')
        sys.exit()


def list_sock(list):
    # 与えられたリストを順番にソケット通信する関数
    list_size = len(list)
    conn_flg = True
    for i in range(list_size):
        data = list[i]
        sock_main(data, conn_flg)
        conn_flg = False
    return(0)


def sock_conf():
    # 設定ファイル読み込み
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    sec1 = "server"
    IP = config.get(sec1, 'IP')
    PORT = config.get(sec1, 'PORT')
    PORT = int(PORT)
    BUFFER_SIZE = config.get(sec1, 'BUFFER_SIZE')
    BUFFER_SIZE = int(BUFFER_SIZE)
    return IP, PORT, BUFFER_SIZE


def sock_open(IP, PORT):
    # ソケット接続
    global connection
    print('接続待ち....\n')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, PORT))
        s.listen()
        (connection, client) = s.accept()
        ip_tag = str(client[0])
        port_tag = str(client[1])
        one_line()
        nowtime()
        print('IP: ' + ip_tag + '\nPORT: ' + port_tag + '\n接続しました')
        one_line()
        return(0)


def receive_data_int(BUFFER_SIZE):
    # INT型 ソケット受信
    data = connection.recv(BUFFER_SIZE)
    conv_data = data.decode('utf-8')
    conv_data = str(conv_data)
    try:
        conv_int = int(conv_data)
    except ValueError:
        print('Data receive Err.\nProgram abort.\n')
        sys.exit()

    if conv_data == '':  # 空データ避け
        print('Data null.\nProgram abort.\n')
        sys.exit()
    else:
        return(conv_int)


def senddata(data):
    # ソケット送信
    s_data = str(data) + '\r\n'
    conv_data = s_data.encode('utf-8')
    try:
        connection.send(conv_data.upper())
        return(0)
    except BrokenPipeError:
        return(1)
    finally:
        pass


"""
コンソール整形用
"""


def one_line():
    print('-------------------------------')


def nowtime():
    nowt = datetime.datetime.now()
    nowt_str = str(nowt.strftime("%y-%m-%d %H:%M:%S"))
    print(nowt_str)
