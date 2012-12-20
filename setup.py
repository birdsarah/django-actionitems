from setuptools import setup, find_packages
import os


setup(
    author="Sarah Bird",
    author_email="sarah@aptivate.org",
    name='django-actionitems',
    version='1.1',
    description='Action items for Django',
    long_description=open(os.path.join(os.path.dirname(__file__),
        'README.md')).read(),
    url='https://github.com/birdsarah/django-actionitems/',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'django>=1.4',
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False
)
