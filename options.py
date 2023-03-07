import datetime
from colorama import Fore, Style

from controller import Controller
from modelJson import ModelJson
from view import View
from note import Note

def run():
    c = Controller(ModelJson("notes.json"), View())

    while True:
        command = input(Fore.YELLOW +'создать заметку - 1\n'
                        'редактировать заметку - 2\n'
                        'прочитать заметку - 3\n'
                        'удалить заметку - 4\n'
                        'прочитать все заметки - 5\n'
                        'удалить все заметки - 6\n'
                        'выход - 7\n' +
                        'Выберете опцию: '
                        + Style.NORMAL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + '\nСоздать заметку:')
            c.create_note(get_note_data())

        elif command == '2':
            if c.notes_exist():
                print(Fore.GREEN + '\nРедактировать заметку:')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())
        
        elif command == '3':
            print(Fore.GREEN + '\nПрочитать заметку:')
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить заметку:')
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '5':
            if c.notes_exist():
                print(Fore.GREEN + '\nСписок всех заметок:')
                c.show_notes()

        elif command == '6':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить все заметки:')
                if input(Fore.RED + 'Вы точно хотите удалить все заметки? (да-1 / нет-0): ').capitalize() == '1':
                    if c.notes_exist():
                        c.delete_all_notes()
             
def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите содержание заметки: ')
    return Note(note_id, date, title, text)

def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'Введите целое положительное число!')