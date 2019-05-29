import json
import pyglet

from . import model


class SaveFile(pyglet.resource.Loader):
    """Load program resource files from save file.

    This is a subclass of the pyglet Loader, so look at that for
    better documentation. This adds needed file formats for this game
    engine.
    """
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
