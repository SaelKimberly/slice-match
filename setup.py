from pathlib import Path
from setuptools import setup, find_packages

README = Path('README.md').read_text()

setup_args = dict(
    name='slice-match',
    version='0.1.1',
    description='Simple class, that simplify usage of slices in __getitem__',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='SaelKimberly',
    author_email='sael.kimberly@yandex.ru',
    keywords=['Slice', 'Match', 'SliceMatch'],
    url='https://github.com/SaelKimberly/slice-match',
    download_url='https://pypi.org/project/slice-match/'
)


if __name__ == '__main__':
    setup(**setup_args)
