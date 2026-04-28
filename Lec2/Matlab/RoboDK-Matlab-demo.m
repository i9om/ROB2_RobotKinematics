%% Start up rutine

clc
close
clear

% global robot

% Generate a Robolink object RDK. This object interfaces with RoboDK.
RDK = Robolink;

% Display the list of all items in the main tree
fprintf('Available items in the station:\n');
disp(RDK.ItemList());

robot = RDK.ItemUserPick('Select one robot', RDK.ITEM_TYPE_ROBOT);

if robot.Valid() == 0
    error('No robot selected');
end

%% jump to a location Set the home joints
jhome = [ -50, 40,-30, 30, 10, -50];

% Set the robot at the home position
robot.setJoints(jhome);

%% Move to a location


bT0= robot.Pose();

bT1 = bT0;
bT1(1,4) = bT0(1,4) - 100;
robot.MoveL(bT1);

bTt=[-1 0 0 500;
     0  1 0 300;
     0  0  -1 200;
     0  0  0  1;];
 
robot.MoveL(bTt);
 

%% Make a simple robot program

prog = RDK.AddProgram('Demo prog');
ref = robot.Parent();

targetname = sprintf('P1');
target = RDK.AddTarget(targetname,ref,robot);
target.setPose(bT1);
prog.MoveJ(target);

targetname = sprintf('P2');
target = RDK.AddTarget(targetname,ref,robot);
target.setPose(bTt);
prog.MoveJ(target);

prog.RunProgram();

