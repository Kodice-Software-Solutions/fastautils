from setuptools import setup, find_packages

setup(
    author_email="efren.cabrera@kodice.dev",
    author="Efren Cabrera",
    install_requires=[
        "numpy"
    ],
    name="fasta",
    packages=find_packages(),
    python_requires=">=3.6",
    version="0.1.0"
)
