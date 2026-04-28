%Solutions to Exercise 2 - lecture 3

%--------------------------------
%Given the Rotation matrix R:

R= [0.9752   -0.0370    0.2184;
    0.0978    0.9564   -0.2751;
   -0.1987    0.2896    0.9363];

%1. Compute RPY corresponfing to R

Pitch=atan2(-R(3,1),sqrt(R(1,1)^2+R(2,1)^2))
if (abs(abs(Pitch)-90)<0.00001)
    Yaw=0
    Roll=Pitch/abs(Pitch)*atan2(R(1,2),R(2,2))
else
    Yaw=atan2(R(2,1)/cos(Pitch),R(1,1)/cos(Pitch))
    Roll=atan2(R(3,2)/cos(Pitch),R(3,3)/cos(Pitch))
end

%And now with tool box:
RPY=tr2rpy(R,'zyx')

%2. compute angle/axis representation
theta = acos((R(1,1)+R(2,2)+R(3,3)-1)/2)
if (abs(theta) < 0.000001)
    K = [0;0;0]
else
    K=1/(2*sin(theta))*[R(3,2)-R(2,3);R(1,3)-R(3,1);R(2,1)-R(1,2)]
end

%3. compute quaternions (Craig eq 2.92)

e4 = 0.5*sqrt(R(1,1)+R(2,2)+R(3,3)+1)
e1 = (R(3,2)-R(2,3))/(4*e4)
e2 = (R(1,3)-R(3,1))/(4*e4)
e3 = (R(2,1)-R(1,2))/(4*e4)

%And now with tool box:
q=UnitQuaternion(R)


