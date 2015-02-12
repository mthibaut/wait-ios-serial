#!/usr/bin/env python

from distutils.core import setup

setup(name='wait-ios-serial',
      version='1.0.7',
      url='https://github.com/mthibaut/wait-ios-serial',
      description='Wait for a Cisco IOS device to come up from boot',
      author='Maarten Thibaut',
      author_email='mthibaut@cisco.com',
      scripts=['scripts/wait-ios-login', 'scripts/wait-ios-serial'],
      install_requires=['pexpect']
)



