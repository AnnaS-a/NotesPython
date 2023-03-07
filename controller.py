class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_note(self, note):
        self.model.create_note(note)
        self.view.display_note_stored()

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            self.view.show_empty_list_message()
            return False
        else:
            return True
    
    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            self.view.display_note_id_not_exist(search_id)
            return False
        
    def update_note(self, note_id, note):
        self.model.update_note(note_id, note)
        self.view.display_note_updated(note_id)

    
