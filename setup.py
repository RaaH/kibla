#! /usr/bin/python

from distutils.core import setup

doc_files = ['LICENSE-ar.txt', 'LICENSE-en', 'AUTHORS', 'ChangeLog', 'README']
data_files = [('share/doc/kibla', doc_files),]

setup(
      name='kibla',
      description='Account of the Qiblah',
      version=0.1,
      author='Ahmed Raghdi',
      author_email='asmaaarab@gmail.com',
      url='https://github.com/RaaH/kibla',
      license='Waqf License',
      platforms='Linux',
      py_modules=['kibla'],
      keywords=['Qiblah', 'Prayer', 'Makkah'],
      classifiers=['Programming Language :: Python',
                     'Operating System :: POSIX :: Linux',
                     'Development Status :: 4 - Beta']
      )
