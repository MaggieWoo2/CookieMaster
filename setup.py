import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecl",
    version="0.0.0a0",
    author="MaggieWu",
    author_email="maggiewu@uchicago.edu",
    description="An experimental package for expert coding languages, by the University of Chicago Centre of Applied AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/smulla/cookiemaster",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["pandas"]
)
