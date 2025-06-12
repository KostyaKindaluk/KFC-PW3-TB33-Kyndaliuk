from tkinter import Tk
from gui.main_window import WeatherApp


if __name__ == "__main__":
	root = Tk()
	app = WeatherApp(root)
	root.mainloop()