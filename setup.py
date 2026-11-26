import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yohei Sato',
    maintainer_email='youpeyi1110@icloud.com',
    description='Package for practice',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',      #talker.pyのmain関数をtalkerという名前で
            'listener = mypkg.listener:main', #後で使うので書いておいてコメントアウト
        ],
    },
)
