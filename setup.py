from setuptools import setup

setup(
    name='worldofshamim-cli',
    version='1.0',
    packages=['worldofshamim'],
    entry_points={
        'console_scripts': [
            'worldofshamim = worldofshamim.__main__:main',
            'worldofshamim init = worldofshamim.__main__:init'
        ]
    }
)
