import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def fetch_fox_image():
    try:
        response = requests.get('https://randomfox.ca/floof/')
        if response.status_code == 200:
            image_url = response.json()['image']

            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_data = Image.open(BytesIO(image_response.content))
                photo_image = ImageTk.PhotoImage(image_data)

                image_label.config(image=photo_image)
                image_label.image = photo_image
            else:
                print("Failed to retrieve the fox image.")
        else:
            print("Failed to retrieve the image")
    except Exception as e:
        print(f"An error occurred: {e}")


root = tk.Tk()
root.title("Random Fox Image Generator")
image_label = tk.Label(root)
image_label.pack()
fetch_image_button = tk.Button(root, text="Fetch a new fox image", command=fetch_fox_image)
fetch_image_button.pack()
fetch_fox_image()

root.mainloop()
