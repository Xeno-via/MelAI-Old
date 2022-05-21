import melee

console = melee.Console(path="/SlippiOnline/")

controller = melee.Controller(console=console, port=1)
controller_human = melee.Controller(console=console,
                                    port=2,
                                    type=melee.ControllerType.GCN_ADAPTER)

console.run()
console.connect()

controller.connect()
controller_human.connect()

while True:
    gamestate = console.step()
    # Press buttons on your controller based on the GameState here!
    gamestate = console.step()
    # Press buttons on your controller based on the GameState here!
    if gamestate.menu_state in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        pass
    else:
        melee.menuhelper.MenuHelper.menu_helper_simple(gamestate, 
                                                       controller, 
                                                       1, 
                                                       melee.enums.Character.FOX, 
                                                       melee.enums.Stage.POKEMON_STADIUM, 
                                                       "", 
                                                       autostart=False, 
                                                       swag=True)
