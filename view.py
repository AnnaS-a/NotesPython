from colorama import Fore, Style


class View(object):

    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '---------------------------------------' + Style.RESET_ALL)
        print(Fore.GREEN + 'Заметка добавлена!' + Style.RESET_ALL)
        print(Fore.YELLOW + '---------------------------------------' + Style.RESET_ALL)

    @staticmethod
    def show_empty_list_message():
        print(Fore.YELLOW + '--------------------------------------'+ Style.RESET_ALL)
        print('Заметок нет!')
        print(Fore.YELLOW + '--------------------------------------'+ Style.RESET_ALL)    
        
    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED + '----------------------------------------'+ Style.RESET_ALL)
        print('Заметка с id: {} не найдена!'.format(note_id))
        print(Fore.RED + '----------------------------------------'+ Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.YELLOW + '-------------------------------------' + Style.RESET_ALL)
        print(Fore.GREEN + 'Заметка с id:{} обновлена успешно!'.format(note_id) + Style.RESET_ALL)
        print(Fore.YELLOW + '-------------------------------------' + Style.RESET_ALL)

    @staticmethod
    def show_note(note):
        print(Fore.YELLOW + '------------------------------------' + Style.RESET_ALL)
        print(note)
        print(Fore.YELLOW + '------------------------------------' + Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print('--------------------------------------------------')
        print(Fore.LIGHTRED_EX + 'Удаление заметки с id: {} выполнено!'.format(note_id) + Style.RESET_ALL)
        print('--------------------------------------------------')

    def display_note_id_not_exist(search_id):
        return search_id
    
    


