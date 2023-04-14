# Supplemental Information


## About Me

* Eric Snow
* twitter: @ericsnowcrntly
* github: @ericsnowcurrently
* linkedin: @ericsnowcurrently

history:

* 2006 - started using Python
* 2008 - started getting involved in the Python community
* 2012 - became a Python core developer

(For more info, see ../about-me.md.)


# Multi-Core Python Project History

preliminary work:

* 2014 - determined to solve Python's multi-core story; started research
* 2015 - settled on a plan
* 2017 - landed (Nick Coghlan's) PEP 432 internal implementation (from 2012)
* 2019 - PEP 587 (replaced PEP 432, sort of)

other things impacting momentum and throughput:

* 2014-2016 - also working on PEPs 468/520 and C OrderedDict
* 2017 - new job at Microsoft; get 20% time for OSS (December)
* 2018 - governance discussions stop most progress
* 2021 - part of inaugural "faster-cpython" team with Guido at Microsoft (March)

the GIL:

* ???? - new GIL implementation
* ???? - first real attempt to remove GIL
* ???? - gilectomy
* ???? - "no-gil"
* 2022 - PEP 703

extension module isolation:

* 2007 - PEP 3121
* 2015 - PEP 489 accepted
* 2016 - PEP 573
* 2020 - PEP 630
* ???? - porting stdlib to multi-phase init
* 2022 - PEP 687

interpreter isolation and per-interpreter GIL:

* ???? - support for multiple interpreters added (`PyInterpreterState`)
* ???? - GILState API added
* ...
* 2017 - added `_PyRuntimeState` (and Includes/internal/)
* 2018 - moved GC and other state to `PyInterpreterState`
* ...
* 2020 - added c-analyzer
* 2022 - PEP 683
* 2022 - PEP 684
* 2022 - finished globals consolidation
* 2023 - started working on per-interpreter GIL full-time
* 2023 - finished interpreter isolation

new stdlib module:

* ...
* 2017 - opened PEP 554
* 2018 - added `_xxsubinterpreters` module (PEP 554 low-level implementation)
* ...


## About the GIL

...


## About Interpreters

...


## Concurrency Examples

...


## Parallelism Examples

...


## Isolating Extension Modules

high-level concerns:

* static types -> heap types
* mutable C variables -> module state  (includes all Python objects)
* update module init func to multi-phase init
* guard global data in C libraries

...

Resources:

* https://docs.python.org/3/howto/isolating-extensions.html
* https://peps.python.org/pep-0630/
