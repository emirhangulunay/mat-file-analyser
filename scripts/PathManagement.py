import os
import platform

class DirectoryLister():
    def __init__(self):
        os.chdir("/" if platform.system()=="Linux" else "C:/")
        self.base = os.getcwd()
        self.exec_path_dict = {}

    def show_path_folders(self):
        self.exec_path_dict = {i: os.path.join(self.base, item) 
                               for i, item in enumerate(os.listdir(self.base)) }

        for i, e in self.exec_path_dict.items(): print(f"{i} <- {e}")
        return self.choose_number()


class PathManager(DirectoryLister):
    def __init__(self):
        super().__init__()
        self.choosedPathNumber = 0

    def choose_number(self):
        try:
            self.choosedPathNumber = int(input("Choose index -> "))
            return self.open_path()

        except ValueError as e:
            print(f"{e} please choose integer")
            return self.choose_number()

    def open_path(self):
        choosedPathName = self.exec_path_dict[self.choosedPathNumber]

        os.chdir(choosedPathName)
        self.base = os.getcwd()
        return self.show_path_folders()

    def start(self):
        return self.show_path_folders()
    

PathManager().start()
