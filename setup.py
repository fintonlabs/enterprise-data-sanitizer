from setuptools import setup, find_packages

setup(
    name='DataProcessor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas==1.3.3',
        'numpy==1.21.2',
        'scikit-learn==0.24.2'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python tool for cleaning, normalizing, and identifying inconsistencies in data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dataprocessor',
)