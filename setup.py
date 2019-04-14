import setuptools


setuptools.setup(
    name='morning',
    version='0.1',
    py_modules=['morning'],
    author="Pesko",
    author_email="peskoo@protonmail.com",
    description="CLI to now the weather",
    url="https://github.com/peskoo/morning-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        morning=morning:cli
        ''',
    )
