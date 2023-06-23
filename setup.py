from setuptools import setup


def get_version() -> str:
    """
    read version from VERSION file
    """
    version = '0.1.0'
    version = exec(open("geometrical_layout/version.py").read())
    return version


setup(
    name='geometrical-layout',
    version=get_version(),       
    description='This client library is designed to support the geometrical-layout'
                'geometrical-layout help query endpoints of the "Dowell Geometrical Layout of Big Data API"',
    author='geometrical-layout',
    maintainer='Abdullahi Abdulwasiu',
    maintainer_email='abdullahiabdulwasiu1@gmail.com',
    url='https://github.com/DoWellUXLab/DoWell-Geometrical-layout-of-Big-Data',
    license='Apache',
    packages=["geometrical_layout"],
    package_dir={'': 'geometrical_layout'},
    long_description=open("README.md").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['requests'],
)
