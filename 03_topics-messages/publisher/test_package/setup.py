from setuptools import find_packages, setup

package_name = 'test_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='its-working-test-package-with-publish-node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_pub_node = test_package.test_pub_node:main'
        ],
    },
)
