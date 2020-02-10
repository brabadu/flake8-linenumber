import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_linenumber",
    license="MIT",
    version="0.1.1",
    description="flake8 plugin to limit line number in a module",
    author="Boryslav Larin",
    author_email="brabadu@gmail.com",
    url="https://gitlab.com/brabadu/flake8_linenumber",
    packages=setuptools.find_packages(),
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
