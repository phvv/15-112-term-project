# Preston Vander Vos (pvanderv) Section GG
# TERM PROJECT

# Mode organization adopted from:
# https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#modeDemo
####################################
# imports
####################################

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import math
import random

####################################
# init
####################################

def init(data):
    data.mode = "home"
    data.prevMode = "home"
    data.rainbowL = [ "violet", "red", "orange", "yellow", "green",
                      "blue", "indigo", "violet" ]
    data.generalScreen = 0
    loadRainbowPts(data)
    data.counter = 0
    # detection variables
    loadColors(data)
    loadDetection(data)
    # test mode variables
    loadTest(data)
    loadClassify(data)

def loadRainbowPts(data):
    # x, y values for rotating home background
    data.rainbowPts = [ (5, 5), (5, 75), (75, 145), (145, 215),
                        (215, 285), (285, 355), (355, 425), (425, 495) ]

def loadColors(data):
    # used to identify colors by name
    data.colors = {
                    (220,220,220): 'Gainsboro', (245,245,245): 'White Smoke',
                    (255,255,255): 'White'
                    }
    loadPart1(data)
    loadPart2(data)
    loadPart3(data)
    loadPart4(data)

def loadPart1(data):
    tempDict = {
                    (128,0,0): 'Maroon', (139,0,0): 'Dark Red',
                    (165,42,42): 'Brown', (178,34,34): 'Firebrick',
                    (220,20,60): 'Crimson', (255,0,0): 'Red',
                    (255,99,71): 'Tomato', (255,127,80): 'Coral',
                    (205,92,92): 'Indian Red', (240,128,128): 'Light Coral',
                    (233,150,122): 'Dark Salmon', (250,128,114): 'Salmon',
                    (255,160,122): 'Light Salmon', (255,69,0): 'Orange Red',
                    (255,140,0): 'Dark Orange', (255,165,0): 'Orange',
                    (255,215,0): 'Gold', (184,134,11): 'Dark Golden Rod',
                    (218,165,32):'Golden Rod', (238,232,170):'Pale Golden Rod',
                    (189,183,107): 'Dark Khaki', (240,230,140): 'Khaki',
                    (128,128,0): 'Olive', (255,255,0): 'Yellow',
                    (154,205,50):'Yellow Green', (85,107,47):'Dark Olive Green',
                    (107,142,35): 'Olive Drab', (124,252,0): 'Lawn Green',
                    (127,255,0): 'Chartreuse', (173,255,47): 'Green Yellow',
                    (0,100,0): 'Dark Green', (0,128,0): 'Green',
                    (34,139,34): 'Forest Green', (0,255,0): 'Lime'
                }
    data.colors.update(tempDict)

def loadPart2(data):
    tempDict = {
                    (50,205,50): 'Lime Green', (144,238,144): 'Light Green',
                    (152,251,152): 'Pale Green', (143,188,143):'Dark Sea Green',
                    (0,250,154): 'Medium Spring Green', (0,255,255): 'Aqua',
                    (46,139,87): 'Sea Green', (102,205,170):'Medium Aquamarine',
                    (60,179,113): 'Medium Sea Green', (0,139,139): 'Dark Cyan',
                    (47,79,79):'Dark Slate Gray',(175,238,238):'Pale Turquoise',
                    (32,178,170): 'Light Sea Green', (0,255,127):'Spring Green',
                    (0,255,255): 'Cyan', (224,255,255): 'Light Cyan',
                    (0,206,209): 'Dark Turquoise', (64,224,208): 'Turquoise',
                    (72,209,204): 'Medium Turquoise', (0,128,128): 'Teal',
                    (127,255,212): 'Aquamarine', (176,224,230): 'Powder Blue',
                    (95,158,160): 'Cadet Blue', (70,130,180): 'Steel Blue',
                    (100,149,237):'Cornflower Blue',(0,191,255):'Deep Sky Blue',
                    (30,144,255): 'Dodger Blue', (173,216,230): 'Light Blue',
                    (135,206,235): 'Sky Blue', (135,206,250): 'Light Sky Blue',
                    (25,25,112): 'Midnight Blue', (0,0,128): 'Navy',
                    (0,0,139): 'Dark Blue', (0,0,205): 'Medium Blue'
                }
    data.colors.update(tempDict)

def loadPart3(data):
    tempDict = {
                    (0,0,255): 'Blue', (65,105,225): 'Royal Blue',
                    (138,43,226): 'Blue Violet', (147,112,219): 'Medium Purple',
                    (72,61,139): 'Dark Slate Blue', (106,90,205): 'Slate Blue',
                    (123,104,238): 'Medium Slate Blue', (75,0,130): 'Indigo',
                    (139,0,139): 'Dark Magenta', (148,0,211): 'Dark Violet',
                    (153,50,204): 'Dark Orchid', (186,85,211): 'Medium Orchid',
                    (128,0,128): 'Purple', (216,191,216): 'Thistle',
                   (221,160,221):'Plum',(250,250,210):'Light Golden Rod Yellow',
                    (255,0,255): 'Magenta', (219,112,147): 'Pale Violet Red',
                    (199,21,133): 'Medium Violet Red', (218,112,214): 'Orchid',
                    (255,20,147): 'Deep Pink', (255,105,180): 'Hot Pink',
                    (255,182,193): 'Light Pink', (255,192,203): 'Pink',
                    (250,235,215): 'Antique White', (245,245,220): 'Beige',
                    (255,228,196): 'Bisque', (255,235,205): 'Blanched Almond',
                    (245,222,179): 'Wheat', (255,248,220): 'Cornsilk',
                    (255,250,205): 'Lemon Chiffon', (238,130,238): 'Violet',
                    (255,255,224): 'Light Yellow', (139,69,19): 'Saddle Brown'
                }
    data.colors.update(tempDict)

def loadPart4(data):
    tempDict = {
                    (160,82,45): 'Sienna', (210,105,30): 'Chocolate',
                    (205,133,63): 'Peru', (176,196,222): 'Light Steel Blue',
                    (222,184,135): 'Burlywood', (210,180,140): 'Tan',
                    (188,143,143): 'Rosy Brown', (255,228,181): 'Moccasin',
                    (255,222,173): 'Navajo White', (255,218,185): 'Peachpuff',
                    (255,228,225): 'Misty Rose', (255,240,245):'Lavender Blush',
                    (250,240,230): 'Linen', (253,245,230): 'Old Lace',
                    (255,239,213): 'Papaya Whip', (255,245,238): 'Sea Shell',
                    (245,255,250): 'Mint Cream', (112,128,144): 'Slate Gray',
                    (119,136,153):'Light Slate Gray',(244,164,96):'Sandy Brown',
                    (230,230,250): 'Lavender', (255,250,240): 'Floral White',
                    (240,248,255): 'Alice Blue', (248,248,255): 'Ghost White',
                    (240,255,240): 'Honeydew', (255,255,240): 'Ivory',
                    (240,255,255): 'Azure', (255,250,250): 'Snow',
                    (0,0,0): 'Black', (105,105,105): 'Dim Dray',
                    (128,128,128): 'Gray', (169,169,169): 'Dark Gray',
                    (192,192,192): 'Silver', (211,211,211): 'Light Gray'
                }
    data.colors.update(tempDict)

def loadDetection(data):
    data.fileDetection = None
    data.photoDetection = None 
    data.photoDetectionW, data.photoDetectionH = None, None
    data.photoEnlargeDetection = None
    data.curColorDetection = None
    data.match1Detection = None
    data.match2Detection = None
    data.match3Detection = None

def loadTest(data):
    loadTestVariables(data)
    loadAnswers(data)
    loadColorCombos(data)
    loadCircles(data)
    loadNumbers(data)
    loadBkgColors(data)
    loadNumColors(data)
    loadButtons(data)

def loadTestVariables(data):
    data.index = 0
    data.userAns = [ ]
    data.guess = None
    data.noAns = False
    data.results = {"Correct": 0, "P": 0, "D": 0, "T": 0, "CB": 0}
    data.type = None
    data.intensity = None
    data.disclaimer = True
    data.instructions = False
    data.checked = False

def loadAnswers(data):
    # 14 random numbers for test
    answers = [ ]
    tiles = 14
    for i in range(tiles):
        sm, lg = 0, 9
        num = random.randint(sm, lg)
        answers.append(num)
    data.answers = answers

def loadColorCombos(data):
    # random order for color combinations in test
    data.colorCombos = [ ]
    gray = (100, 100, 100)
    # RGB values for background then number
    colorCombos = [ ("N", (200, 50, 100), (25, 100, 75)),
                    ("D1", gray, (110, 110, 100-15)),
                    ("T2", (125, 100, 200), (100, 100+10, 25)),
                    ("P1", gray, (100+15, 110, 110)),
                    ("T1", gray, (100, 100, 90+25)),
                    ("D2", gray, (100-10, 100, 50)),
                    ("P1", gray, (100+15, 110, 110)),
                    ("D1", gray, (110, 110, 100-15)),
                    ("T1", gray, (100, 100, 90+25)),
                    ("N", (50, 125, 75), (175+10, 50, 175)),
                    ("D1", gray, (100-20, 110, 110)),
                    ("P2", gray, (115+50, 115-10, 115)),
                    ("T1", gray, (100+10, 110, 100+50)),
                    ("P1", gray, (80+20, 90, 90)) ]
    length = len(colorCombos)
    for i in range(length):
        colorScheme = random.choice(colorCombos)
        data.colorCombos.append(colorScheme)
        colorCombos.remove(colorScheme)

def loadCircles(data):
    # fills in circles with random radiuii
    overallCenter = (150, 150)
    overallRadius = 140
    data.circles = [ ]
    # circle w/ random radius in center
    data.circles.append((150, 150, random.randint(3, 5)))
    # larger circles then smaller circles
    for varyingRaduii in [ (4, 10), (3, 4) ]:
        # go till edge of larger circle
        for radius in range(overallRadius):
            # full circle rotation
            for degree in range(360):
                radian = (degree * math.pi) / 180
                newRadius = random.randint(*varyingRaduii)
                newCX = overallCenter[0] + radius * math.cos(radian)
                newCY = overallCenter[1] + radius * math.sin(radian)
                # determine whether circle is valid or not
                count = 0
                for circle in data.circles:
                    curRadius = circle[2]
                    curCX, curCY = circle[0], circle[1]
                    if (((newCX - curCX) ** 2 + (newCY - curCY) ** 2) ** 0.5 >=
                        (newRadius + curRadius)):
                        count += 1
                # if valid, add to list
                if count == len(data.circles):
                    data.circles.append((newCX, newCY, newRadius))

def loadNumbers(data):
    # line segments that make up every number displayed in test
    # (x0, y0, x1, y1) combos for each line segment
    num0(data)
    num1(data)
    num2(data)
    num3(data)
    num4(data)
    num5(data)
    num6(data)
    num7(data)
    num8(data)
    num9(data)

def num0(data):
    data.zeroPiece = [ (100, 80, 175, 80), (175, 80, 200, 105),
                       (200, 105, 200, 180), (200, 180, 175, 210),
                       (175, 210, 100, 210), (100, 210, 75, 180),
                       (75, 180, 75, 105), (75, 105, 100, 80) ]

def num1(data):
    data.onePiece = [ (175, 75, 175, 225), (125, 100, 175, 75) ]

def num2(data):
    data.twoPiece = [ (100, 100, 130, 80), (130, 80, 175, 80),
                      (175, 80, 200, 125), (200, 125, 105, 210),
                      (105, 210, 215, 210) ]

def num3(data):
    data.threePiece = [ (110, 80, 200, 80), (200, 80, 150, 125),
                        (150, 125, 200, 160), (200, 160, 200, 185),
                        (200, 185, 170, 215), (170, 215, 125, 215),
                        (125, 215, 110, 185) ]

def num4(data):
    data.fourPiece = [ (185, 80, 85, 170), (85, 170, 205, 170),
                       (185, 80, 185, 225) ]

def num5(data):
    data.fivePiece = [ (190, 80, 100, 80), (100, 80, 100, 140),
                       (100, 140, 120, 130), (120, 130, 165, 130),
                       (165, 130, 190, 140), (190, 140, 190, 185),
                       (190, 185, 165, 210), (165, 210, 120, 210),
                       (120, 210, 100, 185) ]

def num6(data):
    data.sixPiece = [ (190, 80, 130, 80), (130, 80, 115, 140),
                      (115, 140, 155, 140), (155, 140, 180, 160),
                      (180, 160, 180, 190), (180, 190, 155, 200),
                      (155, 200, 115, 200), (115, 200, 100, 190),
                      (100, 190, 100, 160), (100, 160, 115, 140) ]

def num7(data):
    data.sevenPiece = [ (95, 80, 210, 80), (210, 80, 115, 215) ]

def num8(data):
    data.eightPiece = [ (130, 80, 180, 80), (180, 80, 200, 100),
                        (200, 100, 200, 120), (200, 120, 180, 140),
                        (180, 140, 200, 160), (200, 160, 200, 180),
                        (200, 180, 180, 200), (180, 200, 130, 200),
                        (130, 200, 110, 180), (110, 180, 110, 160),
                        (110, 160, 130, 140), (130, 140, 180, 140),
                        (130, 140, 110, 120), (110, 120, 110, 100),
                        (110, 100, 130, 80) ]

def num9(data):
    data.ninePiece = [ (105, 80, 155, 80), (155, 80, 175, 100),
                       (175, 100, 175, 250), (175, 120, 155, 140),
                       (155, 140, 105, 140), (105, 140, 85, 120),
                       (85, 120, 85, 100), (85, 100, 105, 80) ]

def loadBkgColors(data):
    # random color for every circle
    data.backgroundColors = dict()
    smDiff, lgDiff = 20, 25
    for tile in range(len(data.colorCombos)):
        data.backgroundColors[tile] = [ ]
        for circle in range(len(data.circles)):
            red, green, blue = data.colorCombos[tile][1]
            if red == 100 and green == 100 and blue == 100:
                # if gray, then use same offset so gray is maintained
                offset = random.randint(-lgDiff, lgDiff)
                red += offset
                green += offset
                blue += offset
            else:
                offset = random.randint(-smDiff, smDiff)
                red += offset
                offset = random.randint(-smDiff, smDiff)
                green += offset
                offset = random.randint(-smDiff, smDiff)
                blue += offset
            data.backgroundColors[tile].append((red, green, blue))
    # dictionary is roughly 9,00 elements after this

def loadNumColors(data):
    # random colors for circles that make up number
    data.numberColors = dict()
    for tile in range(len(data.colorCombos)):
        data.numberColors[tile] = [ ]
        num = data.answers[tile]
        if   num == 0: lines = data.zeroPiece
        elif num == 1: lines = data.onePiece
        elif num == 2: lines = data.twoPiece
        elif num == 3: lines = data.threePiece
        elif num == 4: lines = data.fourPiece
        elif num == 5: lines = data.fivePiece
        elif num == 6: lines = data.sixPiece
        elif num == 7: lines = data.sevenPiece
        elif num == 8: lines = data.eightPiece
        elif num == 9: lines = data.ninePiece
        for circle in range(len(data.circles)):
            cx, cy = data.circles[circle][0], data.circles[circle][1]
            for segment in lines:
                color = False
                x0, y0, x1, y1 = segment
                height = calculateHeight(x0, y0, x1, y1, cx, cy)
                # if circle in num, then change color from background to num
                if height != None and height <= 10:
                    type = data.colorCombos[tile][0]
                    numColor = data.colorCombos[tile][2]
                    red, green, blue = randomizeColor(type, numColor)
                    color = True
                if color == True: break
            if color == True: data.numberColors[tile].append((red, green, blue))
            else: data.numberColors[tile].append(None)

def calculateHeight(x0, y0, x1, y1, x2, y2):
    # Area of Triangle = 0.5 * base * height
    # Heron's Formula:
    #  Area of Triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    #  where p = (a + b + c) / 2
    # Solve system for height of triangle
    base = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    leg1 = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
    leg2 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # if base is not longest side then the point is beyond the end boundary
    if base < leg1 or base < leg2: return None
    p = (base + leg1 + leg2) / 2
    areaTri = (p * (p - base) * (p - leg1) * (p - leg2)) ** 0.5
    height = (2 * areaTri) / base
    return height

def loadButtons(data):
    # load number buttons in test mode
    data.radius = 25
    data.nums = [ i for i in range(10) ]
    data.numsCenters = [ ]
    margin = 10
    left = margin
    top = 300 + margin
    for num in data.nums:
        if left + 50 > 300:
            left = margin
            top = top + 50 + margin
        data.numsCenters.append((left + data.radius, top + data.radius))
        left += margin + 50

def randomNum():
    diff = 20
    return random.randint(-diff, diff)

def noneType(red, green, blue):
    if green == 100:
        red += randomNum()
        green += randomNum()
        blue += randomNum()
    else:
        green += randomNum()
        blue += randomNum()
        red = blue + 10
    return (red, green, blue)

def mildDeutan(red, green, blue):
    if red == 100:
        offset = randomNum()
        red += offset
        green += offset
        blue = green - 15
    else:
        offset = randomNum()
        green += offset
        blue += offset
        red = blue - 20
    return (red, green, blue)

def mildProtan(red, green, blue):
    if green == 100:
        offset = randomNum()
        green += offset
        blue += offset
        red = green + 15
    else:
        offset = randomNum()
        green += offset
        blue += offset
        red = green + 20
    return (red, green, blue)

def mildTritan(red, green, blue):
    if green == 90:
        offset = randomNum()
        red += offset
        green += offset
        blue = green + 25
    else:
        green += randomNum()
        red = green + 10
        blue = green + 50
    return (red, green, blue)

def randomizeColor(type, numColor):
    # for randomizing number color
    red, green, blue = numColor
    if type == "N":
        red, green, blue = noneType(red, green, blue)
    elif type == "D1":
        red, green, blue = mildDeutan(red, green, blue)
    elif type == "D2":
        green += randomNum()
        red = green - 10
        blue += randomNum()
    elif type == "P1":
        red, green, blue = mildProtan(red, green, blue)
    elif type == "P2":
        blue += randomNum()
        red = blue + 50
        green = blue - 10
    elif type == "T1":
        red, green, blue = mildTritan(red, green, blue)
    elif type == "T2":
        red += randomNum()
        green = red + 10
        blue += randomNum()
    return (red, green, blue)

def loadClassify(data):
    data.pic1Classify = None
    data.pic1ClassifyW, data.pic1ClassifyH = None, None
    data.pic1EnlargeClassify = None
    data.file1Classify = None
    data.pic1Color = None
    data.pic2Classify = None
    data.pic2ClassifyW, data.pic2ClassifyH = None, None
    data.pic2EnlargeClassify = None
    data.file2Classify = None
    data.pic2Color = None
    data.classification = None

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if   data.mode == "home":      homeMousePressed(event, data)
    elif data.mode == "test":      testMousePressed(event, data)
    elif data.mode == "results":   resultsMousePressed(event, data)
    elif data.mode == "classify":  classifyMousePressed(event, data)
    elif data.mode == "help":      helpMousePressed(event, data)
    elif data.mode == "general":   generalMousePressed(event, data)
    elif data.mode == "detection": detectionMousePressed(event, data)

def keyPressed(event, data):
    if   data.mode == "home":      homeKeyPressed(event, data)
    elif data.mode == "test":      testKeyPressed(event, data)
    elif data.mode == "results":   resultsKeyPressed(event, data)
    elif data.mode == "classify":  classifyKeyPressed(event, data)
    elif data.mode == "help":      helpKeyPessed(event, data)
    elif data.mode == "general":   generalKeyPressed(event, data)
    elif data.mode == "detection": detectionKeyPressed(event, data)

def timerFired(data):
    if   data.mode == "home":      homeTimerFired(data)
    elif data.mode == "test":      testTimerFired(data)
    elif data.mode == "results":   resultsTimerFired(data)
    elif data.mode == "classify":  classifyTimerFired(data)
    elif data.mode == "help":      helpTimerFired(data)
    elif data.mode == "general":   generalTimerFired(data)
    elif data.mode == "detection": detectionTimerFired(data)

def redrawAll(canvas, data):
    if   data.mode == "home":      homeRedrawAll(canvas, data)
    elif data.mode == "test":      testRedrawAll(canvas, data)
    elif data.mode == "results":   resultsRedrawAll(canvas, data)
    elif data.mode == "classify":  classifyRedrawAll(canvas, data)
    elif data.mode == "help":      helpRedrawAll(canvas, data)
    elif data.mode == "general":   generalRedrawAll(canvas, data)
    elif data.mode == "detection": detectionRedrawAll(canvas, data)

####################################
# home mode
####################################

def homeMousePressed(event, data):
    data.prevMode = "home"
    marginH, marginB = 20, 75
    radiusH, sizeB = 15, 125
    topUpper, topLower = 200, 350
    if (((event.x - (data.width - marginH - radiusH)) ** 2 +
        (event.y - (marginH + radiusH)) ** 2) ** 0.5 <= radiusH):
        data.mode = "help"
    elif ((event.x >= marginB and event.x <= marginB + sizeB) and
          (event.y >= topUpper and event.y <= topUpper + sizeB)):
        data.mode = "detection"
    elif ((event.x >= (data.width - marginB - sizeB) and
           event.x <= data.width - marginB) and
          (event.y >= topUpper and event.y <= topUpper + sizeB)):
        data.mode = "test"
    elif ((event.x >= marginB and event.x <= marginB + sizeB) and
          (event.y >= topLower and event.y <= topLower + sizeB)):
        data.mode = "classify"
    elif ((event.x >= (data.width - marginB - sizeB) and
           event.x <= (data.width - marginB)) and
          (event.y >= topLower and event.y <= topLower + sizeB)):
        data.mode = "general"

def homeRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawTitle(canvas, data)
    drawHelp(canvas, data)
    drawDetection(canvas, data)
    drawTest(canvas, data)
    drawPicture(canvas, data)
    drawGeneral(canvas, data)

def drawBackground(canvas, data):
    for i in range(len(data.rainbowPts)):
        top, bottom = 0, data.height
        left, right = data.rainbowPts[i][0], data.rainbowPts[i][1]
        canvas.create_rectangle(left, top, right, bottom, width = 0,
                                fill = data.rainbowL[i])

def drawTitle(canvas, data):
    canvas.create_text(data.width // 2, data.height // 5, anchor = S,
                       text = "Color Vision", font = "Arial 36 bold")
    canvas.create_text(data.width // 2, data.height // 5, anchor = N,
                       text = "Deficiency", font = "Arial 36 bold")

def drawHelp(canvas, data):
    radius, margin = 15, 20
    canvas.create_oval(data.width - margin - (2 * radius), margin,
                       data.width - margin, margin + (2 * radius), width = 3,
                       fill = "lightGray", activefill = "gray")
    canvas.create_text(data.width - margin - radius, margin + radius,
                       text = "?", font = "Arial 18 bold")

def drawDetection(canvas, data):
    margin, size = 75, 125
    top = 2 * (data.height // 5)
    canvas.create_rectangle(margin, top, margin + size, top + size,
                            fill = "white", activefill = "lightGray")
    canvas.create_text(margin + (size // 2), top + (size // 2), anchor = S,
                       text = "Color", font = "Arial 16")
    canvas.create_text(margin + (size // 2), top + (size // 2), anchor = N,
                       text = "Detection", font = "Arial 16")

def drawTest(canvas, data):
    margin, size = 75, 125
    top = 2 * (data.height // 5)
    canvas.create_rectangle(data.width - margin - size, top,
                            data.width - margin, top + size, fill = "white",
                            activefill = "lightGray")
    canvas.create_text(data.width - margin - (size // 2), top + (size // 2),
                       anchor = S, text = "Color Vision", font = "Arial 16")
    canvas.create_text(data.width - margin - (size // 2), top + (size // 2),
                       anchor = N, text = "TEST", font = "Arial 16")

def drawPicture(canvas, data):
    margin, size = 75, 125
    top = 7 * (data.height // 10)
    canvas.create_rectangle(margin, top, margin + size, top + size,
                            fill = "white", activefill = "lightGray")
    canvas.create_text(margin + (size // 2), top + (size // 2), anchor = S,
                       text = "Color", font = "Arial 16")
    canvas.create_text(margin + (size // 2), top + (size // 2), anchor = N,
                       text = "Classification", font = "Arial 15")

def drawGeneral(canvas, data):
    margin, size = 75, 125
    top = 7 * (data.height // 10)
    canvas.create_rectangle(data.width - margin - size, top,
                            data.width - margin, top + size, fill = "white",
                            activefill = "lightGray")
    canvas.create_text(data.width - margin - (size // 2), top + (size // 2),
                       anchor = S, text = "General", font = "Arial 16")
    canvas.create_text(data.width - margin - (size // 2), top + (size // 2),
                       anchor = N, text = "Information", font = "Arial 16")

def homeTimerFired(data):
    # 'move' colors in background
    for i in range(len(data.rainbowPts)):
        left, right = data.rainbowPts[i][0], data.rainbowPts[i][1]
        left += 5
        right += 5
        if i == 0: left = 5
        elif i == len(data.rainbowPts) - 1: right = data.width - 5
        data.rainbowPts[i] = (left, right)
    data.counter += 1
    data.counter %= (((data.width // (len(data.rainbowPts) - 1)) - 1) // 5)
    if data.counter == 0:
        loadRainbowPts(data)
        temp = data.rainbowL[:-1]
        data.rainbowL = [temp[-1]] + temp
 
def homeKeyPressed(event, data):
    pass

####################################
# test mode
####################################

def testMousePressed(event, data):
    if data.disclaimer:
        # separate mouse pressed for disclaimer
        disclaimerMousePressed(event, data)
    elif data.instructions:
        # separate mouse pressed for instuctions
        instructionMousePressed(event, data)
    else:
        for num in data.nums:
            cx, cy = data.numsCenters[num][0], data.numsCenters[num][1]
            if ((event.x - cx) ** 2 + (event.y - cy) ** 2) ** 0.5 < data.radius:
                data.noAns = False
                if not isinstance(data.guess, int): data.guess = num
                else: data.guess = num
        if ((event.x >= 350 and event.x <= 450) and
            (event.y >= 175 and event.y <= 200)):
            if data.guess != None: submit(data)
            else: data.noAns = True
        elif ((event.x >= 10 and event.x <= 130) and
            (event.y >= 430 and event.y <= 455)):
            data.noAns = False
            data.guess = "Unsure"
        elif ((event.x >= 140 and event.x <= 260) and
            (event.y >= 430 and event.y <= 455)):
            data.noAns = False
            data.guess = "Nothing"

def disclaimerMousePressed(event, data):
    # must check box before able to continue
    if 50 <= event.x <= 60 and 250 <= event.y <= 260:
        data.checked = True
    elif data.checked:
        if 415 <= event.x <= data.width and 480 <= event.y <= data.height:
            data.disclaimer = False
            data.instructions = True

def instructionMousePressed(event, data):
    if 415 <= event.x <= data.width and 480 <= event.y <= data.height:
        data.instructions = False

def testKeyPressed(event, data):
    # can use keys or mouse presses to go through test
    if not data.disclaimer and not data.instructions:
        if event.char.isdigit():
            data.noAns = False
            if not isinstance(data.guess, int): data.guess = int(event.char)
            else: data.guess = int(event.char)
        elif event.keysym == "Return":
            if data.guess != None: submit(data)
            else: data.noAns = True
        elif event.keysym == "BackSpace":
            data.noAns = True
            data.guess = None

def submit(data):
    data.userAns.append(data.guess)
    checkAns(data)
    data.guess = None
    data.index += 1
    if data.index == len(data.colorCombos):
        determineType(data)
        data.index = 0
        data.mode = "results"

def checkAns(data):
    # correct!
    if data.guess == data.answers[data.index]:
        data.results['Correct'] += 1
    else:
        # wrong :(
        colorType = data.colorCombos[data.index][0]
        # add to color blind independent of specific type
        data.results['CB'] += 1
        # check if it is universal to them all, then add 1 to all three types
        if colorType == 'N':
            # not specific to any type
            pass
        else:
            # one of the three types
            data.results[colorType[0]] += int(colorType[1])

def determineType(data):
    if data.results['CB'] >= 13:
        # total color blind
        data.type = 'CB'
    elif data.results['Correct'] >= 14:
        # no color vision deficiency
        data.type = None
    else:
        # one of the three types
        for key, value in data.results.items():
            if   key == 'P': pro = value
            elif key == 'D': deu = value
            elif key == 'T': tri = value
        if deu >= pro and deu >= tri:
            data.type = 'D'
        elif pro >= deu and pro >= tri:
            data.type = 'P'
        else:
            data.type = 'T'
        if data.results[data.type] >= 4:
            data.intensity = "hi"
        else:
            data.intensity = "lo"

def testRedrawAll(canvas, data):
    if data.disclaimer:
        drawDisclaimer(canvas, data)
    elif data.instructions:
        drawInstructions(canvas, data)
    else:
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill = "lightBlue", width = 0)
        canvas.create_rectangle(0, 0, 300, 300, fill = "black")
        drawCircles(canvas, data)
        drawFancy(canvas, data)
        drawButtons(canvas, data)

def drawDisclaimer(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width // 2, 30, text = "DISCLAIMER", fill = "white",
                       font = "Arial 24 bold")
    s = """
    The test you are about to take is not approved by a
    licensed optometrist nor is in anyway an official
    color vision test. The test was created for the
    intention of hoping to shed some light on what
    condition (if any) a user MAY POTENTIALLY have. For
    an official color vision test, see a licensed
    optometrist.
    """
    canvas.create_text(0, 35, anchor = NW, font = "Arial 14", fill = "white",
                       text = s)
    canvas.create_rectangle(50, 250, 60, 260, fill = "white")
    s = "I have fully read and fully understand the above disclaimer"
    canvas.create_text(65, 255, anchor = W, fill = "white",
                       text = s, font = "Arial 12")
    if data.checked:
        canvas.create_text(55, 256, text = "X", font = "Arial 16")
        canvas.create_text(data.width, data.height, anchor = SE,
                           text = "Continue", fill = "white", font = "Arial 16")

def drawInstructions(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "lightBlue")
    canvas.create_text(data.width // 2, 30, text = "Instructions",
                       font = "Arial 24")
    canvas.create_text(data.width, data.height, anchor = SE,
                       text = "Continue", font = "Arial 16")
    s = """
    You are about to take the test. The test
    contains 14 slides. Each slide contains a
    one digit number amongst the circles. It
    is your job to discern what number it is.
    You can type the number and hit enter or
    press on the circle of the number then
    press on submit. There are also options
    for being unsure of the number and seeing
    no number. Please be honest when you take
    the test as not being honest, may skew
    your results.
    """
    canvas.create_text(0, 40, anchor = NW, font = "Arial 16", text = s)

def drawCircles(canvas, data):
    bkgColors = data.backgroundColors[data.index]
    numColor = data.numberColors[data.index]
    for circle in range(len(data.circles)):
        color = numColor[circle]
        if color == None:
            color = bkgColors[circle]
        cx, cy = data.circles[circle][0], data.circles[circle][1]
        radius = data.circles[circle][2]
        canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius,
                           fill = rgbString(*color))

def drawFancy(canvas, data):
    canvas.create_rectangle(325, 100, 475, 150, fill = "white", width = 0)
    if data.guess != None:
        canvas.create_text(400, 125, text = str(data.guess), font = "Arial 24")
    canvas.create_rectangle(350, 175, 450, 200, fill = "red")
    canvas.create_text(400, 187, text = "Submit", font = "Arial 16")
    if data.noAns:
        canvas.create_text(400, 220, 
                           text = "Please enter a response.")

def drawButtons(canvas, data):
    for num in data.nums:
        cx, cy = data.numsCenters[num][0], data.numsCenters[num][1]
        canvas.create_oval(cx - data.radius, cy - data.radius,
                           cx + data.radius, cy + data.radius, fill = "green")
        canvas.create_text(cx, cy, text = str(num), font = "Arial 24")
    canvas.create_rectangle(10, 430, 130, 455, fill = "yellow")
    canvas.create_text(70, 442, text = "Unsure")
    canvas.create_rectangle(140, 430, 260, 455, fill = "yellow")
    canvas.create_text(200, 442, text = "I see no number")

def testTimerFired(data):
    pass

####################################
# classify mode
####################################

def classifyMousePressed(event, data):
    marginH, radiusH, heightB, widthB, loadW, loadH = 20, 15, 30, 75, 100, 25
    if (((event.x - (data.width - marginH - radiusH)) ** 2 +
        (event.y - (data.height - marginH - radiusH)) ** 2) ** 0.5 <= radiusH):
        data.prevMode = "classify"
        data.mode = "help"
    elif (event.x <= widthB and event.y >= data.height - heightB):
        data.mode = "home"
    elif (75 <= event.x <= 75 + loadW) and (265 <= event.y <= 265 + loadH):
        loadPicture1(data)
    elif (325 <= event.x <= 325 + loadW) and (265 <= event.y <= 265 + loadH):
        loadPicture2(data)
    elif (data.pic1Classify != None and
          (((250 - data.pic1ClassifyW) // 2) <= event.x
           <= ((250 - data.pic1ClassifyW) // 2) + data.pic1ClassifyW and
           ((250 - data.pic1ClassifyH) // 2) <= event.y
           <= ((250 - data.pic1ClassifyH) // 2) + data.pic1ClassifyH)):
        enlargePic1(event, data)
    elif (data.pic2Classify != None and
          (((250 - data.pic2ClassifyW) // 2) + 250 <= event.x
           <= ((250 - data.pic2ClassifyW) // 2) + data.pic2ClassifyW + 250 and
           ((250 - data.pic2ClassifyH) // 2) <= event.y
           <= ((250 - data.pic2ClassifyH) // 2) + data.pic2ClassifyH)):
        enlargePic2(event, data)
    elif (data.pic1EnlargeClassify != None and
          (20 <= event.x <= 120 and 300 <= event.y <= 400)):
        determineColor1(event, data)
    elif (data.pic2EnlargeClassify != None and
          (380 <= event.x <= 480 and 300 <= event.y <= 400)):
        determineColor2(event, data)

def loadPicture1(data):
    # able to accept jpg, png, and gif files for photos
    filepath =  filedialog.askopenfilename(initialdir = "/",
                            title = "Select photo file",
                            filetypes = (("jpeg files" , "*.jpg"),
                                         ("png files" , "*.png"),
                                         ("gif files", "*.gif")))
    data.file1Classify = filepath
    newSize = (250, 250)
    img = Image.open(data.file1Classify)
    # resize photos
    img.thumbnail(newSize)
    data.pic1ClassifyW, data.pic1ClassifyH = img.size
    data.pic1Classify = ImageTk.PhotoImage(img)

def loadPicture2(data):
    filepath =  filedialog.askopenfilename(initialdir = "/",
                            title = "Select photo file",
                            filetypes = (("jpeg files" , "*.jpg"),
                                         ("png files" , "*.png"),
                                         ("gif files", "*.gif")))
    data.file2Classify = filepath
    newSize = (250, 250)
    img = Image.open(data.file2Classify)
    img.thumbnail(newSize)
    data.pic2ClassifyW, data.pic2ClassifyH = img.size
    data.pic2Classify = ImageTk.PhotoImage(img)

def enlargePic1(event, data):
    x = event.x - ((250 - data.pic1ClassifyW) // 2)
    y = event.y - ((250 - data.pic1ClassifyH) // 2)
    # need to reopen and save image then crop and save again
    img = Image.open(data.file1Classify)
    img.thumbnail((250, 250))
    img.save('mod1.jpg')
    croppedImg = Image.open('mod1.jpg')
    croppedImg = croppedImg.crop((x - 15, y - 15, x + 15, y + 15))
    newImg = croppedImg.resize((100, 100))
    newImg.save('moded1.jpg')
    data.pic1EnlargeClassify = ImageTk.PhotoImage(newImg)

def enlargePic2(event, data):
    x = event.x - 250 - ((250 - data.pic2ClassifyW) // 2) 
    y = event.y - ((250 - data.pic2ClassifyH) // 2)
    img = Image.open(data.file2Classify)
    img.thumbnail((250, 250))
    img.save('mod2.jpg')
    croppedImg = Image.open('mod2.jpg')
    croppedImg = croppedImg.crop((x - 15, y - 15, x + 15, y + 15))
    newImg = croppedImg.resize((100, 100))
    newImg.save('moded2.jpg')
    data.pic2EnlargeClassify = ImageTk.PhotoImage(newImg)

def determineColor1(event, data):
    img = Image.open('moded1.jpg')
    # access pixels for RGB values
    pixels = img.load()
    data.pic1Color = pixels[event.x - 20, event.y - 300]
    if data.pic2Color != None:
        classifyColors(data)

def determineColor2(event, data):
    img = Image.open('moded2.jpg')
    pixels = img.load()
    data.pic2Color = pixels[event.x - 380, event.y - 300]
    if data.pic1Color != None:
        classifyColors(data)

def classifyColors(data):
    red1, green1, blue1 = data.pic1Color
    red2, green2, blue2 = data.pic2Color
    if ((red1 - 3 <= red2 <= red1 + 3) and
        (green1 - 3 <= green2 <= green1 + 3) and
        (blue1 - 3 <= blue2 <= blue1 + 3)):
        # small buffer for 'exactly' the same
        data.classification = "Exact same color"
    elif ((red1 - 8 <= red2 <= red1 + 8) and
          (green1 - 8 <= green2 <= green1 + 8) and
          (blue1 - 8 <= blue2 <= blue1 + 8)):
        # medium buffer for 'nearly' the same
        data.classification = "Nearly same color"
    elif ((red1 - 15 <= red2 <= red1 + 15) and
          (green1 - 15 <= green2 <= green1 + 15) and
          (blue1 - 15 <= blue2 <= blue1 + 15)):
        # larger buffer for 'similar' color
        data.classification = "Similar color"
    elif (findColorName(data, *data.pic1Color) ==
          findColorName(data, *data.pic2Color)):
        # if name is same, then similar colors
        data.classification = "Similar color"
    elif matching(red1, green1, blue1, red2, green2, blue2):
        data.classification = "Matching"
    else:
        # if all else fails, then no relationship
        data.classification = "No Relationship"

def matching(red1, green1, blue1, red2, green2, blue2):
    hsv1 = RGBtoHSV(red1, green1, blue1)
    hsv2 = RGBtoHSV(red2, green2, blue2)
    # must compare hur values to determine matching
    hue1, hue2 = hsv1[0], hsv2[0]
    hueComparable = (hue1 + (1/2)) % 1
    if hueComparable - 0.05 <= hue2 <= hueComparable + 0.05:
        return True
    hueComparable = (hue1 + (5 / 12)) % 1
    if hueComparable - 0.05 <= hue2 <= hueComparable + 0.05:
        return True
    hueComparable = (hue1 + (7 / 12)) % 1
    if hueComparable - 0.05 <= hue2 <= hueComparable + 0.05:
        return True
    return False

def classifyRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill = "lightBlue", width = 0)
    drawHelpAtBottom(canvas, data)
    drawBack(canvas, data)
    drawPics(canvas, data)
    drawColors(canvas, data)
    drawClassification(canvas, data)

def drawHelpAtBottom(canvas, data):
    radius, margin = 15, 20
    canvas.create_oval(data.width - margin - (2 * radius),
                       data.height - margin - (2 * radius),
                       data.width - margin, data.height - margin, width = 3,
                       fill = "lightGray", activefill = "gray")
    canvas.create_text(data.width - margin - radius, 
                       data.height - margin - radius,
                       text = "?", font = "Arial 18 bold")

def drawPics(canvas, data):
    canvas.create_rectangle(0, 0, 250, 250, fill = "lightGray")
    canvas.create_rectangle(250, 0, 500, 250, fill = "lightGray")
    canvas.create_rectangle(75, 265, 175, 290,
                            fill = "lightGray", activefill = "gray")
    canvas.create_text(125, 277, text = "Upload Image")
    canvas.create_rectangle(325, 265, 425, 290,
                            fill = "lightGray", activefill = "gray")
    canvas.create_text(375, 277, text = "Upload Image")
    if data.pic1Classify != None:
        # center newly resized image
        canvas.create_image((250 - data.pic1ClassifyW) // 2,
                            (250 - data.pic1ClassifyH) // 2,
                            anchor = NW, image = data.pic1Classify)
    if data.pic2Classify != None:
        canvas.create_image(((250 - data.pic2ClassifyW) // 2) + 250,
                            (250 - data.pic2ClassifyH) // 2,
                            anchor = NW, image = data.pic2Classify)
    if data.pic1EnlargeClassify != None:
        canvas.create_image(20, 300, anchor = NW,
                            image = data.pic1EnlargeClassify)
    if data.pic2EnlargeClassify != None:
        canvas.create_image(data.width - 20, 300, anchor = NE,
                            image = data.pic2EnlargeClassify)

def drawColors(canvas, data):
    if data.pic1Color != None:
        canvas.create_rectangle(150, 325, 200, 375,
                                fill = rgbString(*data.pic1Color))
        canvas.create_text(175, 375, anchor = N,
                           text = findColorName(data, *data.pic1Color))
    if data.pic2Color != None:
        canvas.create_rectangle(300, 325, 350, 375,
                                fill = rgbString(*data.pic2Color))
        canvas.create_text(325, 375, anchor = N,
                           text = findColorName(data, *data.pic2Color))

def drawClassification(canvas, data):
    if data.classification != None:
        canvas.create_text(data.width // 2, 425, text = "Classification:",
                           font = "Arial 18")
        canvas.create_text(data.width // 2, 460, text = data.classification,
                           font = "Arial 24")

def classifyKeyPressed(event, data):
    pass

def classifyTimerFired(data):
    pass

####################################
# results mode
####################################

def resultsMousePressed(event, data):
    heightB, widthB = 30, 75
    if (event.x <= widthB and event.y >= data.height - heightB):
        data.prevMode = "test"
        loadTestVariables(data)
        data.mode = "home"

def resultsKeyPressed(event, data):
    pass

def resultsTimerFired(data):
    pass

def resultsRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill = "lightBlue", width = 0)
    canvas.create_text(10, 35, anchor = W, text = "Your results are:",
                       font = "Arial 20")
    # show info on certain types that are diagnosed
    if data.type == None:
        canvas.create_text(data.width // 2, 75, text =
                           "No Color Vision Deficiency", font = "Arial 20")
    elif data.type == 'CB':
        canvas.create_text(data.width // 2, 75, font = "Arial 20",
                           text = "You may suffer from total color blindness")
        drawCBInfo(canvas)
    else:
        drawTypeInfo(canvas, data)
    drawBack(canvas, data)

def drawCBInfo(canvas):
    s = """
    This is a serious condition. The two different options
    are below. PLEASE go see an optometrist for further testing.
    
    Cone monochromacy: This results from a failure of two of the
    three cone cell photopigments to work. There is red cone
    monochromacy, green cone monochromacy, and blue cone
    monochromacy. People with cone monochromacy have trouble
    distinguishing colors because the brain needs to compare the
    signals from different types of cones in order to see color.
    When only one type of cone works, this comparison isn’t possible.
    
    Rod monochromacy or achromatopsia: None of the cone cells have
    functional photopigments. Lacking all cone vision, people with
    rod monochromacy see the world in black, white, and gray. And
    since rods respond to dim light, people with rod monochromacy
    tend to be photophobic – very uncomfortable in bright environments.
    They also experience nystagmus.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawTypeInfo(canvas, data):
    if data.type == 'D':
        if data.intensity == 'hi':
            drawDH(canvas, data)
        else:
            drawDL(canvas, data)
    elif data.type == 'P':
        if data.intensity == 'hi':
            drawPH(canvas, data)
        else:
            drawPL(canvas, data)
    elif data.type == 'T':
        if data.intensity == 'hi':
            drawTH(canvas, data)
        else:
            drawTL(canvas, data)

def drawDH(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Strong Deutan")
    s = """
    Deuteranopia (Strong Deutan): In people with deuteranopia,
    there are no working green cone cells. They tend to see reds as
    brownish-yellow and greens as beige. Deuteranopia is an X-linked
    disorder that affects about 1 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawDL(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Mild Deutan")
    s = """
    Deuteuranomaly (Mild Deutan): In people with deuteranomaly,
    the green cone photopigment is abnormal. Yellow and green appear
    redder and it is difficult to tell violet from blue. This
    condition is mild and doesn’t interfere with daily living.
    Deuteranomaly is the most common form of color blindness and
    is an X-linked disorder affecting 5 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawPH(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Strong Protan")
    s = """
    Protanopia (Strong Protan): In people with protanopia, there are no
    working red cone cells. Red appears as black. Certain shades of
    orange, yellow, and green all appear as yellow. Protanopia is an
    X-linked disorder that is estimated to affect 1 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawPL(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Mild Protan")
    s = """
    Protanomaly (Mild Protan): In people with protanomaly, the red cone
    photopigment is abnormal. Red, orange, and yellow appear greener
    and colors are not as bright. This condition is mild and doesn’t
    usually interfere with daily living. Protanomaly is an X-linked
    disorder estimated to affect 1 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawTH(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Strong Tritan")
    s = """
    Tritanopia (Strong Tritan): People with tritanopia, also known as
    blue-yellow color blindness, lack blue cone cells. Blue appears
    green and yellow appears violet or light grey. Tritanopia is an
    extremel rare autosomal recessive disorder affecting males and
    females equally.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

def drawTL(canvas, data):
    canvas.create_text(data.width // 2, 75, font = "Arial 20", text =
                       "You may suffer from Mild Tritan")
    s = """
    Tritanomaly (Mild Tritan): People with tritanomaly have
    functionally limited blue cone cells. Blue appears greener and
    it can be difficult to tell yellow and red from pink. Tritanomaly
    is extremely rare. It is an autosomal dominant disorder affecting
    males and females equally.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 100, anchor = NW, text = s, font = "Arial 12")

####################################
# help mode
####################################

def helpMousePressed(event, data):
    heightB, widthB = 30, 75
    if (event.x <= widthB and event.y >= data.height - heightB):
        data.mode = data.prevMode

def helpKeyPressed(event, data):
    pass

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill = "lightBlue", width = 0)
    drawBack(canvas, data)
    canvas.create_text(data.width / 2, 25, text = "Help", font = "Arial 24")
    # different help screens for the various modes
    if data.prevMode == "home":
        drawHomeHelp(canvas, data)
    elif data.prevMode == "detection":
        drawDetectionHelp(canvas, data)
    elif data.prevMode == "classify":
        drawClassifyHelp(canvas, data)

def drawBack(canvas, data):
    height, width = 30, 75
    canvas.create_rectangle(2, data.height - height, width, data.height,
                            fill = "lightGray", activefill = "gray")
    canvas.create_text(width // 2, data.height - (height // 2),
                       text = "Back", font = "Arial 18")

def drawHomeHelp(canvas, data):
    drawIntro(canvas, data)
    drawHomeHelp1(canvas, data)
    s = """
    The color detection area can determine any color within an image.
    The user is able to upload a picture and tap on the image to
    determine the color along with matching colors, of the selected area.
    """
    canvas.create_text(-7, 375, anchor = W, text = s, font = "Arial 12")
    canvas.create_text(5, 415, anchor = W, text = "Classification",
                       font = "Arial 16 bold")
    s = """
    The classification part of the application allows a user to upload
    two pictures and determine if colors are similar or matching
                                    between the two picures.
    """
    canvas.create_text(-7, 450, anchor = W, text = s, font = "Arial 12")

def drawIntro(canvas, data):
    s = """
    Welcome to my application concerning Color Vision Deficiency (or
    more commonly and incorrectly known as 'Color Blindness'). Below are
    listed the choices you can navigate to from the home screen. Enjoy!
    """
    canvas.create_text(-7, 75, anchor = W, text = s, font = "Arial 12")
    canvas.create_text(data.width - 2, 115, anchor = E,
                       text = "-Preston Vander Vos", font = "Arial 12")
    canvas.create_text(5, 130, anchor = W, text = "General Information",
                       font = "Arail 16 bold")

def drawHomeHelp1(canvas, data):
    s = """
    The general information page gives specific details about what
    exactly color vision deficiency is. It also describes the four types
    of color vision deficiency.
    """
    canvas.create_text(-7, 167, anchor = W, text = s, font = "Arial 12")
    canvas.create_text(5, 208, anchor = W, text = "Take Test",
                       font = "Arial 16 bold")
    s = """
    The testing feature allows you to take a color vision test. The test
    will determine what color vision deficiency (if any) a person may have.
                                                DISCLAIMER...
    The test is not approved by a licensed optometrist! It is not
    guaranteed to give an accurate result. For an accurate color vision
    test please see a licensed optometrist.
    """
    canvas.create_text(-7, 273, anchor = W, text = s, font = "Arial 12")
    canvas.create_text(5, 340, anchor = W, text = "Color Detection",
                       font = "Arial 16 bold")

def drawDetectionHelp(canvas, data):
    s = """
    Step 1: Use the 'Upload Image' button to select a photo file
                  from your computer. Acceptable files are jpg, png, or gif.
    Step 2: Tap on the image to view a close-up of the area you pressed.
    Step 3: Tap on the enlarged picture to find out the color at
                  that location and the colors which match that color.
    """
    canvas.create_text(-7, 150, anchor = W, text = s, font = "Arial 12")
    s = """
    Question: Why are the matching colors the same as the current
    color for whites, grays, and blacks?
    
    Answer: Whites, grays, and blacks can go with any color.
    """
    canvas.create_text(-7, 250, anchor = W, text = s, font = "Arial 12")

def drawClassifyHelp(canvas, data):
    s = """
    Step 1: Use the 'Upload Image' buttons to select two photo files
                  from your computer. Acceptable files are jpg, png, or gif.
    Step 2: Tap on both images to view close-ups of the areas you
                  pressed.
    Step 3: Tap on both enlarged pictures to find what colors are at
                  the locations you pressed. Then, the application
                  will determine whether the colors are the same,
                  similar, matching, or have no relationship.
    """
    canvas.create_text(-7, 150, anchor = W, text = s, font = "Arial 12")

####################################
# general mode
####################################

def generalMousePressed(event, data):
    marginH, radiusH = 20, 15
    heightB, widthB = 30, 75
    if (event.x <= widthB and event.y >= data.height - heightB):
        data.mode = data.prevMode
    elif ((data.width // 2 - 40 <= event.x <= data.width // 2 - 10) and
          (data.height - 35 <= event.y <= data.height - 5) and
          data.generalScreen != 0):
        data.generalScreen -= 1
    elif ((data.width // 2 + 10 <= event.x <= data.width // 2 + 40) and
          (data.height - 35 <= event.y <= data.height - 5) and
          data.generalScreen != 5):
        data.generalScreen += 1

def generalKeyPressed(event, data):
    pass

def generalTimerFired(data):
    pass

def generalRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill = "lightBlue", width = 0)
    drawBack(canvas, data)
    drawArrows(canvas, data)
    drawInformation(canvas, data)

def drawArrows(canvas, data):
    # arrows are grayed out when you cannot proceed any further that way
    if data.generalScreen == 0: colorLeft = "gray"
    else: colorLeft = "black"
    if data.generalScreen == 5: colorRight = "gray"
    else: colorRight = "black"
    canvas.create_rectangle(data.width // 2 - 30, data.height - 25,
                            data.width // 2 - 10, data.height - 15,
                            fill = colorLeft, width = 0)
    canvas.create_rectangle(data.width // 2 + 10, data.height - 25,
                            data.width // 2 + 30, data.height - 15,
                            fill = colorRight, width = 0)
    canvas.create_polygon(data.width // 2 - 40, data.height - 20,
                          data.width // 2 - 30, data.height - 35,
                          data.width // 2 - 30, data.height - 5,
                          fill = colorLeft)
    canvas.create_polygon(data.width // 2 + 40, data.height - 20,
                          data.width // 2 + 30, data.height - 35,
                          data.width // 2 + 30, data.height - 5,
                          fill = colorRight)

def drawInformation(canvas, data):
    # everything has the souce that the info was pulled from
    if data.generalScreen == 0:
        drawWhat(canvas, data)
    elif data.generalScreen == 1:
        drawWho(canvas, data)
    elif data.generalScreen == 2:
        drawDeutan(canvas, data)
    elif data.generalScreen == 3:
        drawProtan(canvas, data)
    elif data.generalScreen == 4:
        drawTritan(canvas, data)
    elif data.generalScreen == 5:
        drawColorBlind(canvas, data)

def drawWhat(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "What is Color Vision Deficiency?")
    s = """
    Most of us share a common color vision sensory experience. Some
    people, however, have a color vision deficiency, which means their
    perception of colors is different from what most of us see. The most
    severe forms of these deficiencies are referred to as color blindness.
    People with color blindness aren’t aware of differences among colors
    that are obvious to the rest of us. People who don’t have the more
    severe types of color blindness may not even be aware of their
    condition unless they’re tested in a clinic or laboratory. Inherited
    color blindness is caused by abnormal photopigments. These
    color-detecting molecules are located in cone-shaped cells within the
    retina, called cone cells. In humans, several genes are needed for the
    body to make photopigments, and defects in these genes can lead to
    color blindness. There are three main kinds of color blindness, based
    on photopigment defects in the three different kinds of cones that
    respond to blue, green, and red light. Red-green color blindness is
    the most common, followed by blue-yellow color blindness. A complete
    absence of color vision —total color blindness – is rare. Sometimes
    color blindness can be caused by physical or chemical damage to the
    eye, the optic nerve, or parts of the brain that process color
    information. Color vision can also decline with age, most often
    because of cataract - a clouding and yellowing of the eye’s lens.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

def drawWho(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "Who gets Color Vision Deficiency?")
    s = """
    As many as 8 percent of men and 0.5 percent of women with
    Northern European ancestry have the common form of red-green
    color blindness. Men are much more likely to be colorblind than
    women because the genes responsible for the most common,
    inherited color blindness are on the X chromosome. Males only
    have one X chromosome, while females have two X chromosomes.
    In females, a functional gene on only one of the X chromosomes
    is enough to compensate for the loss on the other. This kind of
    inheritance pattern is called X-linked, and primarily affects
    males. Inherited color blindness can be present at birth, begin
    in childhood, or not appear until the adult years.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

def drawDeutan(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "Deutan")
    s = """
    Deuteuranomaly: In people with deuteranomaly, the green cone
    photopigment is abnormal. Yellow and green appear redder and it
    is difficult to tell violet from blue. This condition is mild
    and doesn’t interfere with daily living. Deuteranomaly is the
    most common form of color blindness and is an X-linked disorder
    affecting 5 percent of males.
    
    Deuteranopia: In people with deuteranopia, there are no working
    green cone cells. They tend to see reds as brownish-yellow and
    greens as beige. Deuteranopia is an X-linked disorder that affects
    about 1 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

def drawProtan(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "Protan")
    s = """
    Protanomaly: In people with protanomaly, the red cone photopigment
    is abnormal. Red, orange, and yellow appear greener and colors are
    not as bright. This condition is mild and doesn’t usually interfere
    with daily living. Protanomaly is an X-linked disorder estimated to
    affect 1 percent of males.
    
    Protanopia: In people with protanopia, there are no working red
    cone cells. Red appears as black. Certain shades of orange, yellow,
    and green all appear as yellow. Protanopia is an X-linked disorder
    that is estimated to affect 1 percent of males.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

def drawTritan(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "Tritan")
    s = """
    Tritanomaly: People with tritanomaly have functionally limited
    blue cone cells. Blue appears greener and it can be difficult to
    tell yellow and red from pink. Tritanomaly is extremely rare. It
    is an autosomal dominant disorder affecting males and females
    equally.
    
    Tritanopia: People with tritanopia, also known as blue-yellow
    color blindness, lack blue cone cells. Blue appears green and
    yellow appears violet or light grey. Tritanopia is an extremely
    rare autosomal recessive disorder affecting males and females
    equally.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

def drawColorBlind(canvas, data):
    canvas.create_text(data.width // 2, 20, font = "Arial 24",
                       text = "Total Color Blindness")
    s = """
    Cone monochromacy: This rare form of color blindness results
    from a failure of two of the three cone cell photopigments to
    work. There is red cone monochromacy, green cone monochromacy,
    and blue cone monochromacy. People with cone monochromacy have
    trouble distinguishing colors because the brain needs to compare
    the signals from different types of cones in order to see color.
    When only one type of cone works, this comparison isn’t possible.
    People with blue cone monochromacy, may also have reduced visual
    acuity, near-sightedness, and uncontrollable eye movements, a
    condition known as nystagmus. Cone monochromacy is an autosomal
    recessive disorder.
    
    Rod monochromacy or achromatopsia: This type of monochromacy is
    rare and is the most severe form of color blindness. It is present
    at birth. None of the cone cells have functional photopigments.
    Lacking all cone vision, people with rod monochromacy see the world
    in black, white, and gray. And since rods respond to dim light,
    people with rod monochromacy tend to be photophobic – very
    uncomfortable in bright environments. They also experience
    nystagmus. Rod monochromacy is an autosomal recessive disorder.
    
    Source: https://nei.nih.gov/health/color_blindness/facts_about
    """
    canvas.create_text(0, 30, anchor = NW, text = s, font = "Arial 12")

####################################
# detection mode
####################################

def detectionMousePressed(event, data):
    marginH, radiusH, heightB, widthB, picH, picW = 20, 15, 30, 75, 300, 300
    topLoad, leftLoad, loadW, loadH = 75, 380, 100, 25
    if (((event.x - (data.width - marginH - radiusH)) ** 2 +
        (event.y - (marginH + radiusH)) ** 2) ** 0.5 <= radiusH):
        data.prevMode = "detection"
        data.mode = "help"
    elif (event.x <= widthB and event.y >= data.height - heightB):
        data.prevMode = "detection"
        data.mode = "home"
    elif (data.photoDetection != None and (((300 - data.photoDetectionW) // 2)
          <= event.x <= (((300 - data.photoDetectionW) // 2)
          + data.photoDetectionW) and ((300 - data.photoDetectionH) // 2)
          <= event.y <= (((300 - data.photoDetectionH) // 2) + 
          data.photoDetectionH))):
        enlargePicDetection(event, data)
    elif ((event.x >= leftLoad and event.x <= leftLoad + loadW) and
          (event.y >= topLoad and event.y <= topLoad + loadH)):
        loadDetectionPic(data)
    elif (data.photoEnlargeDetection != None and
          (350 <= event.x <= 450 and 150 <= event.y <= 250)):
        img = Image.open('moded.jpg')
        # access pixels at specific location
        pixels = img.load()
        data.curColorDetection = pixels[event.x - 350, event.y - 150]
        determineOtherColors(data)

def enlargePicDetection(event, data):
    x = event.x - ((300 - data.photoDetectionW) // 2)
    y = event.y - ((300 - data.photoDetectionH) // 2)
    # must reopen image, modify it save, then display it
    img = Image.open(data.fileDetection)
    img.thumbnail((300, 300))
    img.save('mod.jpg')
    croppedImg = Image.open('mod.jpg')
    croppedImg = croppedImg.crop((x - 15, y - 15, x + 15, y + 15))
    newImg = croppedImg.resize((100, 100))
    newImg.save('moded.jpg')
    data.photoEnlargeDetection = ImageTk.PhotoImage(newImg)

def loadDetectionPic(data):
    filepath =  filedialog.askopenfilename(initialdir = "/",
                            title = "Select photo file",
                            filetypes = (("jpeg files" , "*.jpg"),
                                         ("png files" , "*.png"),
                                         ("gif files", "*.gif")))
    data.fileDetection = filepath
    newSize = (300, 300)
    img = Image.open(data.fileDetection)
    img.thumbnail(newSize)
    data.photoDetectionW, data.photoDetectionH = img.size
    data.photoDetection = ImageTk.PhotoImage(img)

def determineOtherColors(data):
    # determining matching colors
    originalRed, originalGreen, originalBlue = data.curColorDetection
    # convert to HSV
    hsvOld = RGBtoHSV(originalRed, originalGreen, originalBlue)
    hueOld = hsvOld[0]
    # alter hue via split complimentary rule
    hueMatch1 = (hueOld + (1 / 2)) % 1
    hueMatch2 = (hueOld + (5 / 12)) % 1
    hueMatch3 = (hueOld + (7 / 12)) % 1
    # convert back to RGB from HSV
    match1Red, match1Green, match1Blue = HSVtoRGB(hueMatch1,hsvOld[1],hsvOld[2])
    match2Red, match2Green, match2Blue = HSVtoRGB(hueMatch2,hsvOld[1],hsvOld[2])
    match3Red, match3Green, match3Blue = HSVtoRGB(hueMatch3,hsvOld[1],hsvOld[2])
    data.match1Detection = (match1Red, match1Green, match1Blue)
    data.match2Detection = (match2Red, match2Green, match2Blue)
    data.match3Detection = (match3Red, match3Green, match3Blue)

# Formula found from:
# http://www.rapidtables.com/convert/color/hsv-to-rgb.htm
def HSVtoRGB(hue, saturation, value):
    chroma = value * saturation
    temp = chroma * (1 - abs((hue / (1 / 6)) % 2 - 1))
    match = value - chroma
    if 0 <= hue < (1 / 6):
        red, green, blue = chroma, temp, 0
    elif (1 / 6) <= hue < (1 / 3):
        red, green, blue = temp, chroma, 0
    elif (1 / 3) <= hue < (1 / 2):
        red, green, blue = 0, chroma, temp
    elif (1 / 2) <= hue < (2 / 3):
        red, green, blue = 0, temp, chroma
    elif (2 / 3) <= hue < (5 / 6):
        red, green, blue = temp, 0, chroma
    else:
        red, green, blue = chroma, 0, temp
    redFinal = (red + match) * 255
    greenFinal = (green + match) * 255
    blueFinal = (blue + match) * 255
    return (int(redFinal), int(greenFinal), int(blueFinal))

# Formula found from:
# http://www.rapidtables.com/convert/color/rgb-to-hsv.htm
def RGBtoHSV(red, green, blue):
    redPercent = red / 255
    greenPercent = green / 255
    bluePercent = blue / 255
    colorLg = max(redPercent, greenPercent, bluePercent)
    colorSm = min(redPercent, greenPercent, bluePercent)
    diff = colorLg - colorSm
    if diff == 0: hue = 0
    else:
        if colorLg == redPercent:
            hue = (((greenPercent - bluePercent) / diff) % 6) * (1 / 6)
        elif colorLg == greenPercent:
            hue = (((bluePercent - redPercent) / diff) + 2) * (1 / 6)
        else:
            hue = (((redPercent - greenPercent) / diff) + 4) * (1 / 6)
    if colorLg == 0:
        saturation = 0
    else:
        saturation = diff / colorLg
    value = colorLg
    return (hue, saturation, value)

def detectionKeyPressed(event, data):
    pass

def detectionTimerFired(data):
    pass

def detectionRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill="lightBlue", width = 0)
    canvas.create_rectangle(0, 0, 300, 300, fill = "lightGray")
    drawHelp(canvas, data)
    drawBack(canvas, data)
    drawLoad(canvas, data)
    displayPics(canvas, data)

def drawLoad(canvas, data):
    height, width = 25, 100
    top, left = 75, 380
    canvas.create_rectangle(left, top, left + width, top + height,
                            fill = "lightGray", activefill = "gray")
    canvas.create_text(left + (width // 2), top + (height // 2),
                       text = "Upload Image")

def displayPics(canvas, data):
    if data.photoDetection != None:
        canvas.create_image((300 - data.photoDetectionW) // 2,
                            (300 - data.photoDetectionH) // 2,
                            anchor = NW, image = data.photoDetection)
    if data.photoEnlargeDetection != None:
        canvas.create_image(350, 150, anchor = NW,
                            image = data.photoEnlargeDetection)
        canvas.create_text(400, 150, anchor = S, text = "Enlarged view:",
                           font = "Arial 18")
        if data.curColorDetection != None:
            drawMatchingColors(canvas, data)

def drawMatchingColors(canvas, data):
    canvas.create_text(400, 300, anchor = S, text = "Current color:",
                       font = "Arial 18")
    originalColor = findColorName(data, *data.curColorDetection)
    match1Color = findColorName(data, *data.match1Detection)
    match2Color = findColorName(data, *data.match2Detection)
    match3Color = findColorName(data, *data.match3Detection)
    canvas.create_rectangle(350, 300, 450, 400,
                            fill = rgbString(*data.curColorDetection))
    canvas.create_text(400, 400, anchor = N, text = originalColor)
    canvas.create_rectangle(225, 350, 300, 425,
                            fill = rgbString(*data.match1Detection))
    canvas.create_text(162, 330, text = "Matches with:", font = "Arial 18")
    canvas.create_text(262, 425, anchor = N, text = match1Color)
    canvas.create_rectangle(125, 350, 200, 425,
                            fill = rgbString(*data.match2Detection))
    canvas.create_text(62, 425, anchor = N, text = match3Color)
    canvas.create_rectangle(25, 350, 100, 425,
                            fill = rgbString(*data.match3Detection))
    canvas.create_text(162, 425, anchor = N, text = match2Color)

def findColorName(data, red, green, blue):
    colorsDict = dict()
    for key in data.colors:
        colorName = data.colors[key]
        targetRed, targetGreen, targetBlue = key
        diffRed = (targetRed - red) ** 2
        diffGreen = (targetGreen - green) ** 2
        diffBlue = (targetBlue - blue) ** 2
        colorsDict[(diffRed + diffGreen + diffBlue)] = colorName
    minimumDiff = min(colorsDict.keys())
    return colorsDict[minimumDiff]

# rgbString function copied from:
# https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

# Run function adopted from:
# https://www.cs.cmu.edu/~112/notes/events-example0.py
####################################
# run function
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Create root before calling init (so we can create images in init)
    root = Toplevel() # Toplevel because we are BALLERS
    
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 250 # milliseconds
    init(data)
    # change tkinter defaults in top bar and disallow chaning window size
    root.wm_title("Color Vision Deficiency")
    root.iconbitmap(r'icon.ico')
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    
    root.mainloop()  # blocks until window is closed

run()

####################################
# test functions
####################################

def testAll():
    testRGBtoHSV()
    testHSVtoRGB()
    testMatching()
    testCalculateHeight()

def testRGBtoHSV():
    print("Testing RGBtoHSV() ... ", end = "")
    assert(RGBtoHSV(0, 0, 0) == (0, 0, 0))
    assert(RGBtoHSV(255, 255, 255) == (0, 0, 1))
    assert(RGBtoHSV(200, 50, 175) == ((310/360), .75, (200/255)))
    assert(RGBtoHSV(36, 208, 81) == 
           ((1/6)*(((81/255)-(36/255))/(208/255-36/255)+2),
           (208/255-36/255)/(208/255), (208/255)))
    print("Passed!")

def testHSVtoRGB():
    print("Testing HSVtoRGB() ... ", end = "")
    assert(HSVtoRGB(0, 0, 0) == (0, 0, 0))
    assert(HSVtoRGB(1, 1, 1) == (255, 0, 0))
    assert(HSVtoRGB(0, .5, .5) == (127, 63, 63))
    assert(HSVtoRGB(.5, .2, .8) == (163, 204, 204))
    print("Passed!")

def testMatching():
    print("Testing matching() ... ", end = "")
    assert(matching(255, 255, 255, 0, 0, 0) == False)
    assert(matching(128, 128, 255, 50, 0, 75) == False)
    assert(matching(74, 234, 87, 12, 96, 165) == False)
    assert(matching(9, 176, 228, 98, 32, 234) == False)
    assert(matching(100, 100, 100, 75, 175, 225))
    print("Passed!")

def testCalculateHeight():
    print("Testing calculateHeight() ... ", end = "")
    assert(calculateHeight(4, 6, 2, 7, 3, 5) == 1.3416407864998736)
    assert(calculateHeight(4, 6, 3, 30, 5, 3) == None)
    assert(calculateHeight(7, 4, 2, 8, 4, 3) == 2.6549539521063026)
    assert(calculateHeight(4567,356,346,36,23,765) == None)
    print("Passed!")

# testAll()