import datetime
from colorama import Fore, Style

from controller import Controller
from modelJson import ModelJson
from view import View
from note import Note

def run():
    c = Controller(ModelJson("notes.json"), View())

    while True:
        command = input(Fore.YELLOW +
                        'создать заметку - 1\n'
                        'редактировать заметку - 2\n'
                        'прочитать заметку - 3\n'
                        'удалить заметку - 4\n'
                        'прочитать все заметки - 5\n'
                        'удалить все заметки - 6\n'
                        'выход - 7\n' +
                        'Выберете опцию: '
                        + Style.RESET_ALL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + '\nСоздать заметку:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            if c.notes_exist():
                print(Fore.GREEN + '\nРедактировать заметку:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())
        
        elif command == '3':
            print(Fore.GREEN + '\nПрочитать заметку:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить заметку:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        



        
def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')
    return Note(note_id, date, title, text)

def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'Введите целое положительное число!' + Style.RESET_ALL)