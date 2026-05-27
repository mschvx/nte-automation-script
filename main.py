import tkinter as tk


def activate_script() -> None:
    pass


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

    activate_button = tk.Button(
        frame,
        text="ACTIVATE NOWWW!!!",
        command=activate_script,
        font=("Arial", 14, "bold"),
        padx=18,
        pady=12,
    )
    activate_button.pack()

    root.mainloop()


if __name__ == "__main__":
    build_ui()