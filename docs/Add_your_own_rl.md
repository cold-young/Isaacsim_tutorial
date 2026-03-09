# Add your RL env 

2026.03.09 (Mon.) <br>
**Writer:** Chanyoung Ahn

**Reference:** [Link](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/create_direct_rl_env.html)


## Create Your own RL env in IsaacLab
* **Check:** 1) Download Isaacsim, 2) Download IsaacLab, 3) Make virtual conda env
* Please, activate your individual conda env! 
  
```shell
conda activate [YOUR_ENV_NAME]
cd ~/IsaacLab
git checkout release/2.3.0
```

## Add your Robot 
* Please, check [this tutorial](Add_your_urdf.md)

### Example: RL with KISTAR Hand

```shell
git clone https://github.com/KIST-PRIME-Lab/dex-urdf

cd ~/dex-urdf/robots/hands/kistar_hand
# copy & paste to your project asset folder! 
# don't paste below command.... (check correct path..)
cp ~/kistar_hand ~/IsaacLab/source/isaaclab_assets/isaaclab_assets
```

#### Add path 
```shell
# check below file, 
~/source/isaaclab_assets/isaaclab_assets/__init__.py
```
* Add `from .kistar_hand import *`


### In-hand Manipuation task with KISTAR Hand 
* copy & paste `~/source/isaaclab_tasks/direct/allegro_hand`
* change `__init__.py`

```python
gym.register(
    id="Isaac-[YOUR_TASK_NAME]-v0",
    entry_point=f"{inhand_task_entry}.inhand_manipulation_env:InHandManipulationEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.allegro_hand_env_cfg:AllegroHandEnvCfg",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:AllegroHandPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
    },
)
```

* Add custom assets path: `~/source/isaaclab/isaaclab/utils/assets.py`
```python
ISAACLAB_ASSETS_CUSTOM_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../..", 
        "isaaclab_assets/isaaclab_assets",
        "[YOUR_ASSET_FOLDER]", # e.g., kistar_hand
    )
)
```


* Change `~/allegro_hand/[env]_cfg.py`

```python
from isaacslab.utils.assets import ISAACLAB_ASSETS_CUSTOM_DIR
# robot
robot_cfg = ArticulationCfg(
    prim_path="/World/envs/env_.*/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_NUCLEUS_DIR}/kistar_hand.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            retain_accelerations=False,
            enable_gyroscopic_forces=False,
            angular_damping=0.01,
            max_linear_velocity=1000.0,
            max_angular_velocity=64 / math.pi * 180.0,
            max_depenetration_velocity=1000.0,
            max_contact_impulse=1e32,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
        ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.005, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        rot=(0.5, 0.5, -0.5, 0.5),
        joint_pos={".*":0.0},
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            effort_limit_sim=0.5,
            stiffness=3.0,
            damping=0.1,
            friction=0.01,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)

```



### Test your rl env.. 
```shell
conda activate [YOUR_ENV]
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
        --task "Isaac-[YOUR_TASK_NAME]-v0"\
        --num_envs 36
# --headless # turn off GUI
```