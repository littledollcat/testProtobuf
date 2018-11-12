# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

setup(
        name='advantech',     
        version='1.0',   
        description='This is for protobuf used.',
        author='ElmaLee',  
        packages=['advantech'],
        install_requires=['protobuf>=3.6.1','pandas>=0.23.4'],
        python_requires='>=3.5',
        zip_safe=False       
)