from . import event


class Controller(object):
    def __init__(self, **kwargs):
        self.sprites = []
        self.handlers = {}
        self.__dict__.update(kwargs)

    def handle_event(self, event):
        #print(event.handler_name, hasattr(self, event.handler_name))
        if type(event) in self.handlers:
            return self.handlers[type(event)](event)
        elif hasattr(self, event.handler_name):
            return getattr(self, event.handler_name)(event)
        else:
            return []
        


class NullController(Controller):
    def __init__(self, sprite):
        super().__init__()
        self.sprite = sprite

    def on_activate(self, e):
        return [event.CreateSpriteEvent(sprite=self.sprite)]

