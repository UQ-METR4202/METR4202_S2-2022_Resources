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
### Week 1: Workshop - Intro to ROS

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
# What are we using?
## ROS: Robot Operating System
### Not *quite* an 'operating system'
From **ros.org**:
"ROS is a set of software libraries and tools that help you build robot applications."

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
### Workshop 1a [PRA]
- Understand ROS **topics**, **publishers** and **subscribers**, and **msgs** for communicated packed data around in a modular and extensible way
- Understand **Raspberry Pis**, the **Linux** operating system, the **Python** language and how they fit with ROS
- Understand an overview of the **METR4202 project** this semester, what will be done and how these pracs help you
---

# What is ROS?
It stands for **Robot Operating System**

It is not an operating system :thinking: 

---
![](2021-07-24-19-28-37.png)
is a
### communication framework

---
# Robots are complicated
![](2021-07-24-19-39-03.png)

---
<!--class:  --> 
# ROS provides
- **Topics**, abstract channels on which to communicate data
- **Nodes**, programs which read or write data to topics 
- **Msg types**, the data structures associated with topics that define the format and contents of messages

So a node **publishes** or **subscribes** to data of a particular Msg type on a topic

---
# Raspberry Pi
If you don't already know what a Raspberry Pi is, it is a **single board computer**. It has an ARM architecture Cortex-A CPU and everything it needs as a computer is on a single PCB.

It runs the **Linux** operating system (usually) and is a fully featured computer. 

---
# Linux  ![size 10%](2021-07-24-19-50-00.png)
Linux is an **open-source** operating system. ROS is, for the most part, intimately linked to Linux (although you can get it to run on other OSes).

ROS hijacks the Linux "networking stack" for communication and usually assumes it's running on **Ubunutu**, a particular distribution of Linux. 

---
### A reference for learning software
### https://tinyurl.com/metr4202resources

---
## The big one
# The METR4202 Project
Cue relevant document
<style>
section.leftt h1, section.left h3, section.left p, section.left li, section.left ul {
  text-align: left;
}
section.left ul, section.left li {
    padding: 10;
    margin: 0;
}
section.big p, section.big ul {
  font-size: 50px;
  font-weight: 400;
}

section.smol ul {
  font-size: 35px;
  font-weight: 300;
}

</style>
