import tkinter as tk
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))

root = tk.Tk()
root.title("SharQify - URL Shotner")
root.geometry("600x350")
root.resizable(False, False)
root.configure(bg="#f5f5f5")  # Light background for modern look

#Fonts & Colors
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
bg_color = "#f5f5f5"
entry_bg = "#ffffff"

#Title
title_label = tk.Label(root, text="SharQify", font=("Impact", 24, "bold"), bg=bg_color, fg="#FF8C00")
title_label.pack(pady=(20,5))

#   Tagline
tagline_label = tk.Label(root, text="Where Links Get Lighter.", font=("Arial", 10), bg=bg_color, fg="#555555")
tagline_label.pack(pady=(0,20))

# Long URL
longurl_label = tk.Label(root, text="Original URL:", font=label_font, bg=bg_color)
longurl_label.pack(pady=(5,2))
longurl_entry = tk.Entry(root, font=entry_font, width=50, bg=entry_bg)
longurl_entry.pack(pady=(0,10))

#    Short URL 
shorturl_label = tk.Label(root, text="Shortened URL:", font=label_font, bg=bg_color)
shorturl_label.pack(pady=(5,2))
shorturl_entry = tk.Entry(root, font=entry_font, width=50, bg=entry_bg)
shorturl_entry.pack(pady=(0,20))

#  For Button 
button = tk.Button(root, text="Shorten Now", font=button_font, bg="#FF8C00", fg="#ffffff", width=20, height=1, command=shorten)
button.pack(pady=(0,20))

root.mainloop()
