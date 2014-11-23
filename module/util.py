import os

def get_root_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_absolute_path(relative_path):
    abs_path = ''
    if relative_path:
        abs_path = os.path.join(get_root_path(), relative_path)
        
    return abs_path

def get_current_process_user():
    return os.getlogin()