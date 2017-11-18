from setuptools import setup
setup(
    name="isort",
    version='0.1',
    py_modules=['isort'],
    install_requires=[
        'Click',
        'Clarifai',
    ],
    entry_points='''
        [console_scripts]
        isort=isort:quality
    ''',
)