import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymeleon",
    version="0.0.1",
    author="Konrad Mnich",
    author_email="konrad.mnich@gmail.com",
    description="A simple package to modify matplotlib graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KonradMnich/pymeleon",
    project_urls={
        "Bug Tracker": "https://github.com/KonradMnich/pymeleon/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)