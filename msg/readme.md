# Messages
## This is where you define new message definitions.
## You will need to add the below to 
## package.xml:
<build_depend>message_generation</build_depend>
<run_depend>message_runtime</run_depend>
## CMakeLists.txt:
### Tell catkin to look for message_generation package.
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs
    message_generation # Add message_generation here, after the other packages.
)
### Tell catkin we're going to use messages at runtime.
catkin_package(
    CATKIN_DEPENDS message_runtime  # This will not be the only thing here.
)
### Tell catkin what message files we want to compile.
add_message_files(
    FILES
    Complex.msg
)
### Uncomment generate_messages() call and ensure required dependencies
generate_messages(
    DEPENDENCIES
    std_msgs
)

