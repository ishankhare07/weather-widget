from gi.repository import Gtk
import requests
import datetime

class handler:
	def __init__(self,builder):
		self.builder = builder
	def on_delete(self,*args):
		Gtk.main_quit(*args)
	def on_search(self,button):
		text = self.builder.get_object('city').get_text()
		self.location = text
		response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+text)
		data = response.json()
		self.fill_data(data)
	def fill_data(self,data):
		self.builder.get_object('city_name').set_text(data['name'])
		self.builder.get_object('sunrise_lbl').set_text('Sunrise')
		self.builder.get_object('sunset_lbl').set_text('Sunset')
		self.builder.get_object('weather_des').set_text(data['weather'][0]['description'])
		self.builder.get_object('sunrise').set_text(self.return_time(data['sys']['sunrise']))
		self.builder.get_object('sunset').set_text(self.return_time(data['sys']['sunset']))
		self.builder.get_object('temp').set_text("%.2f %s" %(data['main']['temp'] - 273, '`C'))
		self.builder.get_object('wind_dir').set_text(str(data['wind']['deg']))
		self.builder.get_object('wind_speed').set_text(str(data['wind']['speed'])+'km/h')
	def return_time(self,timestamp):
		return datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

builder = Gtk.Builder()
builder.add_from_file('weather.glade')
builder.connect_signals(handler(builder))
builder.get_object('window1').show()
Gtk.main()
