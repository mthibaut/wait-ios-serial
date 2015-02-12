#!/usr/bin/env python

from distutils.core import setup

setup(name='wait-ios-serial',
      version='1.0.6',
      url='https://github.com/mthibaut/wait-ios-serial',
      description='Wait for a Cisco IOS device to come up from boot',
      author='Maarten Thibaut',
      author_email='mthibaut@cisco.com',
      scripts=['scripts/wait-ios-serial', 'scripts/wait-ios-login'],
      install_requires=['pexpect']
)



