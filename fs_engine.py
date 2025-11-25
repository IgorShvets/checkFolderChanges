import public_var
import typing
import console_engine
import shutil
import os
import json_engine

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

def get_full_path_tech_folder(folder_name: str = ""):
    path_to_tech_folder: str = ""
    if public_var.current_menu == "main": 
        print(f'err: f:get_full_path_tech_folder - cannot return full path to main menu, it not folder!')
        return ""
    if folder_name == "":
        path_to_tech_folder = os.path.join(public_var.PATH_TO_FOLDERS, public_var.current_menu)
    else:
        path_to_tech_folder = os.path.join(public_var.PATH_TO_FOLDERS, folder_name)
        if os.path.exists(path_to_tech_folder):
            return path_to_tech_folder
        else:
            print(f'err: f:get_full_path_tech_folder - folder {path_to_tech_folder} do not exists!')
            return ""
    
def get_full_path_original_folder(folder_name: str = ""):
    tech_folder_path:str = ""
    if folder_name != "":
        tech_folder_path = get_full_path_tech_folder(folder_name)
    else:
        if public_var.current_menu != "main":
            tech_folder_path = get_full_path_tech_folder(public_var.current_menu)
        else:
            print(f'err: f:get_full_path_original_folder - cannot return full path to main menu, it not folder!')
            return ""
    json_file_path: str = os.path.join(tech_folder_path, "path.json")
    full_original_path:str = json_engine.json_read_from_file(json_file_path)
    return full_original_path


