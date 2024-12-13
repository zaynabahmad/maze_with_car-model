from setuptools import find_packages, setup

package_name = 'maze_ros2_gz'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.launch.py']),
    ],
    install_requires=['setuptools', 'ros2pkg', 'ament_cmake', 'colcon-common-extensions'],
    zip_safe=True,
    maintainer='zaynap',
    maintainer_email='zozaahmad203@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

