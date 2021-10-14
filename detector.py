import cv2
import pyttsx3 #pip install pyttsx3
engine = pyttsx3.init()
voz = engine.setProperty('rate',200)
cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()
fala = False; #ligar fala mudar para: True
ok = True;esquerda = False;direita = False;cima = False;baixo = False;centro = False
while True:
    success, img = cap.read()
    img = cv2.resize(img,(300,300))
    if ok == True:
        engine.say('sistema iniciado')
        engine.say('selecione um elemento')
        engine.runAndWait()
        tracker.init(img,cv2.selectROI("selecione o elemento",img));ok = False
        cv2.destroyWindow("selecione o elemento")
    success, bbox = tracker.update(img)
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w),(y+h)),(0,0,0),3,1)
    linhas , colunas ,_ = img.shape
    x1 = int(linhas+colunas)/4.5
    y1 = int(linhas+colunas)/10
#localizar
    if y > x1 and baixo == False:
        if fala == True:engine.say('baixo');engine.runAndWait();
        else:print('baixo')
        baixo = True;cima = False;centro = False
    if y1 > y and cima == False:
        if fala == True:engine.say('cima');engine.runAndWait();
        else:print('cima')
        cima = True;baixo = False;centro = False
    if x > x1 and direita == False:
        if fala == True:engine.say('direita');engine.runAndWait();
        else:print('direita')
        direita = True;esquerda = False;centro = False
    if y1 > x and esquerda == False:
        if fala == True:engine.say('esquerda');engine.runAndWait();
        else:print('esquerda')
        esquerda = True;direita = False;centro = False
    if y1 < x and x < x1 and y1 < y and y < x1 and centro == False:
        if fala == True:engine.say('centro');engine.runAndWait();
        else:print('centro')
        esquerda = False;direita = False;cima = False;baixo = False;centro = True
    cv2.imshow("seguindo", img)
    if cv2.waitKey(1)%256 == 27: #apertar ESC
        break
cv2.destroyAllWindows()
