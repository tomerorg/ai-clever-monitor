
from setuptools import setup, find_packages

setup(
    name="ai-clever-monitor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Python ai monitor with SQLAlchemy and NumPy and Pytest",
    keywords="ai-clever-monitor, python",
    url="",
)
