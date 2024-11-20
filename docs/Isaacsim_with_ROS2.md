# IsaacSim with ROS2

[![IsaacSim](https://img.shields.io/badge/IsaacSim-4.2.0-silver.svg)](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/22.04/)
[![ROS2](https://img.shields.io/badge/ROS2-Humble-green.svg)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)


Contributor: [Chanyoung Ahn](https://github.com/cold-young)

# Installation
## ROS 2 Humble
* Tested in Ubuntu 22.04 LTS + ROS 2 Humble for IsaacSim 4.2.0
1. [Check](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) Official Documentation!

    * Warning: Update `systemd` and `udev` packages!
2. Install desktop version

```shell
sudo apt install ros-humble-desktop
```

3. (Optional) Write down this command in `~/.bashrc`
```shell
vim ~/.bashrc

# write down below command
source /opt/ros/humble/setup.bash
```

4. (Optional) Install develop tools [(Link)](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html)

```shell
sudo apt update && sudo apt install -y \
python3-flake8-docstrings \
python3-pip \
python3-pytest-cov \
ros-dev-tools
```

```shell
sudo apt install -y \
python3-flake8-blind-except \
python3-flake8-builtins \
python3-flake8-class-newline \
python3-flake8-comprehensions \
python3-flake8-deprecated \
python3-flake8-import-order \
python3-flake8-quotes \
python3-pytest-repeat \
python3-pytest-rerunfailures
```


## Commands
```shell
# Get topic
ros2 topic echo /turtle1/cmd_vel
```

```shell
# Get topic delay time
ros2 topic delay /TOPIC_NAME
```

```shell
# Topic publish
ros2 topic_pub [TOPIC_NAME] [MSG_YTPE] "args"

 ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist \
 "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
```

```shell
# Topic Record 
ros2 bag record <topic_name1> <topic_name2>
ros2 bac info <FILE> 
```

```shell
# Ros bag play 
ros2 bag play <FILE>
```


## ROS2 + IsaacSim Extension
- ROS2 Installation Docs [Link](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_ros.html#ros-and-ros-2-installation)

### Trobleshooting

- **Setting Up Workspaces**: [Link](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_ros.html#isaac-ros-workspace)


```shell
colcon build 
```

- AttributeError: module`em` has no attribute 'BUFFERED_OPT' ~ 
    - Install `empy` 

    ```shell
    pip install empy==3.3.4
    ```