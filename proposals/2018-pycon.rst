My Talk Proposals for PyCon 2018
================================

<blog post?>

Here's the list:

Accepted:
<NONE>

Rejected:
* Subinterpreters and You!


Subinterpreters and You!
------------------------

(#914)

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
