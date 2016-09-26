# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# This program shows the school name and their mascot

import ui

def mother_teresa_button_touch_up_inside(sender):
    view['school_name_label'].text = 'Mother Teresa HS'
    view['mascot_label'].text = 'Titans'
    
def st_joes_button_touch_up_inside(sender):
    view['school_name_label'].text = 'St. Joe HS'
    view['mascot_label'].text = 'Jaguars'
    
def st_marks_button_touch_up_inside(sender):
    view['school_name_label'].text = 'St. Mark HS'
    view['mascot_label'].text = 'Lions'

view = ui.load_view()
view.present('full_screen')
