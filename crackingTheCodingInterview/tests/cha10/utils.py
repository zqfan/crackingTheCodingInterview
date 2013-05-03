import os
import sys

def patch_sys_path():
    TEST_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_ROOT_DIR = os.path.dirname(TEST_FILE_DIR)
    SOURCE_ROOT_DIR = os.path.dirname(TEST_ROOT_DIR)
    sys.path.append(SOURCE_ROOT_DIR)
