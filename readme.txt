Preston Vander Vos
Term Project Readme

Installation:
To run the code you must import all of tkinter. Further, you must specifically import "filedialog" from tkinter.
Next, you must be able to import PIL. PIL is a module installed by doing $pip install Pillow.
Finally, you must import math and random.
You are ready when the lines below run without crashing.

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import math
import random

Overview:
The application that runs from the code is designed to help people who suffer from color vision deficiency.
The application features a color vision test in which a user can take the test and get a possibility of what type
of color vision deficiency they may suffer from. Further, a user can upload any .jpg or .png file from their computer
and determine the color at any location on the image and subsequently the matching colors to the selected color.
Next, users are able to upload two pictures and determine if colors between the two images and the same color or 
matching colors. I hope my application can help people who suffer from color vision deficiency by making daily
choices, such as outfit pairings, easier.