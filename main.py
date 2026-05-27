# NOTE: NTE HAS SOME SORT OF FILTERING FOR THE INPUT IF THE INPUT DOES NOT COME FROM HARDWARE
# SO THE SOLUTION FOR THIS IS TO RUN THE SCRIPT AS ADMINISTRATOR
# EX. CMD > RUN AS ADMIN > cd %USERPROFILE%\Desktop tas whatever hanapin mo nalang depende sa OS 

import ctypes
import time
import tkinter as tk
import pydirectinput 


# mouse script 
def activate_script() -> None:
    user32 = ctypes.windll.user32

    # get the current screen size
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # calculate the center of the screen
    center_x = screen_width // 2
    center_y = screen_height // 2

    # move the mouse to the center of the screen
    pydirectinput.moveTo(center_x, center_y)
    time.sleep(0.05)

    # click twice
    for _ in range(2):
        pydirectinput.click()
        time.sleep(0.05)

    # press F
    pydirectinput.press("f")


# simple ui that litrlly just contains the button cuz thats the only thing it needs to have :D
def build_ui() -> None:

    root = tk.Tk()
    root.title("fons farm")
    root.geometry("250x200")
    root.resizable(False, False)
    root.attributes("-topmost", True)  # always on top

    frame = tk.Frame(root, padx=24, pady=24)
    frame.pack(expand=True, fill="both")

    title = tk.Label(
        frame,
        text="fons farm",
        font=("Arial", 22, "bold"),
    )
    title.pack(pady=(0, 24))

    # the only part here that matters wc is the button
    activate_button = tk.Button(
        frame,
        text="ACTIVATE NOWWW!!!",
        command=activate_script,  # call the script pag cinlick
        font=("Arial", 14, "bold"),
        padx=18,
        pady=12,
    )
    activate_button.pack()

    root.mainloop()


if __name__ == "__main__":
    build_ui()