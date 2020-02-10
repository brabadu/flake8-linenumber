flake8-linenumber
=================

Flake8 plugin to limit lines number in a module


Installation
------------

    $ pip install flake8-linenumber

Usage
-----

Add path to file and it's limit to your flake8 config (`.flake8` file by default)


```
linenumber =
    ./events.py=500
    ./handlers.py=1000
```
                        

Codes
-----
* ``L001`` Reports that logical line count has exceeded limit
