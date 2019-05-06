PyCon 2019 Talk: "to GIL or not to GIL: the Future of Multi-Core (C)Python"
===========================================================================


Log of Time Spent
-----------------

* (2018 . .) submitted proposal on PyCon US 2018 website (same day as started?)
* (2019 Feb 12) talk accepted; tweeted about it
* (Feb 15) started prep
   * added time layout
   * started list of slides
* (Mar ?) decided to skip Q&A
* (Mar 28) more prep
   * summarize slide layout
   * update time layout
   * finish first half of slides list
* (Apr 15) flesh out slides
   * fill in more outline
   * start slide deck
* (Apr 16) work on slide deck
* (Apr 17) work on slide deck
* (Apr 18) finish first draft of slide deck
* (Apr 19)
   * review
   * walk-through
   * present at MS-internal "Python Brownbag"
* (Apr 20) looked at Gary Bernhardt's "How to Prepare a Talk" (www.deconstructconf.com/blog/how-to-prepare-a-talk)
* (Apr 27) ripped out superflous slides
* (May 2) re-structured "Context" part (with diagrams)
* 
* (May 3, 14:35) (Cleveland) present at PyCon
   * info
      * first day, fifth session (second after lunch)
      * 14:35, 30 minutes
      * opposing talks:
         * "Take Back the Web with GraphQL" - Robert Myers
         * "Everything at Once: Python's Many Concurrency Models" - Jess Shapiro
         * "Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting" - Łukasz Langa
         * "Wily Python: Writing simpler and more maintainable Python" - Anthony Shaw
         * "Programación para periodistas: el uso de Python en la extracción y análisis de reportajes" - Judite Macedo Cypreste
   * slides:  https://docs.google.com/presentation/d/1BuU6e-CKdZxDL5z9VBp19LAaIY8Ys2-jlcz-mD0Vr3c/
   * actual runtime:  27 minutes
   * reaction:  great


*practice sessions*

==== ======== ========= ==========
 #     date    minutes    notes
==== ======== ========= ==========
 1.   Apr 19   ~60       "MS Python Brownbag"
 2.   May 2    ~15
 3.   May 3    ~20
 4.
 5.
 6.
 7.
 8.
 9.
10.
...
==== ======== ========= ==========


Time Layout
------------

======== ====================
 minute   topic
======== ====================
  1       intro
  2+      what is the GIL? (context)
  3+      what is the GIL? (context)
  4+      what is the GIL? (context)
  5+      what is the GIL? (context)
  6+      what is the GIL?
  7+      what is the GIL?
  8       costs & benefits
  9       impact and perception
 10       working around the GIL
 11+      working around the GIL
 12       past attempts to remove
 13       other Python implementations
 14       new C-API
 15+      new C-API
 16+      new C-API
 17+      new C-API
 18+      new C-API
 19+      new C-API
 20       subinterpreters
 21+      subinterpreters
 22+      subinterpreters
 23+      subinterpreters
 24+      subinterpreters
 25+      subinterpreters
 26+      subinterpreters
 27+      subinterpreters
 28+      subinterpreters
 29+      subinterpreters
 30+      subinterpreters
======== ====================


Slide Structure / Layout
--------------------------

Per-slide:

* top: sliding global context; current section bold
* top: sliding section context; current slide title bold, double-size
* bottom-right: i/n slide number


Slides / Granular Outline
--------------------------

* title
* ? Ruby
* intro
* overall outline
* time layout
* ++++ the GIL! ++++
   * section outline
   * -- context --
      * overview of CPython's architecture
      * GC and refcounting
      * overview of the eval loop
      * what happens when a Python thread is created?
      * CPython runtime state that is shared by threads
   * -- what is the GIL? --
      * description
      * why?  race conditions on runtime state and objects
      * why global?
   * -- costs & benefits of the GIL --
      * list (multi-core parallelism, ???)
      * list (cheaper, low contention for global resources, simpler eval impl, simpler object/C-API impl)
   * -- effect and perception --
      * who does it really affect?
      * so why does the GIL get such a bad wrap?
   * -- working around the GIL
      * (C) extension modules
      * async
      * multiprocessing
   * -- past attempts to remove --
      * list(???, ???, Gilectomy)
      * other implementations (unladen swallow, ???)
* ++++ the Future! ++++
   * section outline
   * -- other Python implementations --
      * Jython
      * IronPython
      * PyPy
      * PyPy-STM
      * MicroPython
   * -- new C-API --
      * what's the problem?
      * drivers:  Victor, Steve, Neil
      * layers (Steve's proposal)
      * FFI (Brett)
      * opaque structs
      * compatibility
   * -- subinterpreters --
      * what are subinterpreters?
      * stop sharing the GIL
      * PEP 554
      * how-to
* Thanks!  Questions?
* Thanks!  Questions?  Resources

...

https://bit.ly/2ZmMJW0

https://docs.google.com/presentation/d/1_qbtSCAS9KhxVH77np106D0gq1wjHUxrVFHgZuxBupc


Proposal
---------

(#603)

*Description*

Why come to yet another talk about CPython's GIL? [1] Sure, we'll spend a little time on what it is, who it affects (and doesn't), and how to work around it. However, what you want to come hear is what the future holds for the GIL.

We'll take most of the time talking about life after the GIL! Come see what recent developments and ongoing work will allow us to either circumvent the GIL and get rid of it, unlocking true multi-core capability in Python code.

[1] In case you don't know, the GIL is a global lock that prevents multi-core parallelism in pure Python code. It has a controversial place in the community. Look it up (or come to this talk)! 

*Audience*

This talk is aimed at a number of broad groups which encompass most of the community:

* those interested in threads and parallelism
* anyone who wants to know some of the latest trends in CPython core development
* C-extension authors (and CPython embedders)
* anyone who's heard about how the GIL is Python's downfall :)

I will keep the talk relatively high-level. The pace will be quick but motivated beginners will be able to follow along. This isn't just a rehash of old info so even advanced users will have plenty to consider (including during the first part, about the GIL). By the end of the talk everyone will have a better understanding of the GIL and know about upcoming tools (e.g. PEP 554) that will help make it irrelevant. 

*Outline*

A. the GIL
  1. what is the GIL? (1 min)
  2. costs of the GIL (1 min)
  3. benefits of the GIL (1 min)
  4. who does it really affect? (1 min)
  5. so why does the GIL get such a bad wrap? (1 min)
  6. working around the GIL: (C) extension modules (1 min)
  7. working around the GIL: async (1 min)
B. the future
  1. past attempts to get rid of the GIL (2 min)
  2. current attempts: subinterpreters (8 min)
  3. current attempts: new C-API (6 min)
  4. other Python implementations (2 min)

For a 45 minute talk I'd spend a few more minutes on A.6 and A.7 (giving practical examples), an extra 10 minutes on B.2 (with practical subinterpreters examples), and the remaining couple of minutes on B.3.

*Additional notes*

PEP 554 is pretty relevant to this talk (especially section II.b). If the PEP isn't accepted in time for PyCon then I'll put a module on the cheeseshop that does the same thing. (I can provide an advance copy privately if desired.)

Other notes about me:

* given 3 talks at past PyCons
* one of the few Python core developer working extensively on the CPython runtime
* gave related talk at 2018 Language Summit

For details on the overall project (related to subinterpreters), see https://github.com/ericsnowcurrently/multi-core-python.

FWIW, I favor my other proposal, #325 ("Subinterpreters and You!") over this one. However, I'd be glad to give either (or both). They do overlap a bit but the other one has a more practical (and focused) subject matter. 
