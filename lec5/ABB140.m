

%% Section1 
%            alpha      a        d     modified D&H
%                                      Because we use Craig            

T= [1 0 0 0;
      0 1 0 0;
      0 0 1 352;
      0 0 0 1];

L1=Link('d',  0,'a',  0,'alpha',  0,       'modified');
L2=Link('d',  0,'a', 70,'alpha',-90*pi/180,'offset',-90*pi/180,'modified');
L3=Link('d',  0,'a',360,'alpha',  0,       'modified');
L4=Link('d',380,'a',  0,'alpha',-90*pi/180,'modified');
L5=Link('d',  0,'a',  0,'alpha', 90*pi/180,'modified');
L6=Link('d',  0,'a',  0,'alpha',-90*pi/180,'modified');
 
ABB140x=SerialLink([L1 L2 L3 L4 L5 L6], 'name', 'ABB');
 
q=[10 20 30 40 50 60]*pi/180;

T06=cast(ABB140x.fkine(q), 'like', T)  

RZYX = tr2rpy(T06,'deg','zyx')

    

%% Section 2 Move base frame

TB0= [1 0 0 0;
      0 1 0 0;
      0 0 1 352;
      0 0 0 1];

TB6 = TB0*T06

RZYX = tr2rpy(TB6,'deg','zyx')

%% Step 3 Move wrist frame

T6W= [-1  0  0  0;
      0  -1  0  0;
      0  0  1 65;
      0  0  0  1];

TBW=TB0*T06*T6W  
ZYX = tr2rpy(TBW,'deg','zyx')
 
%% step 4 With tool data

TWT=transl(-4,0,371.300)*troty(45*pi/180);
TBT=TB0*T06*T6W*TWT
ZYX = tr2rpy(TBT,'deg','zyx')

