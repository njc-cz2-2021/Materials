from functools import partial, reduce
from typing import Any, List

def validator(to_validate:Any,datatype:str,conditions = None):
    """Code that functions as a template to build functions for code validation"""
    conversion_fn = None
    if datatype == "str":
        conversion_fn = lambda x : str(x)
    elif datatype == "float":
        conversion_fn = lambda x : float(x)
    elif datatype == "int":
        conversion_fn = lambda x : int(x)
    elif datatype == "bool":
        conversion_fn = lambda x : bool(x)

    try:
        converted = conversion_fn(to_validate)
    except:
        return False

    if len(conditions) == 0 or conditions == None:
        return True
    else:
        for condition in conditions:
            if not condition(converted):
                return False
    return True
  
  
