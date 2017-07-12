from setuptools import setup
import sys
if sys.version_info < (3,3):
    sys.exit('Sorry, Python < 3.3 is not supported by mitmproxy.')

setup(name='aProxy',
      version = '0.0.1',
      description = 'iframe stuff for sdf',
      author = 'sdf',
      url = 'http://github.com/sdf-epfl/url_filter',
      install_requires=['bs4', 'mitmproxy'],
      scripts = ['aProxy.py'])
