"""
AMGD Python package setup
"""

from setuptools import setup, find_packages
import os

# Read long description from README
def read_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="amgd-optimizer",  
    version="1.0.0",        
    author="Ibrahim Bakari",
    author_email="2020913072@ogr.cu.edu.tr",
    description="Adaptive Momentum Gradient Descent for Regularized Poisson Regression",
    long_description=read_long_description(),
    url="https://github.com/elbakari01/amgd-optimizer",  # ← Your repo URL
    project_urls={
        "Bug Tracker": "https://github.com/elbakari01/amgd-optimizer/issues",
        "Documentation": "https://amgd-optimizer.readthedocs.io/",
        "Source Code": "https://github.com/elbakari01/amgd-optimizer",
        "Paper": "https://arxiv.org/abs/your-paper-id"
    },
)

    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.812",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "sphinxcontrib-napoleon>=0.7",
            "matplotlib>=3.3",
        ],
        "examples": [
            "jupyter>=1.0",
            "seaborn>=0.11",
            "pandas>=1.3",
        ],
    },
    keywords="machine learning, optimization, poisson regression, regularization, sparse modeling",
    include_package_data=True,
    zip_safe=False,
)