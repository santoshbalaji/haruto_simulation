from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
  return LaunchDescription([
    # launch_ros.actions.Node(
    #   parameters=[
    #     get_package_share_directory("haruto_simulation") + '/config/localization.yaml'
    #   ],
    #     package='slam_toolbox',
    #     executable='localization_slam_toolbox_node',
    #     name='slam_toolbox',
    #     output='screen'
    #   ),
    launch_ros.actions.Node(
      parameters=[
        get_package_share_directory("haruto_simulation") + '/config/localization.yaml'
      ],
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        arguments=['--ros-args', '--log-level', 'debug']
      )
    ])
