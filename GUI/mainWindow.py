# Import(s)
import tkinter as tk
from GUI import buttonPress

# Declare the Window
window = tk.Tk()
window.title("Simple URL Shortener")
window.geometry("1750x1800")
window.columnconfigure([0, 1], minsize=250)
window.rowconfigure([0, 4], minsize=100)
window.resizable(width=False, height=False)

# Add Properties to the Layout
lURLLabel = tk.Label(text="Enter the URL you wish to shorten:")
lURLLabel.grid(row=0, column=1)
lText = tk.Text(window)
lText.insert("end-1c", "https://")
lText.grid(row=1, column=1)
btn_Convert = tk.Button(master=window, text="Convert", command=lambda: buttonPress.convert_button_press())
btn_Convert.grid(row=2, column=1)
btn_Clear = tk.Button(master=window, text="Clear", command=lambda: buttonPress.clear_button_press())
btn_Clear.grid(row=2, column=2)
btn_Exit = tk.Button(master=window, text="Exit Program", command=lambda: buttonPress.exit_button_press())
btn_Exit.grid(row=2, column=0)
sURLLabel = tk.Label(text="Shortened URL:")
sURLLabel.grid(row=3, column=1)
sText = tk.Text(window)
sText.grid(row=4, column=1)

# Execute Window
window.mainloop()
