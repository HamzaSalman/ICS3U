# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# this program calculates the circumference of the circle using the radius

import ui

def calculate_touch_up_inside(sender):
    # This function calculates the circumference using the radius
	
    PI = 3.14

    radius = int(view['radius_textfield'].text)

    circumference = 2 * PI * radius

    view['answer_label'].text = 'The circumference of the circle is:  ' + str(circumference) + 'cm'

view = ui.load_view()
view.present('full_screen')
