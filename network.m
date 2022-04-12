
clear;
T1 = load("/Users/yuzheng/Desktop/data1/network3450.txt");
T = sum(T1);
max_v = max(T);
T2 = T./max_v;
%[M,I] = max(T2);
%I2 = find(T2 <= M & T2 >= M*0.8)
%writematrix(T1, 'MyFile.txt')
%degree distribution