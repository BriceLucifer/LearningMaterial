clc
close all
clear all
[x,fs]=audioread('C6_2_y.wav');  % 读取音频文件，只返回音频数据和采样率
LENGTH=length(x);                          
n=0:1/fs:(LENGTH-1)/fs;   % 时间轴

% 原始语音信号
subplot(2,1,1),plot(n*1000, x),grid ,hold on
xlabel('时间 (ms)');    ylabel('幅度');

% LPC编解码过程
order=12;                                           % 阶数
[a,g]=lpc(x,order);                                 % 获取预测系数（编码参数）
est_x=filter([0 -a(2:end)],1,x);                    % 使用预测系数得到解码后的信号
plot(n*1000,est_x,'r--'),hold off
title('原始信号与解码后信号')
legend('原始信号','解码后信号')

% 预测误差
error=x-est_x;                                      % 计算预测误差
subplot(2,1,2),plot(n*1000,error), grid;
xlabel('时间 (ms)');    ylabel('幅度');
title('预测误差')
