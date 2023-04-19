import os
import os.path
import re
import sys
from threading import Thread
from test.support import interpreters


SCRIPTS_DIR = os.path.dirname(__file__)


def match_file(regex, filename):
    with open(filename, errors='ignore') as infile:
        for line in infile:
            if regex.search(line):
                print(f'{filename}: {line}', end='')
            


def match_file_interp(pattern, filename):
    interp = interpreters.create()
    interp.run(f'''if True:
        import re
        import sys
        sys.path.insert(0, {SCRIPTS_DIR!r})
        from grep import match_file
        regex = re.compile({pattern!r})
        match_file(regex, {filename!r})
        ''')


def match_files(pattern, filenames, *, interpreters=False):
    if interpreters:
        def match_one(filename):
            match_file_interp(pattern, filename)
    else:
        regex = re.compile(pattern)
        def match_one(filename):
            match_file(regex, filename)

    threads = []
    for filename in filenames:
        if not os.path.isfile(filename):
            continue
        t = Thread(target=match_one, args=(filename,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


# XXX how many interpreters can you spin up in one process?


if __name__ == '__main__':
    regex = sys.argv[1]
    filenames = sys.argv[2:]
    match_files(regex, filenames, interpreters=False)
    #match_files(regex, filenames, interpreters=True)
