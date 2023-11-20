from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    ld = []

    package_name = "simple_robot_description"


    #  add gazebo plugin loader
    # load_plugin = ExecuteProcess(
    #     cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
    #     output='screen'
    # )

    gazebo_launch = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py']),
        launch_arguments={
            'world': PathJoinSubstitution([FindPackageShare(package_name), 'worlds', 'empty.world']),
            }.items()
    )

    simple_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'robot', '-x', '0.0', '-y', '0.0', '-z', '1.0',
                   '-file', PathJoinSubstitution([FindPackageShare(package_name),  'models', 'arm_1dof_model.urdf'])])

    # add joint_state_publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        arguments=[PathJoinSubstitution([FindPackageShare(package_name), 'models', 'arm_1dof_model.urdf'])])
    
    # add robot_state_publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        arguments=[PathJoinSubstitution([FindPackageShare(package_name), 'models', 'arm_1dof_model.urdf'])])

   

    cmjsb = Node(
                package="controller_manager",
                executable="spawner",
                name="cm_jsb",
                arguments=["joint_state_broadcaster",
                           "--controller-manager", "/controller_manager"],
                
            )
    cmjtc = Node(
                package="controller_manager",
                executable="spawner",
                name="cm_jtc",
                arguments=["joint_trajectory_controller",
                           "-c", "/controller_manager"]
            )


    
    # ld.append(load_plugin)
    ld.append(gazebo_launch)
    ld.append(simple_robot)

    ld.append(joint_state_publisher)
    ld.append(robot_state_publisher)

    # ld.append(cm)
    ld.append(cmjsb)
    ld.append(cmjtc)

    return LaunchDescription(ld)


# ros2 run controller_manager spawner joint_trajectory_controller