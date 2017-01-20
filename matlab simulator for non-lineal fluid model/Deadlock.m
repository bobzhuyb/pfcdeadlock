
function sol = Deadlock()
    clc; clear; clear all;
    
    global bw;
    global pfcThresh;
  
    bw = 40e9;
    pfcThresh = 40e3*8;
    initial_step = 1e-5;
    max_step = 1e-5;
    
    options = ddeset('MaxStep', max_step, 'InitialStep', initial_step);
    
    sol = ode23(@pfc, [0, 1], [0, 0, 0, 0], options);

    t = sol.x;
    s1i = sol.y(1,:);
    s1o = sol.y(2,:);
    s2i = sol.y(3,:);
    s2o = sol.y(4,:);
    
    figure
    plot (t, s1i, 'b');
    hold on
    plot (t, s2i, 'r');
end

function dy = pfc(t,y)
    global bw;
    global pfcThresh;

    dy = zeros(4, 1);
    
    % y
    % y1 = s1i
    % y2 = s1o
    % y3 = s2i
    % y4 = s2o
    %
    
    if (y(1) - y(2) < pfcThresh)
        dy(1) = bw;
    else
        dy(1) = 0;
    end
    
    denom = y(1) - y(2) + y(3) - y(4);
    
    % how to ensure y2 <= y1
    
    if (denom > 0)
        dy(2) = bw*(y(1) - y(2))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        %dy(2) = bw/2;
         dy(2) = 0;
    end
    
    if (y(3) - y(4) < pfcThresh)
        dy(3) = bw;
    else
        dy(3) = 0;
    end
    
    dy(4) = bw-dy(2);
    
    fprintf('%g y1=%g y2=%g y3=%g y4=%g dy1=%g dy2=%g dy3=%g dy4=%g\n', t, y(1), y(2), y(3), y(4), dy(1), dy(2), dy(3), dy(4));

end

