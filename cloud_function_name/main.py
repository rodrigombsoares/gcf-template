import os


def sec_function(param_sec):
    return param_sec*2


def main_function(request):
    print(os.getenv('DB_NAME'))
    return sec_function(request+'a')