import os

from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
  pkg_mapping = FindPackageShare(package='haruto_simulation').find('haruto_simulation')
 
  # Set the path to the mapping configuration file
  mapping_config_path = os.path.join(pkg_mapping, 'config', 'mapping.yaml')
  
  start_async_slam_toolbox_node = Node(
      parameters=[
        mapping_config_path,
        {'use_sim_time': True},
      ],
      package='slam_toolbox',
      executable='async_slam_toolbox_node',
      name='slam_toolbox',
      output='screen')

  ld = LaunchDescription()

  ld.add_action(start_async_slam_toolbox_node)

  return ld
