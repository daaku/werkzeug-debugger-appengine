try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Werkzeug Debugger AppEngine',
    version='0.1',
    url='https://github.com/nshah/werkzeug-debugger-appengine',
    license='BSD',
    author='Naitik Shah',
    author_email='n@daaku.org',
    description='Some patches.',
    long_description='Makes the debugger work in app engine.',
    packages=['werkzeug_debugger_appengine'],
    platforms='any'
)
