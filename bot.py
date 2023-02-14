import pyautogui
import time
#
pyautogui.PAUSE = 1
rest = False
#
while True:
    print('Checking')
    if not rest:
        injury = pyautogui.locateOnScreen('injury.png', confidence=0.9)
        if injury is not None:
            print('Yar, we have a peg legged scallywag')
            rest = True
    known_locations = pyautogui.locateOnScreen('known_locations.png', confidence=0.9)
    if known_locations is not None:
        if rest:
            print('Throw `em in the hold!')
            rest_button = pyautogui.locateOnScreen('rest.png', confidence=0.9)
            if rest_button is None:
                print('cannot find rest button :(')
            else:
                pyautogui.click(rest_button)
                time.sleep(1)
                rest_button_confirm = pyautogui.locateOnScreen('rest_2.png', confidence=0.9)
                if rest_button_confirm is None:
                    print('cannot find rest_button_confirm :(')
                else:
                    pyautogui.click(rest_button_confirm)
            rest = False
        print('Three sheets to the wind, me hearties')
        pyautogui.click(800,500)
        pyautogui.click(1100,500)
        pyautogui.click(958,667)
    take_all_and_continue = pyautogui.locateOnScreen('take_all_and_continue.png', confidence=0.9)
    if take_all_and_continue is not None:
        print('Take what you can')
        pyautogui.click(take_all_and_continue)
    confirm_leave = pyautogui.locateOnScreen('confirm_leave.png', confidence=0.9)
    if confirm_leave is not None:
        accept = pyautogui.locateOnScreen('accept.png', confidence=0.9)
        if accept is not None:
            print('give nothing back')
            pyautogui.click(accept)
            time.sleep(1)
    board = pyautogui.locateOnScreen('board.png', confidence=0.9)
    if board is not None:
        print('Avast ye scurvy dogs!')
        pyautogui.click(board)
#   All done, clean up for next loop.
    take_all_and_continue = None
    confirm_leave = None
    board = None
    accept = None
    injury = None
    known_locations = None
    rest_button = None
    rest_button_confirm = None
    time.sleep(5)
exit()