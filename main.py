@namespace
class StatusBarKind:
    Enemy_Health = StatusBarKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_current_tilemap(tilemap("""
        Floor 2 Hard
    """))
    Josephine.set_position(20, 130)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_closed_east,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level17
    """))
    Josephine.set_position(30, 50)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_north,
    on_overlap_tile2)

def on_on_overlap(sprite9, otherSprite):
    statusbar.value += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_a_pressed():
    global Attack, x, y, Josephine, statusbar2
    Attack = True
    x = Josephine.x
    y = Josephine.y
    sprites.destroy(Josephine)
    Josephine = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . f f f f . . . . . . 
                    . . . . f f f e e f f f . . . . 
                    . . . f f e e e e e e f f . . . 
                    . . f f e e e e e e e e f f . . 
                    . . f e e e e e e e e e e f . . 
                    . f f e e e e e e e e e e f f . 
                    . f f e f f f e e f f f e f f . 
                    . . f e f b f 4 4 f b f e f . . 
                    . . f e 4 1 f 4 4 f 1 4 e f . . 
                    . . . f e 4 4 4 4 4 4 e f e . . 
                    . . . e f 2 2 2 2 e d d 4 e . . 
                    . . . 4 f 2 2 2 2 e d d e . . . 
                    . . . . f 4 4 4 4 f e e . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . f f f . . . . . . . . .
        """),
        SpriteKind.player)
    Josephine.set_position(x, y)
    x = Josephine.x
    y = Josephine.y
    statusbar.value += -1
    pause(200)
    sprites.destroy(Josephine)
    Josephine = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f e e f f f . . . . 
                    . . . f f e e e e e e f f . . . 
                    . . f f e e e e e e e e f f . . 
                    . . f e e e e e e e e e e f . . 
                    . . f e e e e e e e e e e f . . 
                    . . f e e f f e e f f e e f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f 4 4 f 1 4 e e f . 
                    . . f e e 4 4 f f 4 4 e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.player)
    Josephine.set_position(x, y)
    scene.camera_follow_sprite(Josephine)
    controller.move_sprite(Josephine, 100, 100)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.health)
    statusbar2.attach_to_sprite(Josephine)
    Attack = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite3, location3):
    statusbar2.value += -1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.set_current_tilemap(tilemap("""
        Corridor
    """))
    Josephine.set_position(10, 125)
    game.show_long_text("Welcome to the Dungeons! Get through and kill all the enemies in your way to get out! Good Luck!!",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_east,
    on_overlap_tile4)

def on_on_overlap2(sprite5, otherSprite2):
    Ghost: Sprite = None
    statusbar2.value += -1
    sprites.destroy(Ghost)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_overlap_tile5(sprite6, location6):
    global statusbar, Hard_Boss
    tiles.set_current_tilemap(tilemap("""
        Boss Room
    """))
    Josephine.set_position(150, 60)
    statusbar = statusbars.create(60, 4, StatusBarKind.enemy_health)
    Hard_Boss = sprites.create(assets.image("""
        Hard Boss
    """), SpriteKind.enemy)
    Hard_Boss.set_position(70, 100)
    statusbar.set_color(7, 2)
    statusbar.attach_to_sprite(Hard_Boss)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_east,
    on_overlap_tile5)

def on_overlap_tile6(sprite8, location8):
    tiles.set_current_tilemap(tilemap("""
        Floor 1 Easy
    """))
    Josephine.set_position(30, 40)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_south,
    on_overlap_tile6)

def on_overlap_tile7(sprite52, location5):
    global list2, Josephine
    list2 = ["Helmet", "Armor", "Shield", "Sword"]
    game.splash("You just got a ", list2._pick_random())
    if list2._pick_random():
        Josephine = sprites.create(img("""
                . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f f f f d d d d d e e f . . 
                            . f d d d d f 4 4 4 e e f . . . 
                            . f b b b b f 2 2 2 2 f 4 e . . 
                            . f b b b b f 2 2 2 2 f d 4 . . 
                            . . f c c f 4 5 5 4 4 f 4 4 . . 
                            . . . f f f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
            """),
            SpriteKind.player)
    tiles.set_tile_at(location5, sprites.dungeon.chest_open)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile7)

def on_overlap_tile8(sprite7, location7):
    tiles.set_current_tilemap(tilemap("""
        Level selection
    """))
    Josephine.set_position(30, 30)
    game.show_long_text("Up is Hard Mode, Down is Easy Mode", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile8)

list2: List[str] = []
Hard_Boss: Sprite = None
y = 0
x = 0
Attack = False
statusbar: StatusBarSprite = None
statusbar2: StatusBarSprite = None
Josephine: Sprite = None
scene.set_background_color(11)
Josephine = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f e e f f f . . . . 
            . . . f f e e e e e e f f . . . 
            . . f f e e e e e e e e f f . . 
            . . f e e e e e e e e e e f . . 
            . . f e e e e e e e e e e f . . 
            . . f e e f f e e f f e e f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f 4 4 f 1 4 e e f . 
            . . f e e 4 4 f f 4 4 e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Josephine)
Josephine.set_position(10, 125)
scene.camera_follow_sprite(Josephine)
tiles.set_current_tilemap(tilemap("""
    Start level
"""))
statusbar2 = statusbars.create(20, 4, StatusBarKind.health)
statusbar2.attach_to_sprite(Josephine)

def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)
