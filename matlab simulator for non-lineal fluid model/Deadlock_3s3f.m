
function sol = Deadlock()
    clc; clear; clear all;
    
    global bw;
    global pfcThresh;
  
    bw = 40e9;
    pfcThresh = 40e3*8;
    initial_step = 1e-5;
    max_step = 1e-5;
    
    options = ddeset('MaxStep', max_step, 'InitialStep', initial_step);
    
    sol = ode23(@pfc, [0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], options);

    t = sol.x;
    f1 = sol.y(1,:);
    f2 = sol.y(2,:);
    f3 = sol.y(3,:);
    g1 = sol.y(4,:);
    g2 = sol.y(5,:);
    g3 = sol.y(6,:); 
    h1 = sol.y(7,:);
    h2 = sol.y(8,:);
    h3 = sol.y(9,:);
    
    figure
    plot (t, f1, 'b');
    figure
    plot (t, f2, 'b');
    figure
    plot (t, f3, 'b');
    figure
    plot (t, g1, 'b');
    figure
    plot (t, g2, 'b');
    figure
    plot (t, g3, 'b');
    figure
    plot (t, h1, 'b');
    figure
    plot (t, h2, 'b');
    figure
    plot (t, h3, 'b');

end

function dy = pfc(t,y)
    global bw;
    global pfcThresh;

    dy = zeros(8, 1);
    
    % y
    % y1 = f1
    % y2 = f2
    % y3 = f3
    % y4 = g1
    % y5 = g2
    % y6 = g3
    % y7 = h1
    % y8 = h2
    % y9 = h3
    
    if (y(1) - y(2) < pfcThresh)
        dy(1) = bw;
    else
        dy(1) = 0;
    end
    
    denom = y(1) - y(2) + y(8) - y(9);
    
    if (denom > 0)
        dy(2) = bw*(y(1) - y(2))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(2) = bw/2;
        %dy(2) = 0;
    end
    
    dy(9) = bw-dy(2);
    
     denom = y(2) - y(3) + y(4) - y(5);
    
    if (denom > 0)
        dy(3) = bw*(y(2) - y(3))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(3) = bw/2;
        %dy(2) = 0;
    end
    
    dy(5) = bw-dy(3);
    
    
    if (y(4) - y(5) < pfcThresh)
        dy(4) = bw;
    else
        dy(4) = 0;
    end
    
    
     denom = y(5) - y(6) + y(7) - y(8);
    
    if (denom > 0)
        dy(6) = bw*(y(5) - y(6))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(6) = bw/2;
        %dy(2) = 0;
    end
    dy(8) = bw-dy(6);
    
    if (y(7) - y(8) < pfcThresh)
        dy(7) = bw;
    else
        dy(7) = 0;
    end
    
    if (y(2)-y(3) >= pfcThresh)
        dy(2)=0;
        dy(9)=0;
    end
    if (y(5)-y(6) >= pfcThresh)
        dy(3)=0;
        dy(5)=0;
    end
    if (y(8)-y(9) >= pfcThresh)
        dy(6)=0;
        dy(8)=0;
    end
    
    
    %fprintf('%g dy1=%g dy2=%g dy3=%g dy4=%g dy5=%g dy6=%g dy7=%g dy8=%g\n', t, dy(1), dy(2), dy(3), dy(4), dy(5), dy(6), dy(7), dy(8));
fprintf('%g y1=%g y2=%g y3=%g y4=%g y5=%g y6=%g y7=%g y8=%g dy1=%g dy2=%g dy3=%g dy4=%g dy5=%g dy6=%g dy7=%g dy8=%g\n', t, y(1), y(2), y(3), y(4), y(5), y(6), y(7), y(8), dy(1), dy(2), dy(3), dy(4), dy(5), dy(6), dy(7), dy(8));
end

