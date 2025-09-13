import tkinter as tk
import pyshorteners

def shorten():
    shorturl_entry.delete(0, tk.END)  
    long_url = longurl_entry.get().strip()

    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        shorturl_entry.insert(0, "⚠ Please enter a valid URL (http:// or https://)")
        return

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        shorturl_entry.insert(0, short_url)
    except Exception as e:
        shorturl_entry.insert(0, f"Error: {e}")

def copy_to_clipboard():
    short_url = shorturl_entry.get()
    if short_url and not short_url.startswith(("⚠", "Error")):
        root.clipboard_clear()
        root.clipboard_append(short_url)
        root.update()

root = tk.Tk()
root.title("SharQify - URL Shortener")
root.geometry("600x350")
root.resizable(False, False)
root.configure(bg="#f5f5f5")  

# Fonts & Colors
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
bg_color = "#f5f5f5"
entry_bg = "#ffffff"

# Title
title_label = tk.Label(root, text="SharQify", font=("Impact", 24, "bold"), bg=bg_color, fg="#FF8C00")
title_label.pack(pady=(20, 5))

# Tagline
tagline_label = tk.Label(root, text="Where Links Get Lighter.", font=("Arial", 10), bg=bg_color, fg="#555555")
tagline_label.pack(pady=(0, 20))

# Long URL
longurl_label = tk.Label(root, text="Original URL:", font=label_font, bg=bg_color)
longurl_label.pack(pady=(5, 2))
longurl_entry = tk.Entry(root, font=entry_font, width=50, bg=entry_bg)
longurl_entry.pack(pady=(0, 10))

# Short URL + Copy button
shorturl_label = tk.Label(root, text="Shortened URL:", font=label_font, bg=bg_color)
shorturl_label.pack(pady=(5, 2))

short_frame = tk.Frame(root, bg=bg_color)
short_frame.pack(pady=(0, 20))

shorturl_entry = tk.Entry(short_frame, font=entry_font, width=45, bg=entry_bg)
shorturl_entry.grid(row=0, column=0, padx=(0, 5))

copy_button = tk.Button(short_frame, text="📋", font=("Arial", 12), bg="#4CAF50", fg="white",
                        command=copy_to_clipboard, width=3)
copy_button.grid(row=0, column=1)

# Shorten Button
button = tk.Button(root, text="Shorten Now", font=button_font, bg="#FF8C00", fg="#ffffff",
                   width=20, height=1, command=shorten)
button.pack(pady=(0, 20))

root.mainloop()
