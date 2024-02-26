# 24.02.27
# Chanyoung Ahn

"""This script spawn a scene of quiz_scene.usd

.. code-block:: bash

    # Usage
    PYTHON_PATH tutorials/00_assets/spawn_scene.py
    
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

# import omni.usd

LOCAL_ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

class Test():
    def __init__(self):
        self._device = "cuda:0"        

    def init_simulation(self):
        self._scene = PhysicsContext(sim_params={"use_gpu_pipeline": True},
                                     device='cuda', backend='torch')
        self._scene.set_broadphase_type("GPU")
        self._scene.enable_gpu_dynamics(flag=True)
        self._scene.enable_ccd(flag=False)

    def main(self):        
        # setting init stage 
        path = os.path.join(LOCAL_ASSETS_DIR, 'quiz_scene.usd')
        open_stage(usd_path=path)
        
        world = World(stage_units_in_meters=1, backend='torch')
        
        world._physics_context.enable_gpu_dynamics(flag=True)
        self.stage = world.stage
        self.init_simulation()
        world.reset()

        while simulation_app.is_running():
            world.step(render=True)
            if world.is_playing():
                if world.current_time_step_index == 0:
                    world.reset()

            
                
if __name__ == "__main__":
    try:
        test = Test()
        test.main()
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        simulation_app.close()