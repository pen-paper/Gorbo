class Event(object):
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


class ActivateEvent(Event):
    handler_name = "on_activate"

class KeyDownEvent(Event):
    handler_name = "on_key_down"

class KeyUpEvent(Event):
    handler_name = "on_key_up"

class CollisionEvent(Event):
    handler_name = "on_collision"

class MouseDownEvent(Event):
    handler_name = "on_mouse_down"

class MouseUpEvent(Event):
    handler_name = "on_mouse_up"

class UpdateEvent(Event):
    handler_name = "on_update"

class CreateSpriteEvent(Event):
    handler_name = "on_create"

class DeleteSpriteEvent(Event):
    handler_name = "on_delete"

class QuitEvent(Event):
    handler_name = "on_quit"

class PauseEvent(Event):
    handler_name = "on_pause"

class UnPauseEvent(Event):
    handler_name = "on_resume"


class Response(object):
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


class ChangeMode(Response): pass
class CreateSprite(Response): pass
class DeleteSprite(Response): pass
class NoResponse(Response): pass
