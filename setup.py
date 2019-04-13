from setuptools import setup

setup(
    name='morning',
    version='0.1',
    py_modules=['morning'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        morning=morning:cli
        ''',
    )
