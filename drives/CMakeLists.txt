cmake_minimum_required(VERSION 2.8.3)
project(drives)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

catkin_python_setup()

add_message_files(
   FILES
   MotorCommand.msg
   MotionCommand.msg
)

generate_messages(
    DEPENDENCIES
    std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
   nodes/test_node
   scripts/motion_control
   scripts/motion_command_generator
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
