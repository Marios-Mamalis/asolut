from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asolut',
    description='A solution for the synonym problem in word frequency algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Marios-Mamalis/asolut',
    author='Marios Mamalis',
    author_email='ies16039@uom.edu.gr',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows',
        'Natural Language :: English'
    ],
    python_requires='>=3.7.3',
    install_requires=['nltk', 'inflect', 'numpy', 'plotly==4.6', 'pandas', 'eel>=0.11.0'],
    project_urls={  # Optional
        "Author's Linkedin": 'https://www.linkedin.com/in/marios-mamalis/',
        'Source': 'https://github.com/Marios-Mamalis/asolut',
    },
    version='1.2.12',
    keywords='word frequency synonyms',
    packages=['asolut'],
    include_package_data=True
)
