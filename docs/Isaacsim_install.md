# IsaacSim Install

[![IsaacSim](https://img.shields.io/badge/IsaacSim-4.2.0-silver.svg)](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/20.04/)


Contributor: [Chanyoung Ahn](https://github.com/cold-young) 

# Installation
## IsaacSim
1. [Check](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/requirements.html#isaac-sim-requirements-isaac-sim-system) your machine meets the system requirements. 

2. Install [Isaacsim](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_workstation.html) (Download the Omniverse Launcher)

    ```shell
    cd ~/Download
    sudo chmod +x omniverse-launcher-linux.AppImage
    ```

    **Trouble Shooting:** </br>
    
    - Cannot Run AppImage ... [(Link)](https://itsfoss.com/cant-run-appimage-ubuntu/)

        If your Ubuntu version is 22.04 
        ```shell
        # Check ubuntu version
        lsb_release -a

        # Install libfuse2 (for ubuntu 22.04)
        sudo apt install libfuse2

        # Or install libuse2t64 (for ubuntu 24.04)
        sudo apt install libfuse2t64
        ```

3. Install Cache, Nucleus, VScode, IsaacSim, Isaac Sim Compatibility (Optional)

    **Trouble Shooting** </br>
    - IOMMOU on bare metal Issue ..in AMD CPU [(Link)](https://forums.developer.nvidia.com/t/isaac-sim-issue-with-iommu-on-bare-metal-despite-having-turned-it-off/278711)


## Athor Tools .. 
### Miniconda3+conda-forge (Caution) 
- Use of Anaconda’s Offerings at an organization of more than 200 employees requires a Business or Enterprise license..

- **Miniconda3+conda-forge** [(link)](https://www.codeit.kr/tutorials/150/miniconda-guide)
    - Install Miniconda3
    ```shell
    conda config --add channels conda-forge

    conda config --set channel_priority strict

    conda config --show channels
    ```
    **Trouble Shooting** </br>
    - 'conda'
    ```shell
    sudo vim ~/.bashrc 
    export PATH=/home/USER_NAME/miniconda3/bin:$PATH    
    ```

## Issac Lab 
- Install Isaac Lab [(Link)](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html#installing-isaac-sim)