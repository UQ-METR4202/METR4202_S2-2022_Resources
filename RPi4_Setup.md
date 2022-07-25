http://wiki.ros.org/noetic/Installation/Ubuntu
Setup your sources.list

Setup your computer to accept software from packages.ros.org.

```
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.l
```

Set up your keys

```
    sudo apt install curl # if you haven't already installed curl
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
# ROS Installation

First, make sure your Debian package index is up-to-date:

```
    sudo apt update
```

Desktop-Full Install: (Recommended) : Everything in Desktop plus 2D/3D simulators and 2D/3D perception packages

```
    sudo apt install ros-noetic-desktop-full
```
    
# Bash

```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

# Initialise rosdep

```
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
```

# Install Fiducial Packages
```
sudo apt install ros-noetic-fiducials ros-noetic-fiducial-msgs
```

# Installing Ximea Software Package

```
sudo apt-get update && sudo apt-get install build-essential linux-headers-"$(uname -r)" 
```
Download the zip file from the XIMEA website
```
wget https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz
```
Unzip the file
```
tar xzf XIMEA_Linux_SP.tgz
```
Enter the package folder and install
```
cd package && ./install
```

Disable the USB memory limits
```
echo 0 | sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb
```
Place the following in */etc/security/limits.conf* to make the Ximea camera driver have real time priority
```
*               -       rtprio          0
@realtime       -       rtprio          81
*               -       nice            0
@realtime       -       nice            -16
```
Then add the current user to the group realtime
```
sudo groupadd realtime
sudo gpasswd -a $USER realtime
```

Create a catkin_workspace directory
```
mkdir cd -p ~/catkin_ws/src
```
Clone the Ximea ROS Camera Repository
```
git clone https://github.com/wavelab/ximea_ros_cam.git
```
Go back to the root of the catkin workspace
```
cd ~/catkin_ws
```
Make sure to setup your workspace
```
source devel/setup.sh
```
Download VSCode
```
wget https://update.code.visualstudio.com/1.69.2/linux-deb-arm64/stable
```
Install VSCode
```
sudo dpkg -i code_1.69.2-1658161440_arm64.deb
```
