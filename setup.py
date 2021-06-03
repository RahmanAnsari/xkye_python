from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'xkye',
    version = version,
    license = license,
    author = 'Rahman Ansari',
    author_email = 'iamrahmanansari@gmail.com',
    url = 'https://github.com/RahmanAnsari/',
    description = 'Official Python Standard Library for Xkye Language',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        # put packages here
    ],
    classifiers= [
        "Development Status :: 1 - Planning",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)
