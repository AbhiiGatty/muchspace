from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

setup(name = 'muchspace',
      description = 'A CLI utility in python3 to calulate total disk space required for media links',
      long_description=README + '\n\n' + HISTORY,
      version = '0.1.7',
      url = 'https://github.com/Hitoshirenu/muchspace',
      download_url = 'https://github.com/Hitoshirenu/muchspace/archive/0.1.tar.gz',
      author = 'abhiigatty',
      author_email = 'abhiigatty@gmail.com',
      license = 'MIT',
      classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',   
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Filesystems',
        'Topic :: Software Development',
        'Topic :: Utilities',
      ],
      keywords = ['band width', 'disk-space', 'analyzer', 'cli', 'python3'],
      maintainer = 'abhiigatty',
      maintainer_email = 'abhiigatty@gmail.com',
      packages=find_packages(),
      install_requires = ['fire', 'requests'],
      entry_points = {
          'console_scripts': [
              'muchspace = muchspace.muchspace:main'
          ]
      }
)