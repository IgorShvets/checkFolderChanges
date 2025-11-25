import json
import public_var
import os

def json_serialization(data: any):
    """
    serialization python object to json data
    Args:
        data(str): Text data or python object what need to serialization
    Returns: 
        str: Json data
    """
    try:
        json_data = json.dumps(data)
    except json.JSONDecodeError as err:
        raise TypeError(f'err: json decode error(wrong format) {err}')
    
    return json_data

def json_read_from_file(file_path: str):
    """
    read json data from file
    Args: 
        folder_name(str): Name added folder
        file_name(str): File name for read 
    Returns:
        any: Python object with deserialize json data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            try:
                json_data = json.load(json_file)
            except json.JSONDecodeError as err:
                print(f'err: f:json_read_from_file - decode json from file {err}')
                raise err
            return json_data
    except IOError as err:
        print(f'err: f:json_read_from_file - file read error {err}')
        raise err

def json_write_to_file(data: any, file_path: str,  append: bool = False):
    """
    write json data to file
    Args: 
        data(any): data for write to file
        file_path(str): path to json file
        append(bool)=False: False - rewrite file, True - append file
    """
    if data == "":
        err: str = 'err: f:write_to_file - arg data is empty'
        print(err)
        return
    if file_path == "":
        err: str = 'err: f:write_to_file - arg file_name is empty'
        print(err)
        return
    if append:
        try:
            with open(file_path, 'a', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except IOError as err:
            print(f'err: f:json_write_to_file - {err}')
        print(f'Write data to file {file_path} was success!')
    else:
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except IOError as err:
            print(f'err: f:json_write_to_file - {err}')
        print(f'Write data to file {file_path} was success!')

def json_deserialization(data: any):
    """
    deserialization python object to json data
    Args:
        data(str): json data or string what need to deserialization
    Returns:
        (any): python object
    """
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as err:
        raise TypeError(f'err: json encode error(wrong format) {err}')
    
    return json_data