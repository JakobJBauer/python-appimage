import os
import setuptools

from python_appimage.utils.deps import ensure_excludelist


CLASSIFIERS = '''\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Programming Language :: Python
Topic :: Software Development
Operating System :: POSIX :: Linux
'''


with open('README.md') as f:
    long_description = f.read()


def get_version():
    from python_appimage.version import version
    return version


def get_package_data():
    '''Get the list of package data
    '''
    ensure_excludelist()

    prefix = os.path.dirname(__file__) or '.'
    return ['data/' + file_
            for file_ in os.listdir(prefix + '/python_appimage/data')]


setuptools.setup(
    name = 'python_appimage',
    version = get_version(),
    author = 'Valentin Niess',
    author_email = 'valentin.niess@gmail.com',
    description = 'Appimage releases of Python',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/niess/python-appimage',
    download_url = 'https://pypi.python.org/pypi/python-appimage',
    project_urls = {
        'Bug Tracker' : 'https://github.com/niess/python-appimage/issues',
        'Source Code' : 'https://github.com/niess/python-appimage',
    },
    packages = setuptools.find_packages(),
    classifiers = [s for s in CLASSIFIERS.split(os.linesep) if s.strip()],
    license = 'GPLv3',
    platforms = ['Linux'],
    python_requires = '>=2.7',
    include_package_data = True,
    package_data = {'': get_package_data()},
    entry_points = {
        'console_scripts' : (
            'python-appimage = python_appimage.__main__:main',)
    }
)
