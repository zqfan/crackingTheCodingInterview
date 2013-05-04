import os
import sys

def patch_sys_path():
    TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
    SOURCE_DIR = os.path.dirname(TESTS_DIR)
    sys.path.append(SOURCE_DIR)
