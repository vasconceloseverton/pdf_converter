
import tkinter as tk
from view.app_view import AppView

def main():
    root = tk.Tk()
    app = AppView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
