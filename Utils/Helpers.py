import sys, os

class Helpers:
    
    @staticmethod
    def get_base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))