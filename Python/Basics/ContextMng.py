from contextlib import contextmanager

with open('notes.text', 'w') as file:
    file.write('some text')


class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(exc_type, 'has been handled')
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todos')
print('done')


@contextmanager
def open_managed_file(filename, method):
    f = open(filename, method)
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt', 'w') as f:
    f.write('some new todos...')
