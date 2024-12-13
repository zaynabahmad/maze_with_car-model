import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zaynap/maze_with_car-model/maze_robot/src/install/maze_ros2_gz'
