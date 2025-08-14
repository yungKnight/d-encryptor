from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="d-encryptor",
    version="0.1.0",
    author="Eniola Ajayi",
    author_email="badoknight1@gmail.com",
    description="A simple encryption/decryption tool using drift cipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yungKnight/d-encryptor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "d-encryptor=d_encryptor.__main__:main",
        ],
    },
)