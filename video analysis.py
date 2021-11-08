import  cv2
import glob
import pytesseract
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd =r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

path=r'E:/pytesseract/save/video/Counter-Strike-video-analysis/*.*'

for bb,file in enumerate (glob.glob(path)):
    img = cv2.imread(file)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold( gray_img, 200, 255, cv2.THRESH_BINARY_INV)
    thresh, im_bwa = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    thresh, im_bwt = cv2.threshold(gray_img, 37, 255, cv2.THRESH_BINARY)

    NAME = img[639:661, 539:609]

    HS = img[676:690, 683:710]

    ADR = im_bwa[676:690, 647:669]

    PHI = img[741:769, 38:87]

    KBP = im_bwa[667:691, 496:517]

    ROUND = img[32:52, 647:730]

    TIME = im_bwt[6:33, 651:728]


    NAME_text = pytesseract.image_to_string(NAME, lang='eng', config='--psm 7')

    HS_text = pytesseract.image_to_string(HS, lang='eng', config='--psm 6')

    ADR_text = pytesseract.image_to_string(ADR, lang='eng', config='--psm 6 digits')

    PHI_text = pytesseract.image_to_string(PHI, lang='eng', config='--psm 6 digits')

    KBP_text = pytesseract.image_to_string(KBP, lang='eng', config='--psm 6 digits')

    ROUND_text = pytesseract.image_to_string(ROUND, lang='eng', config='--psm 7')

    TIME_text = pytesseract.image_to_string(TIME, lang='eng', config='--psm 7 ')

    print('Name:', NAME_text, 'Headshoot:', HS_text, 'ADR:',ADR_text, 'PHI:',PHI_text, 'KBP:',KBP_text,'ROUND:', ROUND_text, 'TIME:',TIME_text)
