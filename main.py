import re
import time

import cv2
import pyautogui
import speech_recognition


# MACROS
Sleep_time = 5
Print_path = r'./print.png'


def detect_edges(path):

        # Using cv2.imread() method
        img = cv2.imread(path)

        # Converting image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

        # Applying GaussianBlur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Applying Canny Edge detection
        canny = cv2.Canny(blur, 50, 150)

        # Finding contours

        contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
        # cv2.drawContours(img, [biggest], -1, (0,255,0), 3)

        # Displaying the image with contour
        #cv2.imwrite('te.png', img)
        #cv2.imshow('\Images\test4.png', img)
        #cv2.waitKey()
        return [biggest[0][0], biggest[2][0]]

def define_board(path):
    # get the position of the chessboard
    board = detect_edges(path)
    print(board)


def recognize_voice():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio_data = audio, language ="pt-BR").lower()
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
        positions = re.findall(r"([a-h][1-8])", speech)
        if len(positions) > 0:
            return ("move", positions)
        
        else:
            return ("", None)


def main():
    time.sleep(Sleep_time)
    
    screenshot = pyautogui.screenshot()
    screenshot.save(Print_path)
    
    # get the position of the chessboard
    board = detect_edges(Print_path)
    print(board)

    positions = [] #elias
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
                board = [] #elias update the chessboard

            case "sleep":
                time.sleep(Sleep_time)

            case "move":
                print(action[1])
                # elias - move(positions)
                # move the piece

            case _: # default
                print("not understood")
                



if __name__ == "__main__":
    main()
        