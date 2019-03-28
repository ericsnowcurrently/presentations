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
* 
* (Apr 19) present at MS-internal "Python Brownbag"
* 
* (May 3, 14:35) (Cleveland) present at PyCon
   * first day, fifth session (second after lunch)
   * 14:35, 30 minutes
   * 


*practice sessions*

==== ======== ========= ==========
 #    date    minutes   notes
==== ======== ========= ==========
 1.
 2.
 3.
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
  1       what is the GIL?
  2+      what is the GIL?
  3+      what is the GIL?
  4+      what is the GIL?
  5       costs of the GIL
  6       benefits of the GIL
  7       who does it really affect?
  8       so why does the GIL get such a bad wrap?
  9       working around the GIL: (C) extension modules
  0       working around the GIL: async
 10       past attempts to remove
 11+      past attempts to remove
 12       new C-API
 13+      new C-API
 14+      new C-API
 15+      new C-API
 16+      new C-API
 17+      new C-API
 18       subinterpreters
 19+      subinterpreters
 20+      subinterpreters
 21+      subinterpreters
 22+      subinterpreters
 23+      subinterpreters
 24+      subinterpreters
 25+      subinterpreters
 26+      subinterpreters
 27+      subinterpreters
 28+      subinterpreters
 29       other Python implementations
 30+      other Python implementations
======== ====================


Slides / Granular Outline
--------------------------

* title
* intro
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* Thanks!  Questions?
* Thanks!  Questions?  Resources


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
