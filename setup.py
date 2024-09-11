from setuptools import setup, find_packages

setup(
    name='ml-distance',
    version='0.0.1',
    author='One Octadion',
    author_email='octadion.ai@gmail.com',
    description='Library calculating distances, converted from ml-distance JS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/octadion/ml-distance',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
    ],
    scripts=['scripts/similarity.py'],
)
