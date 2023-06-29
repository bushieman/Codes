## Robotics with ROS2, Arduino & Raspberry Pi
# 
$ ros2 run <package> <node> # Start a node. A node is any program that has access to ros functionalities and communications.
$ rqt_graph # A GUI for visualizing your connections

# Creating a ROS2 Workspace
Create a folder with src sub-folder
$ colcon build
Add the setup.bash script to your .bashrc file

# Creating packages
$ ros2 pkg create <package_name> --build-type ament_python --dependencies rclpy # Create your package inside the src folder for python development and add some dependencies.
A good practice is to create the package in the format <<robot_name><task>> e.g robot2.3_controller
$ colcon build # This will build from the src folder into the install folder

# Creating a ROS2 Node
Create a python file robot_node.py in the root folder as the __init__.py file
$ chmod +x robot_node.py # create an executable script

# Running the Node with ROS2
Add the following line inside the console_scripts list in setup.py, build with colcon then source the bashrc file
'test_node = <package_name>.<node>:<function>'

# AutoBuild
$ colcon build --symlink-install

# other commands
$ ros2 node list # show available nodes
$ ros2 node info <node_name> # show node details

# Topics
A topic is a communication between 2 or more nodes. Nodes can publish or subscribe to the topic.
$ ros2 topic list # show available topics
$ ros2 topic info <topic_name> # show topic details
$ ros2 topic echo <topic_name> # listen to a topic i.e create a subscriber
$ ros2 interface show <type> # show the type of data communicated through a topic
