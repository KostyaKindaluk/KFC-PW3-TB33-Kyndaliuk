import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from logic.weather import create_forecasts_for_year, get_forecasts, clear_all_forecasts


class WeatherApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Прогноз погоди")
		self.root.geometry("600x500")

		self.style = ttk.Style("litera")

		self.btn_frame = ttk.Frame(self.root, padding=10)
		self.btn_frame.pack(fill=X)

		self.generate_btn = ttk.Button(
			self.btn_frame, text="Згенерувати прогноз",
			command=self.generate_forecast, bootstyle=PRIMARY
		)
		self.generate_btn.pack(side=LEFT, padx=5)

		self.clear_btn = ttk.Button(
			self.btn_frame, text="Очистити прогнози",
			command=self.clear_forecast, bootstyle=DANGER
		)
		self.clear_btn.pack(side=LEFT, padx=5)

		self.text_frame = ttk.Frame(self.root, padding=10)
		self.text_frame.pack(fill=BOTH, expand=YES)

		self.text = ttk.ScrolledText(self.text_frame, height=25)
		self.text.pack(fill=BOTH, expand=YES)

		self.load_forecasts()

	def load_forecasts(self):
		try:
			forecasts = get_forecasts()
			self.text.delete("1.0", "end")
			if forecasts:
				for f in forecasts:
					self.text.insert("end", f"{f.date.strftime('%Y-%m-%d')} — {f.temp:.2f}°C\n")
				self.generate_btn.config(state=DISABLED)
				self.clear_btn.config(state=NORMAL)
			else:
				self.text.insert("end", "Немає збережених прогнозів.\n")
				self.generate_btn.config(state=NORMAL)
				self.clear_btn.config(state=DISABLED)
		except Exception as e:
			messagebox.showerror("Помилка", str(e))

	def generate_forecast(self):
		try:
			predictions = create_forecasts_for_year()
			messagebox.showinfo("Успіх", f"Збережено {len(predictions)} прогнозів.")
			self.load_forecasts()
		except Exception as e:
			messagebox.showerror("Помилка", str(e))

	def clear_forecast(self):
		try:
			if messagebox.askyesno("Підтвердження", "Очистити всі прогнози?"):
				clear_all_forecasts()
				messagebox.showinfo("Готово", "Прогнози очищено.")
				self.load_forecasts()
		except Exception as e:
			messagebox.showerror("Помилка", str(e))