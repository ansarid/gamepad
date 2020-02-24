import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='gamepad',
    version='0.0.1',
    description='My gamepad library',
    license='GNU General Public License v3.0',
    packages=setuptools.find_packages(),
    author='Daniyal Ansari',
    author_email='daniyal.s.ansari+pypi@gmail.com',
    url='https://github.com/ansarid/gamepad',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
