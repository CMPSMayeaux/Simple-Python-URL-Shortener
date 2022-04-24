# Import(s)
import tkinter as tk
import pyshorteners as pysh

# Declare the Window
window = tk.Tk()
window.title("Simple URL Shortener")
window.geometry("1750x1800")
window.columnconfigure([0, 1], minsize=250)
window.rowconfigure([0, 4], minsize=100)
window.resizable(width=False, height=False)


# Declare Handling of Convert Button Key Press
def retrieve_input():
    """Convert the value of lURLLabel to a shortened URL and assign the value
    to sURLLabel.
    """
    # Assign the Values to the Variables
    conversionOne = lText.get("1.0", "end-1c")
    conv = pysh.Shortener()
    conversionTwo = conv.tinyurl.short(conversionOne)
    sText.delete(1.0, "end-1c")
    sText.insert("end-1c", conversionTwo)


# Add Properties to the Layout
lURLLabel = tk.Label(text="Enter the URL you wish to shorten:")
lURLLabel.grid(row=0, column=1)
lText = tk.Text(window)
lText.grid(row=1, column=1)
btn_Convert = tk.Button(master=window, text="Convert", command=lambda: retrieve_input())
btn_Convert.grid(row=2, column=1)
sURLLabel = tk.Label(text="Shortened URL:")
sURLLabel.grid(row=3, column=1)
sText = tk.Text(window)
sText.grid(row=4, column=1)

# Execute Window
window.mainloop()
