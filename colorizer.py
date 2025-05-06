import tkinter as tk
from tkinter import filedialog, messagebox
from main import Colorizer
import os

colorizer = Colorizer(height=480, width=640)

def process_image():
    file_path = filedialog.askopenfilename(title="Select a grayscale image", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        try:
            colorizer.processImage(file_path)
            messagebox.showinfo("Success", f"Image colorized and saved to 'output/' folder.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image.\n{e}")


# --- GUI Setup ---
root = tk.Tk()
root.title("CrossDomain - Image Colorizer")
root.state('zoomed')
root.resizable(False, False)

title_label = tk.Label(root, text="Image Colorizer", font=("Helvetica", 14, "bold"))
title_label.pack(pady=20)

btn_image = tk.Button(root, text="Colorize Image", width=25, height=2, command=process_image)
btn_image.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()


