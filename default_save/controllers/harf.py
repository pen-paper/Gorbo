def on_key_down(self, event):
    if event.key == key.A:
        self.vx = -1
    elif event.key == key.D:
        self.vx = 1
    elif event.key == key.W:
        self.vz = -1
    elif event.key == key.S:
        self.vz = 1
    else:
        print(event.key)
        for i in dir(key):
            if getattr(key, i) == event.key:
                print(i)
    return []

def on_key_up(self, event):
    if event.key == key.A:
        self.vx = -0
    elif event.key == key.D:
        self.vx = 0
    elif event.key == key.W:
        self.vz = -0
    elif event.key == key.S:
        self.vz = 0
    return []

def on_update(self, event):
    self.x += self.vx * event.dt
    self.y += self.vy * event.dt
    self.z += self.vz * event.dt
    self.sprite.x = self.x
    self.sprite.y = self.y
    self.sprite.z = self.z
    return []

def on_activate(self, event):
    self.sprite = ModelSprite(self.model, self.x, self.y, self.z, self, self.texture)
    return [CreateSpriteEvent(sprite=self.sprite)]


def __init__(self, save, data):
    super(self.ControllerClass, self).__init__()
    self.texture = save.image("textures/{}".format(data["texture"]))
    self.model = save.obj("models/character.obj")
    self.perks = data["perks"]
    self.skills = data["skills"]
    self.level = data["level"]
    self.class_ = data["class"]
    self.sprite = None
    self.x = 0
    self.y = 0
    self.z = 0
    self.vx = 0
    self.vy = 0
    self.vz = 0


