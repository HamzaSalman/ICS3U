# Created by: Hamza Salman
# Created on: September 2016
#Created for: ICS3U
# This is the hello world program with a button

import ui 

def hello_world_touch_up_inside(sender):
	#print ('Hello, World!')
	view['hello_world_label'].text = ('Hello, World!')

view = ui.load_view()
view.present('full_screen')

