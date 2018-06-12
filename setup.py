from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

setup(name = 'muchspace',
      description = 'A CLI utility in python3 to calulate total disk space required for media links',
      long_description=README + '\n\n' + HISTORY,
      version = '0.3.2',
      url = 'https://github.com/Hitoshirenu/muchspace',
      download_url = 'https://github.com/Hitoshirenu/muchspace/archive/0.1.tar.gz',
      author = 'abhiigatty',
      author_email = 'abhiigatty@gmail.com',
      license = 'MIT',
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',   
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Logging',
        'Topic :: System :: Filesystems',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        'Topic :: Utilities',
      ],
      keywords = ['disk-space', 'analyzer', 'cli', 'python3', 'logging', 'link checking', 'link health'],
      maintainer = 'abhiigatty',
      maintainer_email = 'abhiigatty@gmail.com',
      packages=find_packages(),
      install_requires = [
          'fire',
          'requests',
          'more_itertools'],
      entry_points = {
          'console_scripts': [
              'muchspace = muchspace.muchspace:main'
          ]
      }
)