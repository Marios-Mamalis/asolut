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
    install_requires=['nltk', 'inflect', 'numpy', 'plotly', 'pandas', 'eel'],
    project_urls={  # Optional
        "Author's Linkedin": 'https://www.linkedin.com/in/marios-mamalis/',
        'Source': 'https://github.com/Marios-Mamalis/asolut',
    },
    version='1.1.2',
    keywords='word frequency synonyms',
    include_package_data=True,
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),
    package_data={
        'sample': ['web/main_js.js', 'web/main_css.css', 'web/main.html',
                   'web/images/que.svg', 'web/images/logo.png', 'web/images/loadinggear.svg', 'web/images/gear.svg',
                   'web/images/favicon.ico', 'web/images/arr.svg',
                   'web/fonts/LICENSE.txt', 'web/fonts/OpenSans-Light.ttf', 'web/fonts/OpenSans-Regular.ttf',
                   'web/fonts/OpenSans-SemiBold.ttf']
    },
)
