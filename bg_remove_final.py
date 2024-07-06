# Import libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove

# Create the main window
root = tk.Tk()
root.title("Background Remover")
root.geometry("500x500")

# Define the image variable as global

#This variable will later hold the image object that is opened by the user.
image = None
# This variable will later hold the ImageTk.PhotoImage object, which is a format suitable for displaying in a tkinter widget.
photo = None

# Function to open an image
def open_image():
    global image, photo
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo # creates a refrence
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open the image. Please select a valid image file.\n{e}")


# Function to remove image background
def remove_background():
    global image, photo
    if image:
        try:
            # Remove background and update the image
            image_no_bg = remove(image.convert('RGB'))
            image_no_bg.thumbnail((300, 300))  # Resize for display if needed
            photo = ImageTk.PhotoImage(image_no_bg)
            label.config(image=photo)
            label.image = photo
            image = image_no_bg  # Update the global image variable with the processed image
        except Exception as e:
                messagebox.showerror("Error", f"An error occurred while removing the background: {e}")
    else:
        result_label.config(text="No image selected.")

# Function to save the image
def save_image():
    global image
    if image:
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                image.save(file_path)
                result_label.config(text=f"Image saved as '{file_path}'.")
            else:
                result_label.config(text="Save operation cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while removing the background: {e}")
    else:
        result_label.config(text="No image to save.")

# Create 'Open Image' button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Create 'Remove Background' button
remove_button = tk.Button(root, text="Remove Background", command=remove_background)
remove_button.pack(pady=10)

# Create 'Save Image' button
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)

# Create an image label
label = tk.Label(root)
label.pack()

# Create a label to display the result 
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
