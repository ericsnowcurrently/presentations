My Talk Proposals for PyCon 2019
================================

<blog post?>

Here's the list:

Accepted:
* to GIL or not to GIL: the Future of Multi-Core (C)Python

Rejected:
* Subinterpreters and You!

Dropped:
<NONE>

to GIL or not to GIL: the Future of Multi-Core (C)Python
--------------------------------------------------------

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


Subinterpreters and You!
------------------------

(#325)

*Description*

Did you know that the CPython runtime supports running multiple independent interpreters at the same time, in the same process? It has for over 20 years, in fact! The catch is that it's only exposed in the C-API. Starting in Python 3.7 you can use subinterpreters from Python code, though with some caveats for now.

Come to this talk to find out what subinterpreters are, why you should care, how to take advantage of them, what their limitations are, and what their future holds. That includes how they may eventually support GIL-free parallelism in Python (without async). This talk will include a variety of practical examples. 

*Audience*

This is aimed at nearly everyone (though beginners probably won't get the most out of it). In particular, this talk will interest anyone that uses concurrency in their code (or wants to be conversant in the topic), as well as anyone who has ever complained about the GIL. That's a reasonably sized group. <wink> Library authors that want to take advantage of subinterpreters (via extension modules) will also benefit.

The talk will also involve a small amount of discussion on CPython internals, so that crowd may be interested. However, this will not be a deep dive into internals; I will give any necessary context to a general audience. At least half the talk will be a practical demonstration of using subinterpreters from Python code. 

*Outline*

A rough outline that gives me some wiggle room for a 30 minute talk:

(total: 25 minutes)
1. what are subinterpreters (4 minutes)
2. what's different in Python 3.7 (1 minute)
3. the C-API (1 minute)
4. running code in a subinterpreter from Python (3 minutes)
5. subinterpreters and threads (2 minutes)
6. interpreter isolation (2 minutes)
7. sharing data (5 minutes)
8. a different approach to concurrency (2 minutes)
9. limitations and caveats (2 minutes)
10. a GIL-free, async-free future (3 minutes)

A 45 minute talk would include:

* additional practical examples
* extra info about subinterpreters and extension modules
* more details about future subinterpreter-related improvements in CPython 

*Additional notes*

PEP 554 relates closely to this talk. If the PEP isn't accepted in time for PyCon then I'll put a module on the cheeseshop that does the same thing. (I can provide an advance copy privately if desired.)

Other notes about me:

* given 3 talks at past PyCons
* one of the few Python core developer working extensively on the CPython runtime
* gave related talk at 2018 Language Summit

For details on the overall project, see https://github.com/ericsnowcurrently/multi-core-python.

FWIW, I favor this talk over my other proposal, #603 ("to GIL or not to GIL: the Future of Multi-Core (C)Python"). However, I'd be glad to give either (or both). 
