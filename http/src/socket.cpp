#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

/*
    struct addrinfo{
        int ai_flag; // AI_PASSIVE AI_CANONNAME等
        int ai_family;  // AF_INET AF_INET6 AF_UNSPEC
        int ai_socktype;    // SOCK_STREAM SOCK_DGRAM
        int ai_protocal;    // 用0 当作any
        size_t ai_addrlen; // ai_addr大小
        struct sockaddr *ai_addr; // struct sockaddr_in 或者 struct sockaddr_in6
        char *ai_canonname; // 典型的hostname
        struct addrinfo *ai_next; // 下一个节点指针
    };

    struct sockaddr {
        unsigned short sa_family;   // address family, AF_INET
        char sa_data[14]; // 14bytes of protocal address
    };

    struct sockaddr_in{
        short int sin_family;           // Address_famliy
        unsigned short int sin_port;    // port_number
        struct in_addr sin_addr;    // Internet address
        unsigned char sin_zero[8];  // 和struct sockaddr一个大小
    };

    struct in_addr{
        uint32_t s_addr; // 32_bit int (4bytes)
    };
*/

int main(int argc,char *argv[]){
    struct addrinfo hints, *res;
    // 先设置好地址内存大小以及协议
    memeset(&hints,0,sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flag = AI_PASSIVE; // fill the ip for me

    getaddrinfo(NULL,"3490",&hints,&res);

    s = socket(res->ai_family,res->ai_socktype,res->ai_protocal);
    // return fd;
    // 绑定
    bind(s,res->ai_addr,res->ai_addrlen);
    // 链接
    connect(sockfd,res->ai_addr,res_>ai_addrlen);

    // 聆听
    listen(s,15);

    //接受 fd, struct addr , socklen_t
    accept(s, (struct addr*)&)
}