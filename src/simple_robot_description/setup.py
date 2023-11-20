from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'simple_robot_description'

files = glob('models/*/*_model.xacro')
for file in files:
    cmd = 'ros2 run xacro xacro '+file+' > '+ file.replace('.xacro','.urdf')
    os.system(cmd)


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Include model and simulation files
        (os.path.join('share', package_name, 'models'), glob('models/*/*.urdf')),
        (os.path.join('share', package_name, 'models'), glob('models/*/*.xacro')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leo',
    maintainer_email='amanyamy@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
         'console_scripts': [
                'joint_commander = simple_robot_description.joint_commander:main',
        ],
    },
)

# # get the absolute path to the directory where this file is located
# cur_dir = os.path.dirname(os.path.abspath(__file__))
# # remove two directories from cur_dir
# package_dir = cur_dir[:cur_dir.rfind('/')]
# package_dir = package_dir[:package_dir.rfind('/')]
# # load the content of each of the
# file_paths = glob('../../install/simple_robot_description/share/simple_robot_description/models/*.urdf')
# # load each file
# for file_path in file_paths:
#     with open(file_path, 'r') as file:
#         file_content = file.read()
#         # replace the text $(find simple_robot_description) with the package path
#         file_content = file_content.replace('$(find simple_robot_description)', package_dir+'/install/simple_robot_description/share/simple_robot_description')
#         # write back to the compiled file
#         open(file_path, mode='w').write(file_content)

# file_paths = glob('../../install/simple_robot_description/share/simple_robot_description/models/*.xacro')
# # load each file
# for file_path in file_paths:
#     with open(file_path, 'r') as file:
#         file_content = file.read()
#         # replace the text $(find simple_robot_description) with the package path
#         file_content = file_content.replace('$(find simple_robot_description)', package_dir+'/install/simple_robot_description/share/simple_robot_description')
#         # write back to the compiled file
#         open(file_path, mode='w').write(file_content)