# Isolating Extension Modules


## Resources

how-to:

* https://docs.python.org/3/howto/isolating-extensions.html
* https://peps.python.org/pep-0630/

slides:

* https://docs.google.com/presentation/d/16x-MDia4DbFY6C4epqyHVKMPKjbhxFtODvU2CwS0g_Q/

other:

* https://peps.python.org/pep-0489/
* https://peps.python.org/pep-0573/
* https://peps.python.org/pep-0687/
* https://peps.python.org/pep-0697/


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
