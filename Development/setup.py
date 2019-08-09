import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gurux_common",
    version="1.0.1",
    author="Gurux Ltd",
    author_email="gurux@gurux.org",
    description="Gurux common helpers for device commmunication.",
    long_description="Gurux common helpers for device commmunication.",
    long_description_content_type="text/markdown",
    url="https://github.com/gurux/gurux.common.python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)
