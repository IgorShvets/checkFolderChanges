import public_var
import fs_engine
import json_engine
import pathlib
import os
import typing

def get_promt_from_user(message: str = ""):
    """
    function get string from user in console. 
    Args: none
    Returns: str user command entered in console
    """
    while True:
        user_command: str = input(f'{public_var.current_menu}:{message}> ')
        if user_command != "":
            return user_command
        else:
            print('err: command cannot be empty')

def perform_command(user_command: str):
    """
    function read users command and change way program execution
    Args:
        user_commands: str - комманда которую необходимо выполнить
    Returns: void
    """
    part_of_command:typing.List[str] = user_command.split(maxsplit=1)
    if len(part_of_command) < 2:
        part_of_command.append("")
    match part_of_command[0]:
        case 'help' | 'h' | '-h':
            perform_help_command()
        case 'quit' | 'exit' | 'q' | '-q':
            perform_exit_command()
        case 'add' | 'open' | 'o' | '-o':
            perform_add_folder(part_of_command[1])
        case 'list' | 'dir' | 'ls':
            perform_list_command()
        case 'delete' | 'del' | '-d' | 'd' | 'rm':
            perform_delete_folder(part_of_command[1])
        case 'select' | '-s' | 's' | 'cd':
            perform_select_menu(part_of_command[1])
        case 'scan':
            perform_scan_command(part_of_command[1])
        case _:
            print("have not command \"" + user_command + "\", type \"" + "help" + "\" for command list")

def perform_scan_command(folder_name: str = ""):
    path_to_folder: str = fs_engine.get_full_path_original_folder(folder_name)

    base = pathlib.Path(path_to_folder)
    paths = [p for p in base.rglob("*")]

    print(paths)

def perform_help_command():
    """
    print help text for user
    """
    if public_var.current_menu == 'main':
        print('MAIN MENU:')
        print('  help, h, -h -- list commands with note')
        print('  add, open -- add folder to monitoring ')
        print('  list, ls, dir -- print list of added folders')
        print('  select, s, -s, cd -- select folder')
        print('  delete, del, -d, d, rm -- delete folder from monitoring')
        print('  quit, exit, q -- exit from programm')
    else:
        print('  help, h, -h -- list commands with note')
        print(f'SELECTED FOLDER {public_var.current_menu}')
        print('  path, -p, p - show full path to selected folder')
        print('  quit, back, -b, -q, q, b, cd .. - back to MAIN MENU')

def perform_add_folder(path_to_folder: str = ""):
    """
    add monitoring of folder
    Args:
        path_to_folder(str): full path to folder
    Returns: 
        void
    """
    if path_to_folder == "":
        path_to_folder = get_promt_from_user('Enter folder path:')
    if os.path.exists(path_to_folder):
        folder_name: str = os.path.basename(path_to_folder)
        technical_folder_path = os.path.join(public_var.PATH_TO_FOLDERS, folder_name)
    else:
        print(f'err: f:perform_add_folder -- folder {path_to_folder} does not exists')
        return

    if technical_folder_path == os.path.join(public_var.PATH_TO_FOLDERS, ""):
        err: str = 'err: f:createFolder - folder_path cannot be empty.'
        print(err)
    if os.path.exists(technical_folder_path):
        err: str = 'err: f:createFolder - folder {folder_path} is already exists!'
        print(f'err: f:create_folder - folder {technical_folder_path} already added')

    fs_engine.create_folder(technical_folder_path)
    json_engine.json_write_to_file(path_to_folder, folder_name, 'path.json')
    print('Folder add was success')


def perform_exit_command():
    exit()

def perform_list_command():
    """
    print list of added folders (in main menu)
    """
    if public_var.current_menu == 'main':
        folder_list = fs_engine.get_folder_list(public_var.PATH_TO_FOLDERS)
        print('ADDED FOLDERS:')
        for folder_name in folder_list:
            print(f'  {folder_name}')
    else:
        pass #добавить логику обработки ls для каталогов



def perform_delete_folder(folder_name: str = ""):
    """
    delete added folder from monitoring (original folder will not detete)
    Args: 
        folder_name(str): name folder for detele
    """
    if public_var.current_menu != "main":
        print(f'error: Deleting an added folders is only possible from the main menu!')
        return
    if folder_name == "":
        folder_name = get_promt_from_user('Folder name to delete:')
    folder_path: str = os.path.join(public_var.PATH_TO_FOLDERS, folder_name)
    fs_engine.delete_folder(folder_path)


def perform_select_menu(menu_name: str = ""):
    """
    select folsers menu or main menu
    """
    if menu_name == "":
        perform_list_command()
        menu_name = get_promt_from_user("Enter menu name or name of folder: ")
    if menu_name == "main":
        public_var.current_menu = "main"
        print('Menu has been switched to main')
    else:
        if menu_name == "..":
            if public_var.current_menu == "main":
                print(f'You are already in main menu')
                return
            if public_var.current_menu != "main":
                public_var.current_menu = "main"
                print('Returned to the main menu')
                return
        folder_path = os.path.join(public_var.PATH_TO_FOLDERS, menu_name)
        if os.path.exists(folder_path):
            public_var.current_menu = menu_name
            print(f'Menu has been switched to {menu_name}!')
        else:
            print(f'err: Menu not found. Enter an existing menu name or a previously added directory.')

    