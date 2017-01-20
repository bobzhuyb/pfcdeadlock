close all; clear all; clc;

load trace380.txt
load trace381.txt
load trace382.txt
load trace540.txt
load trace541.txt
load trace542.txt
load trace760.txt
load trace761.txt
load trace762.txt

figure
hold on
plot(trace380(:,1) - 2, trace380(:,2), 'r')
plot(trace760(:,1) - 2, trace760(:,2), 'b')
plot(trace540(:,1) - 2, trace540(:,2), 'k')
xlabel('Time / Seconds','fontsize',16)
ylabel('Received Sequence Number','fontsize',16)
legend('3->8 @ 0', '7->6 @ 0', '5->4 @ 0')

figure
hold on
plot(trace380(:,1) - 2, trace380(:,2), 'r')
plot(trace381(:,1) - 2, trace381(:,2), 'b')
plot(trace382(:,1) - 2, trace382(:,2), 'k')
xlabel('Time / Seconds','fontsize',16)
ylabel('Received Sequence Number','fontsize',16)
legend('3->8 @ 0', '3->8 @ 1', '3->8 @ 2')


figure
xi = 0:0.000001:0.001644;

[tmp, index] = unique(trace380(:,1) - 2);
yi380 = interp1(tmp, trace380(index,2), xi);

[tmp, index] = unique(trace760(:,1) - 2);
yi760 = interp1(tmp, trace760(index,2), xi);

[tmp, index] = unique(trace381(:,1) - 2);
yi381 = interp1(tmp, trace381(index,2), xi);

[tmp, index] = unique(trace761(:,1) - 2);
yi761 = interp1(tmp, trace761(index,2), xi);

plot(xi, yi380 + yi760 - yi381 - yi761)

xlabel('Time / Seconds','fontsize',16)
ylabel('Queue Length / Packets','fontsize',16)
