from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mediaplanning',
  version='0.0.5',
  description='Python package for media planning',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/maazkhan86/mediaplanning',  
  author='Maaz A. Khan',
  author_email='maazkhan700@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='media planning digital online offline', 
  packages=find_packages(),
  install_requires=[''] 
)
