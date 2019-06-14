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

setuptools.setup(
    name='annie-server',
    version='0.0.1',
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
        "filehandlers<=1.2",
        "lcbools>=1.0.2"
    ]
)
