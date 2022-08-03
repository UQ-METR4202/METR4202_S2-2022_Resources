# ROS Cheat Sheet
This is a cheat sheet of all the common ROS commands that you can use during the development of your robot.

# Nodes
```SH
# list all running nodes
rosnode list

# display information about the node
rosnode info <node>
```
Nodes may have multiple publishers and subscribers.

# Topics
```SH
# list all topics
rostopic list

# display the message type of the topic
rostopic type <topic>

# display information about the topic
rostopic info <topic>

# display messages published to the topic
rostopic echo <topic>

# display the frequency of the topic's publish rate
rostopic hz <topic>

# publish messages to the topic
rostopic pub <topic> <msg> <data> [--rate <Hz>, --once]
# e.g., rostopic pub /my_topic std_msgs/Int64 "data: 1" --rate 100
# e.g., rostopic pub /new_topic geometry_msgs/Twist -- '[1, 2, 3]' '[4, 5, 6]'
# note: this can be very tricky due to yaml formatting in the command-line, so just ask a tutor for help if it doesn't work
```
By convention, a `/` character precedes all topic names.

Topics should only be bound to one message type.

# Messages
```SH
# list all message types in your workspace
rosmsg list

# display information about the message type
rosmsg show <message>
```
All default ROS message types follow the format `group_msgs/Type`. For example, `std_msgs/Int64` and `geometry_msgs/Pose`.

# Environment
```SH
# required to set up ROS master
roscore

# return to root workspace directory
roscd

# create package
catkin_create_package <package-name> [dependency1, dependency2, ...]

# compile packages
catkin_make # or
catkin build

# source workspace
source /opt/ros/noetic/setup.bash # once per terminal
source ./devel/setup.bash
```
Only one instance of the ROS master should be initialised.

Always compile packages in the root workspace directory. If new executables, launch files or config files are added, then you must source the workspace with `source devel/setup.bash`.

Hint: sourcing your underlay with `source /opt/ros/noetic/setup.bash` can be done automatically by adding the command in `~/.bashrc`.

# Running & Launching
```SH
# run the executable from the package
rosrun <package> <executable>
# e.g., rosrun rospy_tutorials talker.py

# launch using the launch file from the package
roslaunch <package> <launch-file>
# e.g., roslaunch rospy_tutorials talker_listener.launch
```
Launch files are written in XML and may run several executables at once.