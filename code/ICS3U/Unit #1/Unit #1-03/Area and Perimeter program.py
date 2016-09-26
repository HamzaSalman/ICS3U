# Created by: Hamza Salman
# Course ICS3U
# Created: September 2016
# This program is used to calculate are and perimeter with a gui

import ui

length = 0
width = 0

def calculate_touch_up_inside(sender):
    length = int(view['length_textfield'].text)
    width = int(view['width_textfield'].text)
    area = length * width
    perimeter = (length+width)*2
    view['area_answer_label'].text = str(area)
    view['perimeter_answer_label'].text = str(perimeter)

view = ui.load_view()
view.present('full_screen')
