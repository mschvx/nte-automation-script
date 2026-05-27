import tkinter as tk

# TODO: place the mouse script here
def activate_script() -> None:
    pass
    

# simple ui that litrlly just contains the button cuz thats the only thing it needs to have :D
def build_ui() -> None:

    root = tk.Tk()
    root.title("fons farm")
    root.geometry("420x240")
    root.resizable(False, False)

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