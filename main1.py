import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_rezultat.delete("1.0", "end")
    text_rezultat.insert("end", calculation)


def clear_filed():
    global calculation
    calculation = ""
    text_rezultat.delete("1.0", "end")
    text_rezultat.insert(1.0, calculation)


def evaluare():
    global calculation
    try:
        text_rezultat.delete(1.0, "end")
        text_rezultat.insert(1.0, str(eval(calculation)))
        calculation = str(eval(calculation))
    except:
        clear_filed()
        text_rezultat.insert(1.0, "error")


def curata():
    global calculation
    calculation = ""
    text_rezultat.insert(1.0, "end")


root = tk.Tk()
root.geometry("400x600")

text_rezultat = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_rezultat.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 24))
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 24))
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 24))
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 24))
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 24))
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 24))
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 24))
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 24))
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 24))
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 24))
btn0.grid(row=5, column=2)

btnplus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 24))
btnplus.grid(row=5, column=1)

btnminus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 24))
btnminus.grid(row=5, column=3)

btnegal = tk.Button(root, text="=", command=lambda: evaluare(), width=5, font=("Arial", 24))
btnegal.grid(row=6, column=1)

btncls = tk.Button(root, text="C", command=clear_filed, width=5, font=("Arial", 24))
btncls.grid(row=7, column=1)

root.mainloop()
