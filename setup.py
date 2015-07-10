#!/usr/bin/env python
## begin license ##
#
# "Seecr Web Lib" provides web libraries for web development.
#
# Copyright (C) 2015 Seecr (Seek You Too B.V.) http://seecr.nl
# Copyright (C) 2015 Stichting Kennisnet http://www.kennisnet.nl
#
# This file is part of "Seecr Web Lib"
#
# "Seecr Web Lib" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Seecr Web Lib" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr Web Lib"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from distutils.core import setup

version = '$Version: 0.1.x$'[9:-1].strip()

from os import walk
from os.path import join

data_files = []
for path, dirs, files in walk('usr-share'):
    data_files.append((path.replace('usr-share', '/usr/share/seecr-web-lib'), [join(path, f) for f in files]))

packages = []
for path, dirs, files in walk('seecr'):
    if '__init__.py' in files:
        packagename = path.replace('/', '.')
        packages.append(packagename)

setup(
    name='seecr-web-lib',
    packages=packages,
    data_files=data_files,
    version=version,
    url='http://www.seecr.nl',
    author='Seecr',
    author_email='info@seecr.nl',
    description='Web libraries for web development',
    long_description='Provides javascript libraries and css for web development',
    platforms=['linux'],
)
