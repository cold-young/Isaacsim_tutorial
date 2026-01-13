![IsaacSim tutorial](img/title.png)

# Isaacsim tutorial 

[![IsaacSim](https://img.shields.io/badge/IsaacSim-5.1.0-silver.svg)](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://docs.python.org/3/whatsnew/3.11.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/22.04/)


Contributor: [Chanyoung Ahn](https://github.com/cold-young) 

**IsaacSim tutorial** is Isaacsim examples for everyone.  

## Isaac Sim 5.1.0 version
- Please, check `main` and `sim-5.1.0` branch for Isaac Sim 5.1.0 version tutorial!

### Installation
0. Make your own virtual environment (optional but recommended)

	```shell
	conda create -n [ENV] python=3.11 -y
	conda activate [ENV]
	pip install torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
	```
1. Install Isaac Sim 5.1.0 pip package 

    ```shell
    pip install "isaacsim[all,extscache]==5.1.0" --extra-index-url https://pypi.nvidia.com

    # Varifying the Isaac Sim installation
    isaacsim
    ```

## Tutorials
* Add your urdf with Isaac Sim GUI: [[Link]](./docs/Add_your_urdf.md)

## Isaac Sim 4.2.0 version
- Please, check `sim-4.2.0` branch for Isaac Sim 4.2.0 version tutorial.
- **Supplymentary files**: [Tutorial_DAY1 (KOR)](https://drive.google.com/file/d/1TtW2xgF41CknZzR0cW_nWjrUoT75iXrx/view?usp=sharing)


## Citation

```text
@misc{coldyoung2024isaac-tutorial,
	author = {Chanyoung Ahn},
	title = {Isaacsim_tutorial},
	year = {2024-2026},
}
```
