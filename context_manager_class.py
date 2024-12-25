class Contextmanager:
    def __init__(self, file_name, mode):
        self.file_name=file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with Contextmanager("context_manager_decorator.py","r") as f:
    file = f.read()
    print(file)


with Contextmanager("context_manager_decoratorpy", "a") as f:
    f.write("'hello, world'")
