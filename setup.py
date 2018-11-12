# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

setup(
        name='Test',     
        version='1.0',   
        description='This is a test of the setup',
        author='Elma',  
        packages=['testTest'],
        install_requires=['protobuf>=3.6.1']         
)