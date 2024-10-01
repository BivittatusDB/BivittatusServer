import time, platform, os

'''This will be used for aggregate functions. Will be imported with * to ./BivittatusDB.py'''
#extra functions 
def save(table, name=None, types=None):
    pass
    
def metadata(table):
    pass

def scan(table):
    pass

def drop(database:str):
    pass

def show(database: str):
    pass

#File seeking variables
FBEGIN = None
FCURRENT=None
FEND = None

#True and False commands for auto commit
ON=None
OFF=None
ALL=None
PRIMARY=None
VERBOSE=None


#aggregate functions for stage 3
def ensure_column(table):
    pass

def COUNT(table):
    pass

def SUM(table):
    pass

def AVG(table):
    pass

def MIN(table):
    pass

def MAX(table):
    pass

def STDEV(table):
   pass

def STDEVP(table):
    pass

def MODE(table):
    pass

def MEDIAN(table):
    pass

def FIRST(table):
    pass

def LAST(table):
    pass

#A screan cleaner with delay
def pause_and_clean(duration):
    time.sleep(duration)
    
    # Check the operating system using platform.system()
    system_name = platform.system()
    
    if system_name == 'Windows':
        os.system('cls')
    elif system_name in ['Linux', 'Darwin']:  # Darwin' is for macOS
        os.system('clear')
    else:
        raise NotImplementedError(f"The operating system '{system_name}' is not supported for clearing the screen.")

def delay(duration):
    time.sleep(duration)