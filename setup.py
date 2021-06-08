try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='ApiDjango',
    packages=[
        'Api',
        'ApiDjango',
        'Api.migrations',
    ],
)
