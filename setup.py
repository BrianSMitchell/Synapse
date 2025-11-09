from setuptools import setup, find_packages

setup(
    name="synapse",
    version="0.1.0",
    description="A programming language for emergent AI intelligence",
    author="xAI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "antlr4-python3-runtime==4.13.1",
        "numpy==1.26.4",
        "sympy==1.12",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "synapse=synapse.repl:main",
        ],
    },
)
