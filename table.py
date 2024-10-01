class TableMeta(type):
    def __new__(cls, name, bases, dct):
        namespace = {}
        namespace.update(dct)
        return type.__new__(cls, name, bases, namespace)

class table(metaclass=TableMeta): ...

class table(metaclass=TableMeta):
    def __init__(self, handler, database, table_name, temp:bool=False, temp_data:list=None) -> table:
        pass

    def log(self):
        pass

    def stop_log(self):
        pass

    def __del__(self):
        pass
    
    def write_log(self, message:str, level:str="INFO"):
        pass

    def trace(self):
        pass

    def __try_commit__(self):
        pass

    def __conv_list_dict__(self):
        pass
    
    def __conv_dict_list__(self, dicts:dict, other):
        pass

    def __read__(self):
        pass

    def __edit__(self):
        pass

    def __make__(self):
        pass

    def __save__(self, name=None, types=None):
        pass

    def __repr__(self) -> list:
        pass
    
    def __str__(self) -> str:
        pass
 
    def __load_metadata__(self):
        pass
    
    def __load_refrenced__(self):
        pass

    def __len__(self)->int:
        pass
    
    def __fix_index__(self, key: int | str)->int:
        pass

    def __getitem__(self, key: int | str):
        pass
    
    def __setitem__(self, key: int | str, value: any):
        pass

    def __empty_check__(self):
        pass

    def __iter__(self):
        pass
    
    def __next__(self):
        pass
        
    def __contains__(self, item: any):
        pass
    
    def __mul__(self, key: int | str):
        pass

    def __check_type__(self, new_data: tuple)->bool:
        pass

    def __check_primary__(self, new_data: tuple)->bool:
        pass
    
    def __load_foreign__(self, other: str):
        pass

    def __check_foreign__(self, new_data:tuple)->bool:
        pass

    def __add__(self, value:tuple)->None:
        pass
        
    def __find_compare__(self, operator:str, value):
        pass
    
    def __sub__(self, value: any):
        pass
        
    def __eq__(self, value):
        pass
    
    def __ne__(self, value):
        pass
    
    def __lt__(self, value):
        pass
    
    def __le__(self, value):
        pass
    
    def __gt__(self, value):
        pass
    
    def __ge__(self, value):
        pass
    
    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __xor__(self, other):
        pass
    
    def __matmul__(self, bool):
        pass

    def __rmatmul__(self, other):
        pass

    def __scan__(self):
        pass

    def contains_duplicates(self, lst):
        pass

    def __scan_primary__(self):
        pass
    
    def __invert__(self):
        pass

    def write(self, value:str | tuple, line=None)->None:
        pass

    def writeable(self)->bool:
        pass
    
    def truncate(self, lines:int)->int:
        pass
    
    def tell(self)->int:
        pass
    
    def seek(self, offset:int, position:int)->tuple:
        pass
    
    def seekable(self)->bool:
        pass
    
    def readable(self)->bool:
        pass
    
    def read(self)->tuple:
        pass
    
    def readline(self, position:int=None)->tuple:
        pass
    
    def readlines(self, lines:int)->list[tuple]:
        pass
    
    def flush(self)->None:
        pass

    def detach(self)->None:
        pass
    
    def isatty(self)->bool:
        pass
    
    def fileno(self) -> int | None:
        pass
