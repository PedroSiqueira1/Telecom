import re
import time
import pyautogui

# MACROS
Sleep_time = 5
Print_path = r'./print.png'

def nlp(speech):
    if "espera" in speech or "calma" in speech:
        print("sleep")
        return ("sleep", None)
        
    if "atualizar" in speech:
        print("refreshing")
        return ("refresh", None)

    if "checkmate" in speech:
        print("ending")
        return ("end", None)

    else:
        positions = re.findall(r"([a-h][1-8])", speech)
        # re.search(r"([a-z]+) de ([a-h][1-8]) para ([a-h][1-8])", speech)
        return ("move", positions)


def main():
    # pyautogui.screenshot()
    screenshot = pyautogui.screenshot()
    screenshot.save(Print_path)
    
    # get the position of the chessboard
    board = [213, 456] #detect_board(Print_path)

    positions = [] #elias
    while True:
        time.sleep(Sleep_time)

        # get user speech
        speech = "cavalo de B5 para A2" #siq

        action = nlp(speech)

        match action:
            case "end":
                break

            case "refresh":
                board = [] #elias update the chessboard
                break

            case "sleep":
                time.sleep(Sleep_time)
                break

            case "move":
                # move the piece
                break

            case _: # default
                positions = re.findall(r"([a-h][1-8])", speech)
                # elias - move(positions)
                # re.search(r"([a-z]+) de ([a-h][1-8]) para ([a-h][1-8])", speech)



if __name__ == "__main__":
    main()
        