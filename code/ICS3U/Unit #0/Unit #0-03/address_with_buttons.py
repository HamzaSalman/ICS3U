# Created by: Hamza Salman
# Created on: September 2016
#Created for: ICS3U
# This is the address program with a button

import ui 

def address_touch_up_inside(sender):
	view['hamza_salman_label'].text = ('Hamza Salman')
	view['ottawa_label'].text = ('Ottawa')
	view['ontario_label'].text = ('Ontario')
	
view = ui.load_view()
view.present('full_screen')
