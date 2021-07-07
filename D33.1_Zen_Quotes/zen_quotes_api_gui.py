from tkinter import *
import requests

# ---------- API Call -------------- #
def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random") 
    response.raise_for_status()
    data = response.json()
    print(data)
    for i in data:
        canvas.itemconfig(quote_text, text=i["q"])
        canvas.itemconfig(author_text, text=i["a"])
# -------------------------------------- #


# ---------- GUI Creation -------------- #
window = Tk()

window.title("Daily Inspiration")
window.config(padx=80, pady=80, background="bisque4")

canvas = Canvas(width=500, height=500, background="bisque3")
quote_text = canvas.create_text(250, 207, text="CLICK BUTTON", width=250, font=("Arial", 20, ), fill="black")
author_text = canvas.create_text(250, 400, text="", width=250, font=("Arial", 20,), fill="black")
canvas.grid(row=0, column=0)

click_button = Button(width=20,height=1, text="GET A QUOTE", background="MistyRose3", highlightthickness=0, command=get_quote)
click_button.grid(pady=10, row=1, column=0)

window.mainloop()
# -------------------------------------- #
