import json
import pyglet

from . import model
from . import controller
from . import event
from . import sprite


class SaveFile(pyglet.resource.Loader):
    """Load program resource files from save file.

    This is a subclass of the pyglet Loader, so look at that for
    better documentation. This adds needed file formats for this game
    engine.
    """

    def __init__(self):
        super().__init__()
        self._loaded_controllers = {}

    def json(self, name):
        """Load a JSON document.

        :Parameters:
            `name`: str
                Filename of the JSON resource to load.

        :rtype: `dict`
        """
        self._require_index()
        file = self.file(name)
        return json.load(file)

    def save_json(self, name, data):
        self._require_index()
        file = self.file(name, "w")
        json.dump(file, data)

    def obj(self, name):
        """Load an OBJ file."""
        self._require_index()
        file = self.file(name)
        return model.Model(file)

    def controller(self, name):
        if name in self._loaded_controllers:
            return self._loaded_controllers[name]
        self._require_index()
        file = self.file(name)
        local_values = {}
        exec(file.read(), self.module_globals(), local_values)
        new_controller = type(name, (controller.Controller,), local_values)
        new_controller.ControllerClass = new_controller
        self._loaded_controllers[name] = new_controller
        return new_controller

    def module_globals(self):
        class KeyCollection(object): pass
        all_keys = KeyCollection()
        all_keys.__dict__.update(pyglet.window.key.__dict__)
        return {"ActivateEvent": event.ActivateEvent,
                "CreateSpriteEvent": event.CreateSpriteEvent,
                "key": all_keys,
                "ModelSprite": sprite.ModelSprite}
