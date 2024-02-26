# 24.02.27
# Chanyoung Ahn

"""This script spawn a road and your robot car

.. code-block:: bash

    # Usage
    PYTHON_PATH tutorials/01_robots/move_robot.py
    
    # Debug
    Root folder must "ISAAC_SIM-*"
"""

from omni.isaac.kit import SimulationApp

# launch omniverse app
simulation_app = SimulationApp({"headless": False})

import numpy as np
import os
import torch
from omni.isaac.core import World
from omni.isaac.core.physics_context.physics_context import PhysicsContext
import omni.isaac.core.utils.prims as prim_utils
from omni.isaac.core.utils.stage import open_stage

from omni.isaac.core.articulations import ArticulationView
# import omni.usd

LOCAL_ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

class Test():
    def __init__(self):
        self._device = "cuda:0"        

    def init_simulation(self):
        self._scene = PhysicsContext(sim_params={"use_gpu_pipeline": False, 
                                                 "use_gpu": True, 
                                                 "device": "cpu", 
                                                 "use_flatcache": False})
        
        self._scene.set_broadphase_type("GPU")
        self._scene.enable_gpu_dynamics(flag=True)
        self._scene.enable_ccd(flag=False)

    def add_robot(self):
        # Add robot
        # Change usd_path of your asset' path
        prim_utils.create_prim("/World/Robot",
            usd_path=os.path.join(LOCAL_ASSETS_DIR, 'ex_robot.usd'), 
            translation=(0.,0.,0.01))  

        self.robot = ArticulationView(prim_paths_expr="/World/Robot")

        
    def main(self):        
        # setting init stage 
        path = os.path.join(LOCAL_ASSETS_DIR, 'road_scene.usd')
        open_stage(usd_path=path)
        
        world = World(stage_units_in_meters=1, backend='torch')
        
        world._physics_context.enable_gpu_dynamics(flag=True)
        self.stage = world.stage
        self.init_simulation()
        self.add_robot()
        
        world.scene.add(self.robot)
        world.reset()

        i=0
        while simulation_app.is_running():
            i+=1
            world.step(render=True)
            if world.is_playing():
                if world.current_time_step_index == 0:
                    world.reset()
            
            # Control your robot
            vel = torch.tensor([[20., 10.]])
            self.robot.set_joint_velocities(vel)
            
            if i % 100 == 0: 
                joint_pos = self.robot.get_joint_positions()
                joint_vel = self.robot.get_joint_velocities()
                robot_position, robot_ori = self.robot.get_world_poses()
                
                print("Robot State")
                print(f"Joint position :{joint_pos}, Joint velocity :{joint_vel}")
                print(f"Robot position :{robot_position}, Robot orientation :{robot_ori}")

            
                
if __name__ == "__main__":
    try:
        test = Test()
        test.main()
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        simulation_app.close()