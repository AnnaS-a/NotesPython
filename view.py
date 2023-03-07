from colorama import Fore

class View(object):

    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '---------------------------------------')
        print(Fore.GREEN + 'Заметка добавлена!')
        print(Fore.YELLOW + '---------------------------------------')

    @staticmethod
    def show_empty_list_message():
        print(Fore.YELLOW + '--------------------------------------')
        print('Заметок нет!')
        print(Fore.YELLOW + '--------------------------------------')    
        
    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED + '----------------------------------------')
        print('Заметка с id: {} не найдена!'.format(note_id))
        print(Fore.RED + '----------------------------------------')

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.YELLOW + '-------------------------------------')
        print(Fore.GREEN + 'Заметка с id:{} обновлена!'.format(note_id))
        print(Fore.YELLOW + '-------------------------------------')

    @staticmethod
    def show_note(note):
        print(Fore.WHITE + '------------------------------------')
        print(note)
        print(Fore.WHITE + '------------------------------------')

    @staticmethod
    def display_note_deletion(note_id):
        print('--------------------------------------------------')
        print(Fore.LIGHTRED_EX + 'Заметка с id: {} удалена!'.format(note_id))
        print('--------------------------------------------------')

    def display_note_id_not_exist(search_id):
        return search_id
    
    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(Fore.BLUE + '----------------------------------')
            print(note)
            print(Fore.BLUE + '----------------------------------')

    @staticmethod
    def display_all_notes_deletion():
        print(Fore.RED + '-----------------------------------------')
        print('Все заметки удалены!')
        print(Fore.RED +'------------------------------------------')


    



