import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = tk.Tk()
root.title("Currency Exchange Converter V1.0 | Created By ChipHayIT")

#icon
i1 = PhotoImage(file = "C:\\Users\ROG\Desktop\ICT\Project LAB\BG3.png")
root.iconphoto(False,i1)

Tops = Frame(root, bg = '#C18C8C', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency Exchange Converter V1.0',bg='#C18C8C', fg='black')
headlabel.pack(fill="both",expand=True)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("เลือกสกุลเงิน")
variable2.set("เลือกสกุลเงิน")

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showerror("Error #01","กรุณากรอกตัวเลขใหม่")

	elif (from_currency == "เลือกสกุลเงิน" or to_currency == "เลือกสกุลเงิน"):
		tkinter.messagebox.showerror("Error #02","กรุณาเลือกสกุลเงินเพื่อทำรายการ")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

#Clear
def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["BND", "KHR", "IDR", "LAK", "MYR", "MMK","PHP","SGD","VND","THB"]

root.configure(background='#C18C8C')
root.geometry("600x500")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#C18C8C", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="                    กรอกจำนวนเงิน : ", bg="#C18C8C", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t                    From : ", bg="#C18C8C", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t                        To : ", bg="#C18C8C", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t         จำนวนเงินที่ได้ : ", bg="#C18C8C", fg="black")
label1.grid(row=8, column=0, sticky=W)
label1.place(x=-2,y=275)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#C18C8C", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#C18C8C", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = ttk.Combobox(root,textvariable=variable1,values=CurrenyCode_list)
FromCurrency_option.place(x = 10,y=10)

ToCurrency_option = ttk.Combobox(root,textvariable=variable2,values=CurrenyCode_list)
ToCurrency_option.place(x = 5,y=5)

FromCurrency_option.grid(row=3, column=0, sticky=E)
ToCurrency_option.grid(row=4, column=0, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=9.5, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx = 12,ipady= 12, sticky=E)
Amount2_field.place(x=290,y=280)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="#BEADC9", fg="black",command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)
Label_9.place(x=300,y=200)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#C18C8C", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="#BEADC9", fg="black",command=clear_all)
Label_9.grid(row=10, column=0)
Label_9.place(x=250,y=400)

root.mainloop()
