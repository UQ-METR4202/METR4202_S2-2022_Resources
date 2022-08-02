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
# Welcome back :robot:
#### Prac 2: Electric Boogaloo

---

### Learning Objectives - Prac 2
- Setting up ROS and your **project structure**
- **Writing a ROS publisher/subscriber** node in Python
- Learning **different software components** of a **robot manipulator** system


--- 
# Writing a publisher
##### Lets write a publisher to publish position commands
Starting off with a new `publisher.py` file...
```python
import rospy # import ROS library

# The Msg type on this topic will be "Int32"
from std_msgs.msg import Int32
from random import randint
```

---
#### The actual publisher
```python
def publisher():
    """A function that encompasses publisher functionality"""
    # A publisher object that we can call `publish` on
    pub = rospy.Publisher('position', Int32, queue_size=10)
    # Tell ROS about the node
    rospy.init_node('position', anonymous=True) 
    rate = rospy.Rate(10) # Update information at 10hz

    while not rospy.is_shutdown():
        value = randint(-10, 10)
        rospy.loginfo(f"The velocity command is {value}")
        pub.publish(value)
        rate.sleep() # This loop will sleep until when it
                     # needs to to match 10 Hz 
```

---
### Finish it off
```python
# If this file is launched on its own 
# (and not imported as a library)
if __name__ == "__main__":
    # Run publisher, unless errors
    try: 
        publisher()
    except rospy.ROSInterruptException:
        ros.logerr("ROSInterruptException encountered")
```
---
### and tell CMake about our file
```Cmake
catkin_install_python(PROGRAMS scripts/publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```