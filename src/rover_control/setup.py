from setuptools import setup

package_name = 'rover_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='waseem',
    maintainer_email='waseem@todo.todo',
    description='Rover control package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_cmd_node = rover_control.serial_cmd_node:main',
            'keyboard_control = rover_control.keyboard_control:main',   
        ],
    },
)
