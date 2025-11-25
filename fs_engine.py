import public_var
import typing
import console_engine
import shutil
import os

def create_folder(folder_path: str):
    """
    function create folder 
    Args:
        folder_path(str): full path to folder
    Returns: void
    """
    try:
        os.mkdir(folder_path)
        print(f'Folder {folder_path} was created success')
    except OSError as err:
        print(f'err: f:create_folder - folder {folder_path} - {err}')
        console_engine.perform_command(console_engine.get_promt_from_user())

def get_folder_list(folder_path:str):
    """
    returns list of folders in folder_path
    Args:
        folder_path(str): Full path to folder
    Returns:
        List[str]: List folder names
    """
    folder_list: typing.List[str] = []
    try:
        for folder_name in os.listdir(folder_path):
            folder_list.append(folder_name)
        return folder_list
    except OSError as err:
        raise err
        
def delete_folder(folder_path: str):
    """
    delete added folder from 'dirs'
    Args:
        folder_name(str): name folder to detele
    """
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f'Folder \"{folder_path}\" was deleted success!')
        except OSError as err:
            print(f'err: f:delete_folder - cant detele folder {folder_path} - {err}')
    else:
        print(f'err: f:delete_folder - cant detele folder {folder_path} - folder not exists!')

