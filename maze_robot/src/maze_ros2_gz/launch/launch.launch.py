from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess

import os


def generate_launch_description():
    # gazebo_model_sdf = LaunchConfiguration('gazebo_model_sdf', default='../../../maze/model.sdf')
    # maze_model_path = os.path.join(get_package_share_directory('maze_ros2_gz'), 'maze', 'model.sdf')
    package_dir = os.getenv('AMENT_PREFIX_PATH').split(':')[0]
    print(package_dir)
    # model_path = os.path.join(package_dir, '..', 'maze_ros2_gz', 'maze')
    model_path = ('/home/zaynap/maze_with_car-model/maze_robot/src/maze_ros2_gz/maze')
    
    return LaunchDescription([
        # Gazebo Ignition Simulation
           ExecuteProcess(
            cmd=[
                'ign',
                'gazebo',
                # '--render-engine', 'ogre2',
                os.path.join(model_path, 'model.sdf')
            ],
            output='screen',
            name='gazebo'
        ),

        # /cmd_vel (Ackermann Steering)
        # Node(
        #     package='ros_gz_bridge',
        #     executable='parameter_bridge',
        #     arguments=[
        #         '/cmd_vel@geometry_msgs/msg/Twist[ignition.msgs.Twist]'
        #     ],
        #     output='screen'
        # ),

        # # Camera Image Topic
        # Node(
        #     package='ros_gz_bridge',
        #     executable='parameter_bridge',
        #     arguments=[
        #         '/front_camera@sensor_msgs/msg/Image[ignition.msgs.Image]',
        #         '/front_camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo]'
        #     ],
        #     output='screen'
        # ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/front_camera@sensor_msgs/msg/Image@ignition.msgs.Image',
                '/front_camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo',
                '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'
            ],
            output='screen'
        )


        


        # # World Control 
        # Node(
        #     package='ros_gz_bridge',
        #     executable='parameter_bridge',
        #     arguments=[
        #         '/world_control@std_msgs/msg/Bool[ignition.msgs.Boolean]'
        #     ],
        #     output='screen'
        # ),

        # # Simulation Statistics
        # Node(
        #     package='ros_gz_bridge',
        #     executable='parameter_bridge',
        #     arguments=[
        #         '/world_stats@std_msgs/msg/String[ignition.msgs.StringMsg]'
        #     ],
        #     output='screen'
        # )
    ])
