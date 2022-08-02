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

# Hello everyone! :robot:
Welcome to the METR4202 workshops!

---
# What are workshops about?
- Putting robotics theory into practice
- Implementing equations and algorithms in code
- Learning about frameworks for robotics (e.g. ROS)
- Making progress on the robotics team project



--- 
# Overall Learning Objectives
- **LO-1**: To understand how to use ROS effectively do design modular robotic systems
- **LO-2**: To be able to design a simple robotic system for application in an automated task
- **LO-3**: To be able to program a robotic system to algorithmically plan movements to execute a task effectively

---
# LO-1: ROS
  - **LO-1.1**: To be able to understand basic concepts in ROS (e.g. nodes, topics, messages, services, actions)
  - **LO-1.2**: To be able to *use* common robotics libraries and tools in ROS
  - **LO-1.3**: To be able to write robotics libraries for use in the team project
  - **LO-1.4**: To be able to explain how the modular parts of a robot system communicate with each other

---

# LO-2: 
- **LO-2**: To be able to design a simple robotic system and apply as a method of automating a process
  - **LO-2.1**: To understand how the robot design, and configuration of links, joints and actuators affects the reachability and manipulability of the end-effector
  - **LO-2.1**: To understand how the design and component selection of the robot affects the dynamics and control of the robot.
  - **LO-2.3**: To understand how sensor (e.g. camera) selection and placement affects robot perception

---
# LO-3: 
  - **LO-3.1**: To understand how control algorithms can be used in a practical robotic system
  - **LO-3.2**: To demonstrate how motion planning can be integrated into the robot motion pipeline
  - **LO-3.3**: To demonstrate how basic image sensing, processing and computer vision techniques can be used by the robot to sense the environment
  
---

## Learning Objectives
### Practical 1
- Understand ROS **topics**, **publishers** and **subscribers**, and **msgs** for communicated packed data around in a modular and extensible way
- Understand **Raspberry Pis**, the **Linux** operating system, the **Python** language and how they fit with ROS
- Understand an overview of the **METR4202 project** this semester, what will be done and how these pracs help you

---
# What are we using?
## ROS: Robot Operating System
### Not *quite* an 'operating system'
From **ros.org**:
"ROS is a set of software libraries and tools that help you build robot applications."

---

# What ROS is *not*:
It stands for **Robot Operating System**
But, it is *not* an operating system :thinking: 

---


# But what *is* ROS?

---
![](ros.png)
is a
### communication framework

---
# Robots are complicated
![](robotics.png)

---

# ROS provides
- **Topics**, abstract channels on which to communicate data
- **Nodes**, programs which read or write data to topics 
- **Msg types**, the data structures associated with topics that define the format and contents of messages

So a node **publishes** or **subscribes** to data of a particular Msg type on a topic

---

# Raspberry Pi
![width:200px](rpi.png)
If you don't already know what a Raspberry Pi is, it is a **single board computer**. It has an ARM architecture Cortex-A CPU and everything it needs as a computer is on a single PCB.

It runs **Linux**-based operating systems (usually) and is a fully featured computer. 

---
# Linux
![width:100px](tux.png)
Linux is an **open-source** operating system. ROS is, for the most part, intimately linked to Linux (although you can get it to run on other OSes).

ROS hijacks the Linux "networking stack" for communication and usually assumes it's running on **Ubuntu**, a particular distribution of Linux. 

---
### A reference for learning software
### https://tinyurl.com/metr4202resources

---
## The big one
# The METR4202 Project

---

## But that's for another time.
