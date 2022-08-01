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


<!--_class: invert -->
# Welcome to Prac 3 :robot:
##### Signed up for transformers, got transformation matrices 
## :frowning:

---
### Learning Objectives - Prac 3
- Learn **transformation matrices** and how they relate to poses
- Learn how transformation matrices are communicated in ROS through **the TF system** and how they can be visualised using rqt
- Write a **TF broadcaster** for forward kinematics of a simple arm **using Denavit-Hartenberg parameters**