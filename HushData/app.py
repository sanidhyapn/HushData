try:
    from HushData.HushData_cli import *
    from HushData.HushData_gui import *
    from exceptions import *
except ImportError:
    from HushData.HushData_cli import *
    from HushData.HushData_gui import *
    from HushData.exceptions import *


def run(mode:str='cli') -> None:
    """run application in mode specified

    Parameters:
        mode: type of interface for the application
            'cli' --> command-line-interface
            'gui' --> graphical-user-interface
    """
    if mode=='cli':
        command_line_interface()
    elif mode=='gui':
        graphical_user_interface()
    else:
        raise InvalidModeError("Modes = {'cli', 'gui'}")
