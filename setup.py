from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='muchspace',
      description='A CLI utility in python3 to calulate total disk space required for media links',
      long_description=long_description,
      version='0.1.0',
      url='https://github.com/Hitoshirenu/muchspace',
      author='abhiigatty',
      author_email='abhiigatty@gmail.com',
      license='MIT',
      classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Console",   
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Filesystems",
        "License :: OSI Approved :: MIT License"
      ],
      keywords=['band width', 'disk-space', 'analyzer', 'cli', 'python3'],
      maintainer='abhiigatty',
      maintainer_email='abhiigatty@gmail.com',
      packages=find_packages(),
      install_requires=['fire>=0.1.3', 'requests>=2.18.4'],
      entry_points={
          'console_scripts': [
              'muchspace = muchspace.main:run'
          ]
      }
)