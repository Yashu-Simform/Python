
#Custom Context Manager
class MyContextManager:
    def __enter__(self):
        print('Entering the context block.')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Closing the context.')

def use_custom_contx_mng():
    with MyContextManager():
        print('Accessing the resources.')

def read_from_file(file_path):
    
    with open(file_path) as f:
        print('File name: ', f.name)

        print(f.read(20))   #Reads only 20 characters
        print(f.seekable())
        f.seek(0)       #Change the position of the file pointer

        for line in f:
            print(id(line),end=' -> ')
            print(line)


def copy_file(from_file, to_file, f_type = 'txt'):
    mode = ''
    if f_type != 'txt':
        mode = 'b'
    with open(from_file, 'r' + mode) as rf:
        with open(to_file, 'w' + mode) as wf:
            for line in rf:
                wf.write(line)

        print('File copied!')

    

from_file_ = 'file_handling/test.txt'
to_file_ = 'file_handling/test_copy.txt'
# read_from_file('file_handling/test.txt')
# copy_file(from_file_, to_file_)
copy_file('Outputs/contextmanager.png', 'file_handling/copy.png', 'png')