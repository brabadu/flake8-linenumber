import setuptools

requires = [
    "flake8 > 3.0.0",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flake8_linenumber",
    license="MIT",
    version="0.1.8",
    description="flake8 plugin to limit line number in a module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Boryslav Larin",
    author_email="brabadu@gmail.com",
    url="https://github.com/brabadu/flake8-linenumber",
    py_modules=['flake8_linenumber'],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'L001 = flake8_linenumber:LineNumberPlugin',
        ]
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
