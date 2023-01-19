from DataCollection import DataCollector
from DataAccess.Read import ReadData
import tkinter as tk
import threading
from pandastable.core import Table
from pandastable.core import TableModel


def set_input(url):
    clear_input()
    url_entry.insert(0, url)


def clear_input():
    url_entry.delete(0, tk.END)


def check_text_field_empty(*args):
    if len(url_entry.get()) > 0:
        send_button.config(state='normal')
    else:
        send_button.config(state='disabled')


def run():
    send_button.config(state='disabled')
    output_label.config(text="Extracting Restaurant Data...")
    DataCollector.open_webpage(url_entry.get())
    send_button.config(state='normal')
    new_window = tk.Toplevel(master=root)
    new_window.title("Restaurant Menu")
    new_window.geometry("1000x700")
    frame = tk.Frame(new_window)
    frame.pack()
    df = ReadData.read_from_restaurant_menus()
    table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True, width=800, height=400)
    table.show()
    output_label.config(text="Restaurant Data is Extracted. You can close the app now.")


maydonoz_url = "https://www.yemeksepeti.com/restaurant/sopa/maydonoz-doner-sopa"
popeyes_url = "https://www.yemeksepeti.com/restaurant/lm6l/popeyes-lm6l"
dominos_url = "https://www.yemeksepeti.com/restaurant/qfq9/dominos-pizza-qfq9"
morgis_url = "https://www.yemeksepeti.com/restaurant/defq/morgis-odun-atesinde-doner"
yemeksepeti_urls = [maydonoz_url, popeyes_url, dominos_url, morgis_url]

root = tk.Tk()
root.geometry("800x500")
root.resizable(False, False)
root.title('Restaurant Data Extractor')

top1 = tk.Frame(root)
top2 = tk.Frame(root)
middle1 = tk.Frame(root, pady=10)
middle2 = tk.Frame(root, pady=10)
bottom1 = tk.Frame(root, pady=10)
bottom2 = tk.Frame(root, pady=20)

warning_label = tk.Label(master=top1, text="You need to have Firefox installed in order to run the app!", font=("Arial", 20))
warning_label.pack(side='left')

greeting_label = tk.Label(master=top2, text="Enter the url or choose from below", font=("Arial", 15))
greeting_label.pack(side='left')

restaurant_button_1 = tk.Button(master=middle1, text="Maydonoz", width=10, height=3, command=lambda: set_input(yemeksepeti_urls[0]))
restaurant_button_1.pack(side='left')
restaurant_button_2 = tk.Button(master=middle1, text="Popeyes", width=10, height=3, command=lambda: set_input(yemeksepeti_urls[1]))
restaurant_button_2.pack(side='left')
restaurant_button_3 = tk.Button(master=middle1, text="Dominos", width=10, height=3, command=lambda: set_input(yemeksepeti_urls[2]))
restaurant_button_3.pack(side='left')
restaurant_button_4 = tk.Button(master=middle1, text="Morgis", width=10, height=3, command=lambda: set_input(yemeksepeti_urls[3]) )
restaurant_button_4.pack(side='left')

url_text_variable = tk.StringVar(middle2)
url_entry = tk.Entry(master=middle2, textvariable=url_text_variable, width=80)
url_entry.pack(side='top')
url_text_variable.trace('w', check_text_field_empty)

send_button = tk.Button(master=bottom1, text="Enter", width=10, height=3,state='disabled', command=lambda: threading.Thread(target=run).start())
send_button.pack(side='left')

clear_button = tk.Button(master=bottom1, text="Clear", width=10, height=3, command=clear_input)
clear_button.pack(side='left')

output_label = tk.Label(master=bottom2, text="", font=("Arial", 20))
output_label.pack(side='left')

top1.pack()
top2.pack()
middle1.pack()
middle2.pack()
bottom1.pack()
bottom2.pack()

root.mainloop()
