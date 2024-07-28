% 读取语音信号
[signal, fs] = audioread('C6_2_y.wav');

% 设置不同的预测阶数
orders = [5, 10, 15, 20];
decoded_signals = cell(length(orders), 1);

% LPC 编码和解码
for i = 1:length(orders)
    order = orders(i);
    % LPC 编码
    [lpc_coeffs, g] = lpc(signal, order);
    % 计算残差信号
    residual = filter(lpc_coeffs, 1, signal);
    % LPC 解码
    decoded_signal = filter(1, lpc_coeffs, residual);
    decoded_signals{i} = decoded_signal;
end

% 绘制原始和解码信号进行比较
figure;
plot(signal, 'k');
hold on;
for i = 1:length(orders)
    plot(decoded_signals{i});
end
hold off;
legend(['Original Signal', arrayfun(@(x) ['Order ' num2str(x)], orders, 'UniformOutput', false)]);
xlabel('Sample Index');
ylabel('Amplitude');
title('Comparison of LPC Decoded Signals with Different Prediction Orders');

% 保存解码后的音频文件
for i = 1:length(orders)
    audiowrite(['output_audio_order_' num2str(orders(i)) '.wav'], decoded_signals{i}, fs);
end
