from contextlib import contextmanager
@contextmanager
def file_manager(file_name, mode):
    global file
    file = None
    try:
        print(f"File '{file_name}' is opened")
        file = open(file_name,mode)
        yield file
    finally:
        print(f"File '{file_name}' is closed")
        file.close()
with file_manager("context_manager_class.py",'r') as file:
    f = file.read()
    print(f)
