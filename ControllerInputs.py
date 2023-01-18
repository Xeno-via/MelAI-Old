from dis import disco
import melee
import argparse
import signal
import sys
import random
import TensorFlowNet

def RandomInputButton(RandNum):
    match RandNum:
        case 1:
             controller.press_button(melee.enums.Button.BUTTON_A)
             print("A")
        case 2:
             controller.press_button(melee.enums.Button.BUTTON_B)
             print("B")
        case 3:
             controller.press_button(melee.enums.Button.BUTTON_L)
             print("L")
        case 4:
             controller.press_button(melee.enums.Button.BUTTON_R)
             print("R")
        case 5:
             controller.press_button(melee.enums.Button.BUTTON_Z)
             print("Z")
        case 6:
             controller.press_button(melee.enums.Button.BUTTON_Y)
             print("Y")

def RandomStickInput(RandNumX, RandNumY):
    controller.tilt_analog(melee.enums.Button.BUTTON_MAIN, RandNumX, RandNumY)
       

def check_port(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 4:
        raise argparse.ArgumentTypeError("%s is an invalid controller port. \
                                         Must be 1, 2, 3, or 4." % value)
    return ivalue

parser = argparse.ArgumentParser(description='Libmelee in action')
parser.add_argument('--dolphin_executable_path', '-e', default=None, help='The directory where dolphin is')
parser.add_argument('--connect_code', '-t', default="", help='Direct connect code to connect to in Slippi Online')
args = parser.parse_args()

console = melee.Console(path=args.dolphin_executable_path)
controller = melee.Controller(console=console, port=1, type=melee.ControllerType.STANDARD)
controller_opponent = melee.Controller(console=console, port=4, type=melee.ControllerType.GCN_ADAPTER)
console.run()
console.connect()
controller.connect()
costume = 1
framedata = melee.framedata.FrameData()


while True:
    gamestate = console.step()
    if gamestate is None:
        continue
    if gamestate.menu_state in [melee.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:
        #print(gamestate.players[1].action)
        if gamestate.players[1].action == melee.enums.Action.STANDING or gamestate.players[1].action == melee.enums.Action.CROUCHING or gamestate.players[1].action == melee.enums.Action.DASHING or gamestate.players[1].action == melee.enums.Action.FALLING or gamestate.players[1].action == melee.enums.Action.FALLING_BACKWARD or gamestate.players[1].action == melee.enums.Action.FALLING_FORWARD or gamestate.players[1].action == melee.enums.Action.ON_HALO_DESCENT or gamestate.players[1].action == melee.enums.Action.ON_HALO_WAIT or gamestate.players[1].action == melee.enums.Action.RUNNING or gamestate.players[1].action == melee.enums.Action.SHIELD or gamestate.players[1].action == melee.enums.Action.TUMBLING or gamestate.players[1].action == melee.enums.Action.EDGE_HANGING :
            controller.release_all()
            RandomInputButton(random.randint(1, 6))
            RandomStickInput(random.uniform(0, 1), random.uniform(0, 1))
            controller.flush()
        else:
            controller.empty_input()
    else:
        melee.MenuHelper.menu_helper_simple(gamestate, controller, melee.Character.DOC, melee.Stage.YOSHIS_STORY, costume=costume, autostart=True, swag=False)



