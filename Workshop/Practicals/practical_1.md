---
marp: true
theme: uncover
style: |
    :root {
    --color-background: #FFFFFF;
    --color-foreground: #8B2781;
    --color-highlight: #8B2781;
    --color-dimmed: #888888;
    }
    h1 {
      color: #51247A
    }
    h2 {
      color: #8B2781
    }
    h3 {
      color: #220033
    }
    section {
      font-size: 30px;
    }
paginate: true

---

# METR4202
## Robotics & Automation
### Week 1: Practical - Intro to ROS

---

### In Summary...
- ROS stands for **R**obot **O**perating **S**ystem
- It is a middleware for communicating between processes that independently perform tasks for your robot stack (e.g., sensing, decision-making, acting)
- As robot developers you will use ROS as a library inside your Python or C++ code
- It is recommended to get comfortable with BASH (terminal) to run ROS commands during development [(there is a cheat sheet in the METR4202 repository for your convenience)](https://github.com/UQ-METR4202/METR4202_S2-2022_Resources/blob/main/Workshop/Practicals/ros_cheat_sheet.md)

---

### Using the ROS Command-line
#### Prepare your Virtual Machine


---

### Exercise 1 (Together)
Create a publisher and echo the result in separate terminals.

*Terminal 1*
```SH
rostopic pub <topic> <msg> <data>
```

*Terminal 2*
```SH
rostopic echo <topic>
```

---

### Exercise 1 (Together)
Create a publisher and echo the result in separate terminals.

*Terminal 1*
```SH
rostopic pub /example_topic std_msgs/Int64 'data: 4'
```

*Terminal 2*
```SH
rostopic echo /example_topic
```

---

### Exercise 2 (Your turn)
Run the following command and try to publish to the node in a separate terminal.

*Terminal 1*
```SH
rosrun rospy_tutorials listener.py
```

*Terminal 2*
```SH
# Hint: Find out the topic name and message type the node subscribes to
```

---

### Exercise 2 (Your turn)
Run the following command and try to publish to the node in a separate terminal.

*Terminal 1*
```SH
rosrun rospy_tutorials listener.py
```

*Terminal 2*
```SH
rostopic pub /chatter std_msgs/String "data: hi"
```

---

### Exercise 3 (Challenge)
Run the following command. This will open a simulation window of a turtle. In a separate terminal, publish to the appropriate topic to spin the turtle at 50 rad/s.

*Terminal 1*
```SH
rosrun turtlesim turtlesim_node
```

*Terminal 2*
```SH
# Hint: You can fill out the data after entering the right topic by pressing <tab> twice
```

---

### Exercise 3 (Challenge)
Run the following command. This will open a simulation window of a turtle. In a separate terminal, publish to the appropriate topic to spin the turtle at 50 rad/s.

*Terminal 1*
```SH
rosrun turtlesim turtlesim_node
```

*Terminal 2*
```SH
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 50]'
```