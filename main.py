# NOTE: NTE HAS SOME SORT OF FILTERING FOR THE INPUT IF THE INPUT DOES NOT COME FROM HARDWARE
# SO THE SOLUTION FOR THIS IS TO RUN THE SCRIPT AS ADMINISTRATOR
# EX. CMD > RUN AS ADMIN > cd %USERPROFILE%\Desktop tas whatever hanapin mo nalang depende sa OS
# 
# ANOTHER NOTE: LEVEL 1-9, USE AURELIA, MINT, AND SAKIRI 
# note requires more testing will come back next monday
import ctypes
import time
import tkinter as tk
import pydirectinput 


# UI globals updated from the automation loop
root = None
loop_label = None

# mouse script 
def activate_script() -> None:
    global loop_label, root
    user32 = ctypes.windll.user32

    for run in range(117):
        # update loop counter in the UI
        loop_label.config(text=f"Run: {run+1}/117")
        root.update()
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
        time.sleep(0.05)

        # move to the target point and click it
        pydirectinput.moveTo(1390, 798)
        time.sleep(0.05)
        pydirectinput.click()

        # NOW AT THIS POINT THE GAME IS RUNNING SO ALL WE HAVE TO DO IS WAIT FOR 50SECONDS TO GET THREE STARS
        time.sleep(50)  # buffer to get three stars

        # press the exit button 
        pydirectinput.moveTo(33, 33)
        time.sleep(0.05)
        pydirectinput.click()

        # press the claim button 
        pydirectinput.moveTo(955, 674)
        time.sleep(0.05)
        pydirectinput.click()

        # click twice
        for _ in range(2):
            pydirectinput.click()
            time.sleep(0.05)

# simple ui that litrlly just contains the button cuz thats the only thing it needs to have :D
def build_ui() -> None:

    global root, loop_label

    root = tk.Tk()
    root.title("fons farm")
    root.geometry("250x220")
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
        command=activate_script,
        font=("Arial", 14, "bold"),
        padx=18,
        pady=12,
    )
    activate_button.pack()

    loop_label = tk.Label(
        frame,
        text="Run: 0/117",
        font=("Arial", 11),
    )
    loop_label.pack(pady=(16, 0))

    root.mainloop()


if __name__ == "__main__":
    build_ui()