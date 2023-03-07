from colorama import Fore, Style


class View(object):
    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        print(Fore.GREEN + 'Заметка успешно добавлена!' + Style.RESET_ALL)
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        