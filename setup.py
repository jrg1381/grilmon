from distutils.core import setup

setup(
    name='grilmon',
    version='1.0.0',
    packages=[''],
    package_dir={'': 'grilmon'},
    url='https://github.com/jrg1381/grilmon',
    license='GNU General Public License v3.0',
    author='jrg',
    author_email='spam@example.com',
    description='Simple remote monitoring UI', requires=['psutil', 'flask']
)
