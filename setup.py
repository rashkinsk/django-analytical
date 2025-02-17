"""
Packaging setup for django-analytical.
"""

from pathlib import Path

from setuptools import setup

import analytical as package


def read_file(filename):
    """Read a text file and return its contents."""
    project_home = Path(__file__).parent.resolve()
    file_path = project_home / filename
    return file_path.read_text(encoding="utf-8")


setup(
    name='django-analytical',
    version=package.__version__ + "+rashkinsk",
    description=package.__doc__.strip(),
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    author=package.__author__,
    author_email=package.__email__,
    packages=[
        'analytical',
        'analytical.templatetags',
    ],
    keywords=[
        'django',
        'analytics',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    platforms=['any'],
    url='https://github.com/rashkinsk/django-analytical',
    download_url='https://github.com/rashkinsk/django-analytical/archive/main.zip',
    project_urls={
        'Documentation': 'https://django-analytical.readthedocs.io/',
    },
)
