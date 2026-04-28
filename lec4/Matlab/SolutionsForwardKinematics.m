%% Solutions to exercise 1.1 on Forward kinematics

% Forward kinematics using Robotic Tool box
clear all
L1=1;
L2=1;
%Using Robotic Toolbox
L(1) = Link('alpha', 0,'a', 0,'d', 0,'modified') %rotational
L(2) = Link('alpha', 90*pi/180,'a', L1,'d', 0,'modified') %rotational
L(3) = Link('alpha', 0,'a', L2,'d', 0,'modified') %rotational
threeDOF=SerialLink(L, 'name', 'ThreeDOF-RRR');
%Lets test the movement
threeDOF.teach();

% Symbolic
syms theta1 theta2 theta3 L1 L2
PI=sym(pi)
T01= TDH(0,0,0,theta1);
T12= TDH(PI/2,L1,0,theta2);
T23= TDH(0,L2,0,theta3);
T03=simplify(T01*T12*T23)


%% Solutions to exercise 1.2 on Forward kinematics

% Forward kinematics using Robotic Tool box
% Using robotic toolbox
L1 = 0.5;

% alpha a d modified D&H
% Because we use Craig
L(1) = Link('alpha', 0,'a', 0,'d', 0,'modified') %rotational
L(2) = Link('alpha',pi/2,'a',L1,'theta',0,'modified') %translational
L(3) = Link('alpha',pi/2,'a', 0,'d', 0,'modified') %rotational
L(2).qlim=[0 1];

threeDOF=SerialLink(L, 'name', 'ThreeDOF-RRR');

threeDOF.plotopt = {'workspace' [-1,1,-1,1,-1,1]};

%Lets test the movement
threeDOF.teach();

% Symbolic
syms theta1 d2 theta3 L1
PI=sym(pi)
T01= TDH(0,0,0,theta1);
T12= TDH(PI/2,L1,d2,0);
T23= TDH(PI/2,0,0,theta3);
T03=simplify(T01*T12*T23)

%% %% Solutions to exercise 2 on Forward kinematics

clear all
% alpha a d theta offset modified D&H
L(1) = Link('alpha', 0,'a', 0,'d', 342, 'modified'); %rotational
L(2) = Link('alpha', 0,'a', 325,'d', 0, 'modified'); %rotational
L(3) = Link('alpha', 0,'a', 275, 'theta', 0,'offset',-165,'modified');%prismatic
L(4) = Link('alpha', 0,'a', 0,'d', 0, 'modified');%rotational
cobra=SerialLink(L, 'name', 'AdeptCobras600');
L(3).qlim=[0,1000];

%Lets test the movement
cobra.teach();


