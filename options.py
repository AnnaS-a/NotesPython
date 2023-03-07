import datetime
from colorama import Fore, Style

from note import Note

def run():
    c = Controller(ModelJson("notes.json"), View())

    while True:
        command = input(Fore.GREEN +
                        'создать заметку - 1\n'
                        'редактировать заметку - 2\n'
                        'прочитать заметку - 3\n'
                        'удалить заметку - 4\n'
                        'удалить все заметки - 5\n'
                        'прочитать все заметки - 6\n'
                        'выход - 7\n' +
                        'Выберете опцию: '
                        + Style.RESET_ALL)
        if command == '7':
            break

        
            