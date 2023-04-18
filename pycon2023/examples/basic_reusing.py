import os
import os.path
from test.support import interpreters


SCRIPT_DIR = os.path.dirname(__file__)


def section_header(label):
    print()
    print('####################')
    print(f'# {label}')
    print('####################')
    print()


#############################

interp = interpreters.create()


#############################

section_header('example 1')

"""
>>> interp.run('print("spam")')
spam
>>> interp.run('print("eggs")')
eggs
>>> interp.run('print(42)')
42
"""

interp.run('print("spam")')
interp.run('print("eggs")')
interp.run('print(42)')


#############################

section_header('example 2')

"""
>>> interp.run('answer = 42')
>>> interp.run('print(answer)')
42
"""

interp.run('answer = 42')
interp.run('print(answer)')


#############################

section_header('example 3')

"""
>>> interp.run('''if True:
...     import required_module
...     def run_task():
...         ...
...     ''')
>>> do_something_for_a_while()
>>> interp.run('run_task()')
"""

filename = f'{SCRIPT_DIR}/required_module.py'
with open(filename, 'w') as outfile:
    outfile.write('print("imported", __name__)')

interp.run(f'''if True:
    import sys
    sys.path.insert(0, {SCRIPT_DIR!r})
    import required_module
    def run_task():
        print('spam')
    ''')
...  # do_something_for_a_while()
interp.run('run_task()')

os.unlink(filename)
