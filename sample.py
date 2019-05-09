import socket_server

"""
サンプルプログラム
環境に応じて"./config/config.ini"の値を変更してください。
"""


def ex1():
    # clientからデータを受け取るとsend_dataを返します。
    send_data = int(1234)  # 送信データ
    conn_flg = True  # 初回通信接続
    socket_server.sock_main(send_data, conn_flg)


def ex2():
    # clientからデータを受け取る毎にlistを順番に返します。
    list = [1, 10, 100, 1000, 10000]
    socket_server.list_sock(list)


ex1()
# or
# ex2()
