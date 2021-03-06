
function sol = Deadlock()
    clc; clear; clear all;
    
    global bw;
    global pfcThresh;
  
    bw = 40e9;
    pfcThresh = 40e3*8;
    initial_step = 1e-5;
    max_step = 1e-5;
    
    options = ddeset('MaxStep', max_step, 'InitialStep', initial_step);
    
    sol = ode23(@pfc, [0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], options);

    t = sol.x;
    f1 = sol.y(1,:);
    f2 = sol.y(2,:);
    f3 = sol.y(3,:);
    f4 = sol.y(4,:);
    g1 = sol.y(5,:);
    g2 = sol.y(6,:); 
    g3 = sol.y(7,:);
    g4 = sol.y(8,:);
    h1 = sol.y(9,:);
    h2 = sol.y(10,:);
    
    figure
    plot (t, f1, 'b', 'linewidth', 3);
    figure
    plot (t, f2, 'b', 'linewidth', 3);
    figure
    plot (t, f3, 'b', 'linewidth', 3);
    figure
    plot (t, f4, 'b', 'linewidth', 3);
    figure
    plot (t, g1, 'b', 'linewidth', 3);
    figure
    plot (t, g2, 'b', 'linewidth', 3);
    figure
    plot (t, g3, 'b', 'linewidth', 3);
    figure
    plot (t, g4, 'b', 'linewidth', 3);
    figure
    plot (t, h1, 'b', 'linewidth', 3);
    figure
    plot (t, h2, 'b', 'linewidth', 3);
end

function dy = pfc(t,y)
    global bw;
    global pfcThresh;

    dy = zeros(8, 1);
    
    % y
    % y1 = f1
    % y2 = f2
    % y3 = f3
    % y4 = f4
    % y5 = g1
    % y6 = g2
    % y7 = g3
    % y8 = g4
    
    if (y(1) - y(2) < pfcThresh)
        dy(1) = bw;
    else
        dy(1) = 0;
    end
    
    denom = y(1) - y(2) + y(7) - y(8);
    
    % how to ensure y2 <= y1
    
    if (denom > 0)
        dy(2) = bw*(y(1) - y(2))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(2) = bw/2;
        %dy(2) = 0;
    end
    
    dy(8) = bw-dy(2); 
    
    denom = y(2) - y(3) + y(9) - y(10);
     if (denom > 0)
        dy(3) = bw*(y(2) - y(3))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(3) = bw/2;
        %dy(2) = 0;
     end
    dy(10) = bw-dy(3); 
     
         
     
    if (y(5) - y(6) < pfcThresh)
        dy(5) = bw;
    else
        dy(5) = 0;
    end
    
    denom = y(5) - y(6) + y(3) - y(4);
    
    % how to ensure y2 <= y1
    
    if (denom > 0)
        dy(6) = bw*(y(5) - y(6))/denom;
    elseif (denom < 0)
        fprintf('error\n');
    else
        dy(6) = bw/2;
        %dy(6) = 0;
    end
    
    dy(4) = bw-dy(6);
    
    if (y(7) - y(8) < pfcThresh && y(6)-y(7) >0)
        dy(7) = bw;
    else
        dy(7) = 0;
    end
    
    
    
    if (y(9) - y(10) < pfcThresh)
        dy(9) = bw;
    else
        dy(9) = 0;
    end
    
    if (y(2)-y(3) >= pfcThresh)
        dy(2)=0;
        dy(8)=0;
    end
    if (y(3)-y(4) >= pfcThresh)
        dy(3)=0;
        dy(10)=0;
    end
    if (y(6)-y(7) >= pfcThresh)
        dy(4)=0;
        dy(6)=0;
    end
    
    
    %fprintf('%g dy1=%g dy2=%g dy3=%g dy4=%g dy5=%g dy6=%g dy7=%g dy8=%g\n', t, dy(1), dy(2), dy(3), dy(4), dy(5), dy(6), dy(7), dy(8));
fprintf('%g y1=%g y2=%g y3=%g y4=%g y5=%g y6=%g y7=%g y8=%g y9=%g y10=%g dy1=%g dy2=%g dy3=%g dy4=%g dy5=%g dy6=%g dy7=%g dy8=%g dy9=%g dy10=%g\n', t, y(1), y(2), y(3), y(4), y(5), y(6), y(7), y(8), y(9), y(10), dy(1), dy(2), dy(3), dy(4), dy(5), dy(6), dy(7), dy(8), dy(9), dy(10));
end

