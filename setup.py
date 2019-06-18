"""
Annie Modified MIT License

Copyright (c) 2019-present year Reece Dunham and the Annie Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and/or distribute
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. SELLING THE SOFTWARE IS ALSO NOT ALLOWED WITHOUT WRITTEN PERMISSION
FROM THE ANNIE TEAM.
"""

import setuptools

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Unix",
    "Operating System :: Other OS",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Topic :: System",
    "Topic :: Terminals",
    "Topic :: Text Processing",
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP :: WSGI",
    "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Software Distribution",
    "Development Status :: 4 - Beta",
    "Framework :: IDLE",
    "Framework :: Flask",
    "Natural Language :: English",
    "Environment :: Web Environment"
]

URLs = \
    {
        "Bug Tracker": "https://github.com/annieapp/annie/issues",
        "Documentation": "https://docs.annieapp.co",
        "Source Code": "https://github.com/annieapp/annie",
        "License": "https://github.com/annieapp/annie/blob/master/LICENSE",
    }

setuptools.setup(
    name='annie-server',
    version='1.2.1',
    author="Annie Team",
    description="Annie Server",
    license="See https://github.com/annieapp/annie/blob/master/LICENSE",
    url="https://annieapp.co",
    author_email="me@rdil.rocks",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask==1.0.3",
        "lcbools>=1.0.2"
    ],
    classifiers=CLASSIFIERS,
    project_urls=URLs,
    long_description="See https://annieapp.co",
    long_description_content_type="text/markdown"
)
