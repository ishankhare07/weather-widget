from gi.repository import Gtk
import requests

class handler:
	def __init__(self,builder):
		self.builder = builder
	def on_delete(self,*args):
		Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file('weather.glade')
builder.connect_signals(handler(builder))
builder.get_object('window1').show()
Gtk.main()