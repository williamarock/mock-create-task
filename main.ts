namespace StatusBarKind {
    export const Enemy_Health = StatusBarKind.create()
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorClosedEast, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`Floor 2 Hard`)
    Josephine.setPosition(20, 130)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite8, location8) {
    tiles.setCurrentTilemap(tilemap`Floor 1 Easy`)
    Josephine.setPosition(30, 40)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite52, location5) {
    let list: number[] = []
    workChest(list, Josephine)
    tiles.setTileAt(location5, sprites.dungeon.chestOpen)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    x = Josephine.x
    y = Josephine.y
    sprites.destroy(Josephine)
    Josephine = sprites.create(img`
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
        `, SpriteKind.Player)
    Josephine.setPosition(x, y)
    x = Josephine.x
    y = Josephine.y
    if (list2[3]) {
        statusbar.value += -15
    } else {
        statusbar.value += -5
    }
    pause(200)
    sprites.destroy(Josephine)
    Josephine = sprites.create(img`
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
        `, SpriteKind.Player)
    Josephine.setPosition(x, y)
    scene.cameraFollowSprite(Josephine)
    controller.moveSprite(Josephine, 100, 100)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar2.attachToSprite(Josephine)
    Hard_Boss.follow(Josephine, 50)
    Attack = false
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    game.gameOver(true)
})
function workChest (list: string[], Josephine: Sprite) {
    list = [
    "Helmet",
    "Trap >:^)",
    "Shield",
    "Sword"
    ]
    game.splash("You just got a ", list._pickRandom())
    if (list[0]) {
        statusbar2.setBarSize(40, 4)
        statusbar2.attachToSprite(Josephine)
    }
    if (list[1]) {
        statusbar2.value += -15
    }
    if (list[2]) {
        statusbar2.setBarSize(40, 4)
        statusbar2.attachToSprite(Josephine)
    }
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite3, location3) {
    statusbar2.value += -1
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorOpenEast, function (sprite4, location4) {
    tiles.setCurrentTilemap(tilemap`Corridor`)
    Josephine.setPosition(10, 125)
    game.showLongText("Welcome to the Dungeons! Get through the maze and beat the final boss to get out and win the game! Good Luck!!!", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    statusbar2.value += -20
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorLockedEast, function (sprite6, location6) {
    tiles.setCurrentTilemap(tilemap`Boss Room`)
    Josephine.setPosition(150, 60)
    statusbar = statusbars.create(60, 4, StatusBarKind.EnemyHealth)
    Hard_Boss = sprites.create(assets.image`Hard Boss`, SpriteKind.Enemy)
    Hard_Boss.setPosition(70, 100)
    statusbar.setColor(7, 2)
    statusbar.attachToSprite(Hard_Boss)
    Hard_Boss.follow(Josephine, 50)
})
let Attack = false
let Hard_Boss: Sprite = null
let statusbar: StatusBarSprite = null
let y = 0
let x = 0
let statusbar2: StatusBarSprite = null
let Josephine: Sprite = null
let list2 : string[] = []
scene.setBackgroundColor(11)
Josephine = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Josephine)
Josephine.setPosition(10, 125)
scene.cameraFollowSprite(Josephine)
tiles.setCurrentTilemap(tilemap`Start level`)
statusbar2 = statusbars.create(20, 4, StatusBarKind.Health)
statusbar2.attachToSprite(Josephine)
