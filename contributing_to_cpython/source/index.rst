
Contributing to CPython
=======================

So you want to contribute to CPython?

Getting Set Up
==============


CPython Development Dependencies
--------------------------------

``sudo apt-get build-dep python3-dev``  (<100 MB)

or

* build-essential (debian/ubuntu)
* python3-all-dev (debian/ubuntu)

optional:
* libz-dev
* tk-dev
* libreadline5-dev
* libncursesw5-dev
* libssl-dev
* libgdbm-dev
* libsqlite3-dev
* libbz2-dev
* libdb-dev
* libc6-dev


Dev-in-a-box
------------

http://hg.python.org/devinabox/file/default/make_a_box.py
http://hg.python.org/devinabox/file/default/build_cpython.py


Building CPython
================

``./configure --with-pydebug --enable-ipv6 --prefix=/opt/python3.3``
``make -j``


Testing CPython
===============

``./python -bb -E -Wd -m test -r -w -Wd -uall -G``

Roll Credits
============

| Eric Snow
| ericsnowcurrently@gmail.com
| https://bitbucket.org/ericsnowcurrently/presentations

References:

| https://bitbucket.org/ericsnowcurrently/upug-cpython/
| http://docs.python.org/devguide/
| http://hg.python.org/devinabox/
| http://www.julython.org/
| http://www.debian.org/doc/packaging-manuals/python-policy/ap-build_dependencies.html
