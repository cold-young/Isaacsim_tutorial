# Add Your URDF with Isaac Sim GUI
26.01.13 <br>
Written by Chanyoung Ahn


# 1. Add and Control Robot
This tutorial shows how to 1) `add` your own URDF file with Isaac Sim 2) `validate` DOF and 3) `run` a simple simulation.


1. Open Isaac Sim and import your urdf (File -> Import -> your_robot.urdf)
    <img src="../img/t1_1.png" alt="t1_1" width="60%" />
<br>

2. Load your urdf with customized options.. 
   * ([x] Allow Self-Collisions, [x] Convex Hull)<br>
    <img src="../img/t1_2.png" alt="t1_2" width="60%" />

3. Add robot joint controller 
   * (Tools > Robotics > OmniGraph Controllers > Joint Position)
    <img src="../img/t1_3.png" alt="t1_3" width="60%" />

4. Add Robot Root Prim 
    * (i.g., ur10 (defaultPrime)) <br>
  
    <img src="../img/t1_4.png" alt="t1_4" width="60%" />

    <img src="../img/t1_5.png" alt="t1_5" width="60%" />

5. Open Graph <br>
    <img src="../img/t1_6.png" alt="t1_6" width="60%" />

6. Click `JointCommandArray` and set the desired joint angles in `Value` field.
    <img src="../img/t1_7.png" alt="t1_7" width="60%" />

    * Try your robot joint movement!
    * (Turn on play button for watching real-time movement)
    <img src="../img/t1_8.gif" alt="t1_8" width="100%" />


# 2. Check Robot Collsiion Mesh
1. Turn on collision mesh view
    * Eye Icon > Show By Type > Physics > Colliders > All
    <img src="../img/t1_9.png" alt="t1_9" width="100%" />
    <br>
    <img src="../img/t1_10.png" alt="t1_9" width="100%" />
