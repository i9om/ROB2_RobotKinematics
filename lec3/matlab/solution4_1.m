%Solutions to Exercise 1 - lecture 4

%--------------------------------
%% 1. Compute the rotation matrices which correspond to:
%       Extrinsic (fixed axis rotation) rotation about XYZ (Craigs roll, pitch, yaw): 
%       Roll(X)=30;Pitch(Y)=50,Yaw(Z)=-20

roll  = 30*pi/180;
pitch = 50*pi/180;
yaw   =-20*pi/180;

%Two ways (the elementary rotation and the product (from Craig) -nhopefully they give the same results:

R1_multi = rotz(yaw)*roty(pitch)*rotx(roll)
R1_matrix=[cos(yaw)*cos(pitch)  cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll) cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll) ;
             sin(yaw)*cos(pitch)  sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll) sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll);
             -sin(pitch)          cos(pitch)*sin(roll)                             cos(pitch)*cos(roll)]

%and now with the toolbox:
R1_toolbox=rpy2r(roll,pitch,yaw,'zyx') %Note: Corke uses intrinsic XYZ - to transform change rotation sequence 

         
%----------------------------
%% Compute the rotation matrices which correspond to:
%       Intrinsic rotation about ZYX
%       X(gamma)=20;Y(beta)=-15,Z(alpha)=30


alpha  = 30*pi/180;
beta   =-15*pi/180;
gamma  = 20*pi/180;


%Two ways (the elementary rotation and the product (from Craig) -nhopefully they give the same results:

R2_multi = rotz(alpha)*roty(beta)*rotx(gamma)%Using formula from slides and Crieg
R2_matrix=[cos(alpha)*cos(beta)  cos(alpha)*sin(beta)*sin(gamma)-sin(alpha)*cos(gamma) cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma) ;
           sin(alpha)*cos(beta)  sin(alpha)*sin(beta)*sin(gamma)+cos(alpha)*cos(gamma) sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma);
           -sin(beta)            cos(beta)*sin(gamma)                                  cos(beta)*cos(gamma)]

%and now with the toolbox:
R2_toolbox=rpy2r(gamma,beta,alpha,'zyx') %Note: Corke uses intrinsic XYZ - to transform change rotation sequence 

%----------------------------
%% Compute the rotation matrices which correspond to:
%       Angle/axis representation: theta = 21.8583 degrees; k =[0.3379;0.4808;0.8093]

theta  = 21.8583*pi/180;
kx     =  0.3379;
ky     =  0.4808;
kz     =  0.8093;

%insert into axis/angle formula (2.80)
R3_matrix= [kx*kx*(1-cos(theta))+cos(theta)     kx*ky*(1-cos(theta))-kz*sin(theta) kx*kz*(1-cos(theta))+ky*sin(theta) ;
            kx*ky*(1-cos(theta))+kz*sin(theta)  ky*ky*(1-cos(theta))+cos(theta)    ky*kz*(1-cos(theta))-kx*sin(theta) ;
            kx*kz*(1-cos(theta))-ky*sin(theta)  kz*ky*(1-cos(theta))+kx*sin(theta) kz*kz*(1-cos(theta))+cos(theta)]

% and now with the toolbox:
R3_toolbox=angvec2r(theta,[kx ky kz])

%----------------------------
%% Compute the rotation matrices which correspond to:
%       Quaternion = [0.064071;0.091158;0.15344;0.98186;]

e1=0.064071;
e2=0.091158;
e3=0.15344;
e4=0.98186;

theta  = 21.8583*pi/180;
kx     =  0.3379;
ky     =  0.4808;
kz     =  1.8093;

%Method 1:Insert into axis/angle formula (2.91)
R4_matrix= [1-2*e2^2-2*e3^2     2*(e1*e2-e3*e4) 2*(e1*e3+e2*e4) ;
            2*(e1*e2+e3*e4)  1-2*e1^2-2*e3^2    2*(e2*e3-e1*e4) ;
            2*(e1*e3-e2*e4)  2*(e2*e3+e1*e4)    1-2*e1^2-2*e2^2]


%Method 2: Compute axis/angle rotation

theta=2*acos(e4)
kx=e1/sin(theta/2)
ky=e2/sin(theta/2)
kz=e3/sin(theta/2)

%insert into axis/angle formula
R4_axisAngle=[kx*kx*(1-cos(theta))+cos(theta)     kx*ky*(1-cos(theta))-kz*sin(theta) kx*kz*(1-cos(theta))+ky*sin(theta) ;
            kx*ky*(1-cos(theta))+kz*sin(theta)  ky*ky*(1-cos(theta))+cos(theta)    ky*kz*(1-cos(theta))-kx*sin(theta) ;
            kx*kz*(1-cos(theta))-ky*sin(theta)  kz*ky*(1-cos(theta))+kx*sin(theta) kz*kz*(1-cos(theta))+cos(theta)]
        
%and now with the toolbox:
R4_toolbox = Quaternion([e4 e1 e2 e3]).R
