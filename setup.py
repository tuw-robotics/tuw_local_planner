from setuptools import setup

package_name = 'tuw_local_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Markus Bader',
    maintainer_email='markus.bader@tuwien.ac.at',
    description='Local Planner',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'dummy = tuw_local_planner.dummy:main',
        ],
    },
)
