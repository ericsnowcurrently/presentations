My Talk Proposals for PyCon 2012
================================

http://ericsnowcurrently.blogspot.com/2011/10/my-pycon-2012-talk-proposals.html

Here's the list:

Accepted:
* Getting the Most Out of Python Imports
* Interfaces and Python

Rejected:
* The Future of Python's Imports
* Explicit Handlers to Python Language Features

Dropped:
* AST Transformations using PEP 302
* Code Archaeology and Repository Spelunking
* Running Python in Your Browser with Chrome's NativeClient
* Python on Android


Getting the Most Out of Python Imports
--------------------------------------

To really take advantage of Python you must understand how imports work and how to use them effectively. In this talk we'll discuss both of these. After a short introduction to imports, we'll dive right and show how you can put PEP 302 import hooks to work for you.
Type: Talk
Python's import statement has been a powerful feature since the first release, and only gotten better with age. Understanding how imports work under the hood will let you take advantage of that power.
The key to customizing Python's imports is the importers introduced by PEP 302. That's a tool that you want in your belt!
Talk Outline
Python's imports (5 min)
the evolution of the import machinery
the gears in the machine
motivation for PEP 302
Finder Objects (5 min)
what they're for
how to write one
what to do with it
Loader Objects (5 min)
what they're for
how to write one
what to do with it
sys.meta_path vs. sys.path_hooks (5 min)
when and how to use them
example of putting it all together
Real-life Examples of Import Hooks (7 min)
Python/import.c
importlib module
PyPy
PyFilesystem
Other Import Customizations (3 min)
builtins.__import__
.pth files
PEP 402
import engine

The Future of Python's Imports
------------------------------

The history of Python's import machinery is one of evolving power since its humble beginnings in the original Python release. That trend is continuing with efforts to make Python's imports even more useful. Come hear about the current and upcoming project, and learn why it matters to you.
Type: Talk
Here's an outline of the talk:
Imports in Python (5 min)
the evolution of the import machinery
the gears in the machine
importlib (7 min)
its introduction in the stdlib
as the default builtins.__import__
status
PEP 382/402 (5 min)
why "namespace" packages matter
how it would work
status
The Import Engine (5 min)
consolidating the import state
how it could help you
status
Other PEPs (3 min)
PEP 369 -- Post import hooks
PEP 395 -- Module Aliasing
And Beyond... (5 min)
Armin's Rant
exocet, mercurial, and PEAK
Much more information on Python imports may be found at my Python Imports page.


Explicit Handlers to Python Language Features
---------------------------------------------

Come learn all about how Python's language features are handled and how some of that behavior can be customized. We'll go from the grammar to AST and on to the functions that handle the behavior.
Type: Talk
Like all programming languages, Python can be described by the language features it has and how it handles those features. One of Python's strengths is how some of these handlers, like __import__ or __len__, can be explicitly customized to extend the language.
In this talk we'll look at Python's language features and how it handles them. We'll trace the path from syntax through AST and beyond. We'll also look at the handlers that you can override and what implicit handlers are candidates to be exposed. This talk will be partly CPython-specific, but the analytic process applies equally to alternate implementations.
Talk Outline:
Language Features and Handlers (3 min)
what is a language feature?
what is a handler?
a comparison across languages of a feature subset
Python Language Features (7 min)
Python's language feature catalog
a handler for each feature
examples of implicit handlers
examples of explicit handlers (special methods)
From Grammar to AST (6 min)
mapping features to grammar
mapping grammar to AST
some concrete examples
examining the transformation
From AST to Handler (9 min)
via opcodes in CPython
mapping AST to opcodes (compiler)
mapping opcodes to handlers
implicit handlers as an implementation detail
some concrete examples
examining the transformation
Current Implicit Handlers (5 min)
a look at the handlers that are not customizable
which ones could be turned into explicit handlers
the impact of doing so
More information on Language Feature Handlers see my Python Language Feature Handlers page.


Interfaces and Python
---------------------

In 2.6, Python introduced the Abstract Base Classes. Before that we had "protocols" (and we still do). In this talk we'll look at the how the general concept of interfaces fits into today's Python. We'll also look at some of the alternate proposals of the past, some of the controversies around ABCs, and the direction interfaces might go in the future.
Type: Talk
Talk Outline:
What are Interfaces? (3 min)
modeling strict abstraction
precedents in other languages
Interfaces in Python (6 min)
duck-typing
Python "protocols"
past proposals (PEP 245)
how Python "interfaces" are different
Newer Interface Support (11 min)
annotations
Abstract Base Classes
why run-time validation?
ABC vs. duck-typing
Third-party Libraries (5 min)
Peak's PyProtocols
zope.interface
Twisted
What Next? (3 min)
strict interfaces
compile-time validation
an example interface library
For more comprehensive coverage of interfaces in Python, check out this reference.


AST Transformations using PEP 302
---------------------------------

Python's stdlib offers the ast module, which exposes the AST portion of the compiler. It's a powerful tool for manipulating code before compilation. Combine this with a PEP 302 import hook and you are ready to do some pretty neat stuff. We'll use domain-specific languages to demonstrate the power of this technique.
Type: Talk
AST + PEP 302 == awesome
First of all, if you want an introduction to the stdlib ast module or PEP 302 importers, this talk has a lot to offer. If you are interested in domain-specific languages, we'll be talking about those too.
The magic of combining the ast module with import hooks is in the that ability to transform a seemingly invalid module into a valid one. The end result is compiled python code, as though you had written the module in legal Python in the first place.
Talk Outline:
the stdlib ast module (5 min)
briefly cover CPython's compiler
look at the interface of the AST module
a quick example of using the AST module to modify partially compiled code
PEP 302 importers (5 min)
customizing imports and the problem with builtins.import
what goes into an importer (finders and loaders)
the default importers
sys.meta_path vs. sys.path_hooks
two examples of custom importers
an example of a domain-specific language (5 min)
what is a DSL?
a simple DSL for SQL
putting it all together (15 min)
an AST transformer for the DSL
an importer that intelligently applies the AST transformer
actually using it with a real database
For more information, go to my pages on Code Transformations in Python, Python Imports, and Domain-Specific Languages in Python.


Code Archaeology and Repository Spelunking
------------------------------------------

Come learn about the tools I used and experience I had while peeling back the layers of CPython's full repository. We'll also talk about how these relate to "code archaeology" in general.
Type: Talk
The power of version control lies partly in the history it offers. However, for a large project digging down into the repository to gather historical artifacts is no trivial matter.
While working on a project related to Python's history, I needed to look at commit history and to search through commits/patches. Thankfully CPython's repository goes back almost to the beginning (1990). In early 2011 the CPython repository moved to Mercurial, which factors in to the tools I was able to use in my spelunking.
In this talk we'll look at the tools and methods I used in my "archaeology", with a focus on Mercurial and CPython. However, the material should be applicable to most VCSs and most projects.
Talk Outline:
What is Code Archaeology? (3 min)
motivation (understanding what brought us here)
why does it matter?
The Tools (2 min)
VCS
mail archives
Investigating CPython (2 min)
CPython resources
mercurial repos
mail archives
The Evolution of a Code Base (3 min)
how projects evolve
examples from CPython
The Players (3 min)
personalities and community play a part
examples from CPython
Preparing to Dive In (3 min)
determine what you care about
know what to look for (get familiar with the topic)
examples from CPython
Extracting Timelines (7 min)
take a focused approach
search permutations on the VCS
supplement with other resources
examples from CPython
The Story Behind the Commits (4 min)
lingering questions (like "why?!?")
searching in the mail archives
timeline offers a target
examples from CPython
What Might Have Been (3 min)
alternate outcomes mostly fade into obscurity
lessons learned from them
examples from CPython
What I learned about the CPython Core Developers (2 min)
For more information go to my Code Archaeology and Repository Spelunking page.


Running Python in Your Browser with Chrome's NativeClient
---------------------------------------------------------

Chrome's Native Client has gotten a lot of press in the last year. It's a tool for compiling C/C++ to native code and running it sandboxed in your browser. This is a talk about porting Python to run in the Native Client, and why you'd like that.
Type: Talk
Mark Seaborn from the Chromium project has done a lot of work on getting CPython to run inside Chrome's Native Client. In this talk we'll look at the work he's done, what's left to do, and how you can help.
We'll also talk about why Python in the NaCl sandbox matters and we'll wrap up by discussing the idea of PyPy on Native Client.
Talk Outline:
What is Native Client? (5 min)
virtual machine for C/C++
released on Chrome in 2011
continued work to port libraries
uses Python 2.x for a number of tools
Porting CPython to Native Client (10 min)
initial work by Mark Seaborn (Jun. 2009)
trouble with dynamic linking and build tools (Dec. 2010)
upcoming dynamic linking support and Python bindings in NaCl
current roadblocks and options
Possibilities with PyPy (15 min)
using PyPy's RPython toolchain to port Python to NaCl
is a NaCl backend for PyPy pointless?
porting the toolchain to NaCl
examples


Python on Android
-----------------

Come learn about the present and future of writing Android apps in Python. We'll cover SL4A and efforts to port both Jython and PyPy.
Type: Talk
The Android mobile operating system is a great target for developers. However, when you write apps for the dalvik virtual machine, you have to write in Java. Personally, I would rather not. Instead, wouldn't it be nice to write Android apps in Python? This has certainly crossed every Python programmer's mind who has even thought about Android. So what are the options?
First of all, in 2008 there was a project called jythonroid that tried to port Jython to Android. We'll talk about why it didn't pan out.
Secondly, in 2010 Google released the "Scripting Layer for Android" (SL4A) project with Python support; and in 2011 they spun off the Python portion into its own project. It's neat to be able to write Python on my phone. We'll talk about why this currently isn't a good solution for writing Android Apps; and what could make it work better (i.e. a tool for building wrappers around SL4A scripts).
Finally, two of the Python implementations have already been involved in discussions on porting Python to Android: Jython and PyPy. We'll talk about what happened with past (official) porting efforts for Jython and where efforts are headed for both projects.
The idea of writing Android apps in Python is both appealing and elusive. It invites your imagination. So, let's tap into that! To wrap up the talk we'll look at what it would be like to write for Android in Python and what you can do to help make that a reality.
Talk Outline:
Programming for Android (3 min)
Java
Android API
an example
Dalvik is not JVM
Python on Android: SL4A (6 min)
summary
examples
difference from native Android apps
why SL4A Isn't Good Enough
making it a little better
Current Efforts in Jython (13 min)
jythonroid (2009)
jython-for-android (2011)
early optimism (2008/2009)
hints of Android support for 2.5.1 (2009)
The challenge of dynamic code generation on Android
PBC (Python bytcode) and Java PBC VM
performance implications
examples (theoretical)
future availability
Current Efforts in PyPy (8 min)
acknowledged early (2009)
JIT backend for ARM (2011)
examples (theoretical)
future availability
