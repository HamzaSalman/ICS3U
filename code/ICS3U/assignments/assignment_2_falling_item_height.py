# Created by: Hamza Salman
# Course: ICS3U
# Created: September 2016
# This program is used to calculate the height of a falling object from 100 meters in a vacuum with a gui

import ui

GRAVITY = 9.81

seconds = 0
height = 0

def calculate_touch_up_inside(sender):
	#This function calculates the height of the object above ground when falling from 100m in a vacuum with gravity.
	
	
    seconds = int(view['seconds_textfield'].text)
    height = 100 - 0.5 *GRAVITY*seconds**2

    if height<0:
        view['height_output_label'].text = ('The object hit the ground.')

    if height>0:
        view['height_output_label'].text = str(height)

view = ui.load_view()
view.present('full_screen')
