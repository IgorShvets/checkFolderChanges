import pathlib
import os

PATH_TO_THIS_SCRIPT = pathlib.Path(__file__).resolve().parent
PATH_TO_FOLDERS = os.path.join(PATH_TO_THIS_SCRIPT, 'dirs')
current_menu = "main"