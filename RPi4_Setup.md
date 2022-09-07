# Introduction
The Raspberry Pi Model 4B comes with a fresh install of Ubuntu MATE 20.04.
In order to get the required functionality for the project, you will need to setup some things on the RPi4.
This includes installing relevant libraries, drivers and tools.

In the project you will need the following:
- ROS Noetic
- XIMEA Camera Spftware
- Dynamixel Software
- Camera Calibration Libraries
- Aruco Tag Detection Libraries

The following document will cover the required steps to get these to work on the RPi4.
Of course, these steps should also work on any machine running Ubuntu 20.04, with minor differences.

# Contents
- [1 Setting up ROS Noetic](1-setting-up-ros-noetic)

# 1 Setting up ROS Noetic

The following instructions can also be found on the ROS wiki [here](http://wiki.ros.org/noetic/Installation/Ubuntu).

## 1.1 Setting up your sources and keys

Setup your computer to accept software from packages.ros.org.

```console
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Set up your keys

```console
sudo apt install -y curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
#  1.2 Installing ROS Noetic (Full Desktop)
First, make sure your Debian package index is up-to-date:
```console
sudo apt update
```

Desktop-Full Install: (Recommended) : Everything in Desktop plus 2D/3D simulators and 2D/3D perception packages

```console
sudo apt install -y ros-noetic-desktop-full
```
    
# 1.3 Setting up the ROS Environment

If you would like to have ROS automatically setup when you open a terminal use these commands:
```console
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
bash
```
Otherwise, if you would like to have a shortcut command (alias) for running the environment setup, use these commands:

```console
echo "alias noetic='source /opt/ros/noetic/setup.bash'" >> ~/.bash_aliases
bash
```

# 1.4 Setting up dependencies for packages
The following command will install tools for handling dependencies.
```console
sudo apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```
Install Python ROSdep with the following command:
```console
sudo rosdep init
rosdep update
```

# Install Fiducial Packages
```console
sudo apt install -y ros-noetic-fiducials ros-noetic-fiducial-msgs
```

# Installing Ximea Software Package
```console
sudo apt-get update && sudo apt-get install -y build-essential linux-headers-"$(uname -r)" 
```
Download the zip file from the XIMEA website
```console
wget https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz
```
Unzip the file
```console
tar xzf XIMEA_Linux_SP.tgz
```
Enter the package folder and install
```console
cd package && ./install
```

Disable the USB memory limits
```console
echo 0 | sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb
```
Run the following to make the Ximea camera driver have real time priority
```console
echo "*               -       rtprio          0
@realtime       -       rtprio          81
*               -       nice            0
@realtime       -       nice            -16" | sudo tee -a /etc/security/limits.conf
```
Then add the current user to the group realtime
```console
sudo groupadd realtime
sudo gpasswd -a $USER realtime
```

Create a catkin_workspace directory
```console
mkdir -p ~/catkin_ws/src
```

Go back to the root of the catkin workspace
```console
cd ~/catkin_ws/src
```

Clone the Ximea ROS Camera Repository
```console
git clone https://github.com/wavelab/ximea_ros_cam.git
```

Make the catkin workspace
```console
cd ~/catkin_ws
catkin_make
```

Make sure to setup your workspace
```console
source devel/setup.bash
```

```console
cd ~/Downloads
```

Download VSCode
```console
wget -O code_arm64.deb https://update.code.visualstudio.com/1.69.2/linux-deb-arm64/stable
```
Install VSCode
```console
sudo dpkg -i code_arm64.deb
```


# Dynamixel Setup

Install Dynamixel SDK for ROS
```console
sudo apt install ros-noetic-dynamixel-sdk
```

Clone and build Dynamixel interface
```console
cd ~/catkin_ws/src
git clone https://github.com/UQ-METR4202/dynamixel_interface
git clone https://github.com/UQ-METR4202/dynamixel_slider
cd ~/catkin_ws
catkin build
```
## Error can't open port
Run the following commands and REBOOT.
```console
sudo usermod -a -G dialout $USER
```

## Error can't ping ID #
Ensure the above commands are run. DO NOT CLONE THE CSIRO-ROBOTICS dynamixel_interface.
