import socket
def main():
    #1.创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定一个本地信息
    local_addr = ("",8080)#ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socket.bind(local_addr)  # 必须绑定自己带闹闹的ip以及port,其它的不行
    #3.接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)#最大是1024个字节
        #4.打印接收到的数据
        print(recv_data)
     #5.关闭套接字
    udp_socket.close()

if __name__ =="__main__":
    main()
