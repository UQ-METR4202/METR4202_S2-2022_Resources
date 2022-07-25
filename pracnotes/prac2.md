---
marp: true
theme: uncover
header: METR4202 Prac 1
paginate: true
---

<!--_class: invert -->
# Welcome back :robot:
#### Prac 2: Electric Boogaloo

---
<!-- _backgroundColor: beige -->
### Learning Objectives - Prac 2
- Setting up ROS and your **project structure**
- **Writing a ROS publisher/subscriber** node in Python
- Learning **different software components** of a **robot manipulator** system


--- 
# Writing a publisher
<!-- class: invert-->
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
---
<!-- _backgroundColor: beige -->
<!-- class: default -->
## Different subtasks of a robot manipulator
Let's try and understand what is involved in making 


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
