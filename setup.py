import setuptools

with open("readme.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="CodeKit",
    version="0.3",
    author="ErickRen",
    author_email="erickren2022@outlook.com",
    description="Codekit provides functions and decorators to assist developers in coding.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ErickRen2023/CodeKit",
    packages=setuptools.find_packages(),
    install_requires=[''],
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)