import os
import random
import cv2  # OpenCV 라이브러리 import
import sys  # sys 모듈 import
import mediapipe as mp  # MediaPipe 패키지 import하고 mp라는 별칭으로 사용하겠다는 뜻.
import math  # math 모듈 import
import pyttsx3
ch=0
# 거리 계산 함수 선언
def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))  # 두 점 p1, p2의 x, y 좌표로 거리를 계산한다.
def practice(fingers, random_file):
    global ch
    if fingers == f'{random_file}':
        engine.say("정답입니다.")
        engine.runAndWait()
        cv2.destroyWindow(f'{random_file}')
        cv2.putText(frame, fingers, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, )
        ch += 1
    else:
        engine.say("틀렸습니다.")
        engine.runAndWait()
        print('틀렸습니다')
        ch -= 1
# MediaPipe 패키지에서 사용할 기능들.
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands  # 손 인식을 위한 객체

cap = cv2.VideoCapture(1)  # 비디오 캡처 객체 생성

if not cap.isOpened():  # 연결 확인
    print("Camera is not opened")
    sys.exit(1)  # 프로그램 종료
fingers=0
random_file=0
hands = mp_hands.Hands()  # 손 인식 객체 생성
skip_ratio = 40
frame_count = 0
while True:  # 무한 반복
    res, frame = cap.read()  # 카메라 데이터 읽기
    if not res:  # 프레임 읽었는지 확인
        print("Camera error")
        break  # 반복문 종료

    frame = cv2.flip(frame, 1)  # 셀프 카메라처럼 좌우 반전
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 미디어파이프에서 인식 가능한 색공간으로 변경
    results = hands.process(image)  # 이미지에서 손을 찾고 결과를 반환
    engine = pyttsx3.init()

    if results.multi_hand_landmarks:  # 손이 인식되었는지 확인
        for hand_landmarks in results.multi_hand_landmarks:  # 반복문을 활용해 인식된 손의 주요 부분을 그림으로 그려 표현
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )
            points = hand_landmarks.landmark#  landmark 좌표 정보들을 points라는 변수로 활용
            key = cv2.waitKeyEx(5) & 0xFF
            folder_path = '/home/pi/Desktop/fingers'
            file_list = os.listdir(folder_path)
            # 사진 한 장씩 나오도록 처리
            while random_file==fingers:

                random_file = random.choice(file_list)
                file_path = os.path.join(folder_path, random_file)

                image = cv2.imread(file_path)
                resized_image = cv2.resize(image, (300,300))

                # 사진 출력
                cv2.imshow(f'{random_file}', resized_image)

            if frame_count % skip_ratio == 0:
                if distance(points[4], points[0]) > distance(points[3], points[0]) and distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[4], points[10]) > distance(points[4], points[6])  and distance(points[8], points[4]) > 0.1 and distance(points[8],points[0])<0.2:
                    fingers = 'a'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[13]) < distance(points[3], points[13]) and distance(points[8], points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) > distance(points[15], points[0]) and distance(points[20],points[0]) > distance(points[19], points[0]) and distance(points[4], points[13]) < 0.1:
                    fingers = 'b'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) > distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) > distance(points[15], points[0]) and distance(points[20],points[0]) > distance(points[19], points[0]) and 0.1 < distance(points[8], points[4]) < 0.3:
                    fingers = 'c'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8], points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]):
                    fingers = 'd'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[16]) < distance(points[3], points[16]) and distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[4], points[16])<0.1 and distance(points[4],points[6])>0.1:
                    fingers = 'e'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) > distance(points[3], points[9]) and distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) > distance(points[15], points[0]) and distance(points[20],points[0]) > distance(points[19], points[0]):
                    fingers = 'f'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[0]) > distance(points[3], points[0]) and distance(points[8], points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[4],points[6])<0.08:
                    fingers = 'g'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[0]) > distance(points[3], points[0]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]) and distance(points[8],points[12]) < 0.1 and distance(points[4],points[10])<0.1:
                    fingers = 'h'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8], points[0]) < distance(points[7], points[0])and distance(points[12], points[0]) < distance(points[11], points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) > distance(points[19], points[0]) :
                    fingers = 'i'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[0]) > distance(points[3], points[0]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[8], points[12]) > 0.1 and distance(points[4],points[6])<0.1:
                    fingers = 'k'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9])>distance(points[3],points[9]) and distance(points[8],points[0])>distance(points[7],points[0]) and distance(points[12], points[0]) < distance(points[11], points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]) and distance(points[8],points[4])>0.2:
                    fingers = 'l'
                    practice(fingers, f'{random_file}')
                elif distance(points[8], points[0]) < distance(points[7], points[0])and distance(points[12], points[0]) < distance(points[11], points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]) and distance(points[4], points[13]) < distance(points[3], points[13]) and distance(points[4], points[10]) > distance(points[4], points[14]) and distance(points[16],points[0])>0.1:
                    fingers = 'm'
                    practice(fingers, f'{random_file}')
                elif distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12],points[0]) < distance(points[11], points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0])  and distance(points[4], points[10]) < distance(points[4], points[6]) and distance(points[12],points[0])>0.1:
                    fingers = 'n'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) > distance(points[3], points[9]) and distance(points[8],points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) > distance(points[19], points[0]):
                    fingers = 'y'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]):
                    fingers = 'x'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) > distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]):
                    fingers = 'w'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[8], points[12]) > 0.1:
                    fingers = 'v'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]) and distance(points[8], points[12]) < 0.1:
                    fingers = 'u'
                    practice(fingers, f'{random_file}')
                elif distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11], points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0])  and distance(points[8],points[0])>0.1:
                    fingers = 't'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8], points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[8], points[5]) < 0.05:
                    fingers = 's'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) < distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]):
                    fingers = 'r'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) > distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]):
                    fingers = 'q'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[9]) > distance(points[3], points[9]) and distance(points[8],points[0]) > distance(points[7], points[0]) and distance(points[12], points[0]) > distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20], points[0]) < distance(points[19], points[0]):
                    fingers = 'p'
                    practice(fingers, f'{random_file}')
                elif distance(points[4], points[0]) > distance(points[3], points[0]) and distance(points[8],points[0]) < distance(points[7], points[0]) and distance(points[12], points[0]) < distance(points[11],points[0]) and distance(points[16], points[0]) < distance(points[15], points[0]) and distance(points[20],points[0]) < distance(points[19], points[0]) and distance(points[8], points[4]) < 0.1:
                    fingers = 'o'
                    practice(fingers, f'{random_file}')
                else :
                    cv2.putText(frame, ' ', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, )
                cv2.imshow("MediaPipe Hands", frame)  # 영상을 화면에 출력.

            frame_count += 1


        if ch>2:
            engine.say("학습종료")
            engine.runAndWait()
            break  # 반복문 종료

cv2.destroyAllWindows()  # 영상 창 닫기
cap.release()
