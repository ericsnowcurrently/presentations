# Isolating Extension Modules


## Resources:

* https://docs.python.org/3/howto/isolating-extensions.html
* https://peps.python.org/pep-0630/


## High-Level Concerns

* static types -> heap types
* mutable C variables -> module state  (includes all Python objects)
* update module init func to multi-phase init
* guard global data in C libraries

### Converting Static Types

...

### Module State

...

### Multi-Phase Init

...

### Dealing With External State

...
