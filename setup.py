import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dire',
    version='0.1.0',
    author='Ken Youens-Clark',
    author_email='kyclark@gmail.com',
    description="Python equivalent of Perl's warn and die functions",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kyclark/dire',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
