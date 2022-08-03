# ROS Cheat Sheet
This is a cheat sheet of all the common ROS commands that you can use during the development of your robot.

## Nodes
```SH
# list all running nodes
rosnode list

# display information about the node
rosnode info <node>
```

## Topics
```SH
# list all topics
rostopic list

# display information about the topic
rostopic info <topic>

# display messages on the topic
rostopic echo <topic>

# display the frequency of the topic
rostopic hz <topic>

# publish messages to the topic
rostopic pub <topic> <msg> <data> [--rate <Hz>, --once]
# e.g., rostopic pub /my_topic std_msgs/Int64 "data: 1" --rate 100
# note: this can be very tricky due to yaml formatting in the command line, so just ask a tutor for help if it doesn't work
```

## Messages
```SH
# list all message types in your workspace
rosmsg list

# display information about the message type
rosmsg show <msg>