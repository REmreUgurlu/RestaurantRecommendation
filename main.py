from DataCollection import DataCollector
import tkinter as tk


def set_input(url):
    clear_input()
    url_text.insert("1.0", url)


def clear_input():
    url_text.delete("1.0", tk.END)


def run(url):
    output_label.config(text="")
    DataCollector.open_webpage(url)
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

url_text = tk.Text(master=middle2, width=50, height=3)
url_text.pack(side='top')

send_button = tk.Button(master=bottom1, text="Enter", width=10, height=3, command=lambda: run(url_text.get("1.0", tk.END)))
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
