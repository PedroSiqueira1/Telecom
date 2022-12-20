import re
import time
from unidecode import unidecode
from playsound import playsound

import cv2
import pyautogui
import speech_recognition

import getCoord


# MACROS
Sleep_time = 3
Print_path = r'./print.png'


def detect_edges(path):
    screenshot = pyautogui.screenshot()
    screenshot.save(Print_path)

    # Using cv2.imread() method
    img = cv2.imread(path)

    # Converting image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Applying GaussianBlur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Applying Canny Edge detection
    canny = cv2.Canny(blur, 50, 150)

    # Finding contours
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Finding the biggest contour
    biggest = None
    max_area = 0
    for i in contours:
            area = cv2.contourArea(i)
            if area > 100:
                    peri = cv2.arcLength(i,True)
                    approx = cv2.approxPolyDP(i,0.02*peri,True)
                    if area > max_area and len(approx)==4:
                            biggest = approx
                            max_area = area

    # Draw the biggest contour
    cv2.drawContours(img, [biggest], -1, (0,255,0), 3)

    # Displaying the image with contour
    cv2.imwrite('te.png', img)
    cv2.imshow('\Images\contour.png', img)
    cv2.waitKey()
    print(biggest)
    return [biggest[0][0], biggest[2][0]]


def recognize_voice():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        speech_to_txt = ""
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            playsound(r'./sounds/ready.mp3')
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio_data = audio, language ="pt-BR").lower()
            speech_to_txt = unidecode(speech_to_txt) # remove accents
        except Exception as ex:
            print("Sorry. Could not understand.")
    return speech_to_txt


def nlp(speech):
    if "espera" in speech or "calma" in speech:
        print("sleep")
        return ("sleep", None)
        
    if "atualizar" in speech:
        print("refreshing")
        return ("refresh", None)

    if "xeque-mate" in speech:
        print("ending")
        return ("end", None)

    else:
        for replace in [("um", "1"), ("dois", "2"), ("tres", "3"), ("quatro", "4"), ("cinco", "5"), ("seis", "6"), ("sete", "7"), ("oito", "8")]:
            speech = speech.replace(replace[0], replace[1])

        positions = re.findall(r"(\s|^)([a-h] ?[1-8])", speech)
        if len(positions) > 0:
            positions = [x[1].replace(" ", "") for x in positions]
            return ("move", positions)
        
        else:
            return ("", None)


def main():
    time.sleep(Sleep_time)
    
    # get the position of the chessboard
    board_edges = detect_edges(Print_path)
    print("board_edges:", board_edges)

    board_coord = getCoord.coordDictionary(board_edges)
    while True:
        time.sleep(Sleep_time)

        # get user speech
        speech = recognize_voice()
        print(speech)

        action = nlp(speech)
        print(action)

        match action[0]:
            case "end":
                break
            
            case "refresh":
                board_edges = detect_edges(Print_path)
                board_coord = getCoord.coordDictionary(board_edges)

            case "sleep":
                time.sleep(Sleep_time + 10)

            case "move":
                print(action[1])
                getCoord.movePiece(board_coord, action[1])
                # elias - move(positions)
                # move the piece

            case _: # default
                print("not understood")
                



if __name__ == "__main__":
    main()
        