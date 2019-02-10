import socket


def serverFunc():
    # 1 建立socket
    # ipv4协议簇
    # 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2 绑定ip and port
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 3 接受访问,等待方式死等
    # recvfrom接受
    data, addr = sock.recvfrom(500)  # 返回元组中的两项

    # 发送过来的数据bytes 格式：必须通过解码才能得到strg格式内容
    text = data.decode(encoding='utf-8')
    # 4 反馈
    rsp = "Ich hab keine Hunge"
    #
    data = rsp.encode()
    sock.sendto(data, addr)


if __name__ == '__main__':
    serverFunc()
