class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_note(self, note):
        self.model.create_note(note)
        self.view.display_note_stored()
