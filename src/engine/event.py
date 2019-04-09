class Event(object):
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


class KeyDownEvent(Event): pass
class KeyUpEvent(Event): pass 
class CollisionEvent(Event): pass
class MouseDownEvent(Event): pass
class MouseUpEvent(Event): pass
class UpdateEvent(Event): pass
class CreateSpriteEvent(Event): pass
class DeleteSpriteEvent(Event): pass
class QuitEvent(Event): pass
class PauseEvent(Event): pass
class UnPauseEvent(Event): pass
