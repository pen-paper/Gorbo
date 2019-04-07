Engine Structure
================

The game engine used in this game has four main components: the game,
modes, sprites, and controllers. 

Game
----

The game is a singleton that controls the window. It keeps track of the
current mode, and handles switching between them. It also catches
external events and passes them down to the current mode and its
sprites.

Modes
-----

A mode in this engine is a self-contained region, equivalent to a scene
or room in other engines. Modes can be 2d or 3d (or both), and are
responsible for drawing everything to the screen, generally through a
pyglet Batch. They also alert sprites to events, whether external (such
as keypresses) or internal (such as collisions or round changes during
combat).

Sprites
------

A sprite is a thing that is visible in the world. It contains its own
position, velocity, and texture information. Sprites are also
responsible for both updating themselves and responding to events, such
as collisions with other sprites or key presses. Each sprite has an
associated controller, which can be accessed for any purpose in
updating, reacting, or drawing.

Four types of sprites are used:

  * *Ground Sprites*

    Ground sprites form the ground of a 3d mode. In addition to
    responding to events, ground sprites must also be able to tell the
    current mode the height of the ground at a given position so that
    model sprites can be given the proper height for them to stand (or
    land, if falling). Anything a character can stand on should be a
    ground sprite.

  * *Model Sprites*

    While ground sprites generally do have models, model sprites
    represent things in the world. Collisions between model sprites are
    handled horizontally, as long as the heights are close enough
    vertically. Characters and walls should be model sprites.

  * *Display Sprites*

    Display sprites are 2d, and are used for showing information such
    as menus, health bars, and similar things. No collision detection
    is done for these.

  * *Null Sprites*

    Null sprites do not have any display and serve only as an
    intermediate between the mode and controller for event purposes.


Controllers
-----------

Controllers serve as persistent data storage devices. They are not
responsible for remembering position, but are responsible for any
abilities a character has, items they have collected, and other peices
of relevant history. Each controller may have multiple sprites, spread
among as many modes as are necessary. (Ex: the main player character
controller will have sprites in the Overworld mode and every Combat
mode.) If necessary, controllers may have their own update functions,
but sprites are still responsible for calling those. Null sprites exist
for this purpose.
