import setuptools                                                         

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setuptools.setup(
    name="schema_matcher_api",
    version="0.0.1",
    author="ColumbusTech",
    author_email="columbustechio@gmail.com",
    description="Python API for Schema Matching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/columbustech/schema-matcher-api",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
