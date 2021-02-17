# image_folder = sys.argv[1]
# output_folder = sys.argv[2]
from PIL import Image, ImageFilter
import sys
import os
# def JPGtoPNG():
# def PNGtoJPG():

Transfunction = (input('choice function, A: to Jpeg B:  to PNG : '))
if Transfunction is 'A':
    print('1:PNG to Jpeg')
    input_folder = input('please enter import folder :')
    output_folder = input('please enter outport folder :')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        print(f'{input_folder}\{filename}')
        img = Image.open(f'{input_folder}\B{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}\{filename}', 'jpeg')
    print('it work now')

elif Transfunction is 'B':
    print('Jpeg to PNG')
    input_folder = input('please enter import folder :')
    output_folder = input('please enter outport folder :')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        print(f'{input_folder}\{filename}')
        img = Image.open(f'{input_folder}\{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}\{filename}', 'png')
    print('it work now')

else:
    print('plz enter A or B')
