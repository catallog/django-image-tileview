import os
import re
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(
        "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE
    ).group(1)

name = 'django-image-tileview'
description = 'Django Admin Image Tileview'
url = 'https://www.collabo.com.br'
author = 'Thomas Alexander Ewald'
author_email = 'thomas@collabo.com.br',
license = 'BSD'
package = 'tileview'
version = get_version(package)
install_requires = open('requirements.txt').read().split('\n')

setup(
    name=name,
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license=license,
    description=description,
    long_description=README,
    url=url,
    author=author,
    author_email=author_email,
    install_requires=install_requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)
