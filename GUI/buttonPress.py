# Import(s)
from GUI import mainWindow
import pyshorteners as pysh


# Declare Handling of Convert Button Key Press
def convert_button_press():
    """
    Convert the value of lText to a shortened URL and assign the value
    to sText. NOTE: Must delete existing text in sText.
    """
    # Assign the Values to the Variables
    conversionOne = mainWindow.lText.get("1.0", "end-1c")
    conv = pysh.Shortener()
    conversionTwo = conv.tinyurl.short(conversionOne)
    mainWindow.sText.delete(1.0, "end-1c")
    mainWindow.sText.insert("end-1c", conversionTwo)


def clear_button_press():
    """
    On button press, clear the value of both the non-converted URL and converted URL
    textboxes.
    """
    mainWindow.sText.delete(1.0, "end-1c")
    mainWindow.lText.delete(1.0, "end-1c")
    mainWindow.lText.insert("end-1c", "https://")


def exit_button_press():
    """
    Exits the program when Exit button is pressed.
    """
    quit()

