from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

color_light = "#FBF7F0"
color_mid = "#CDC9C3"
color_dark = "#555555"
border = 0

root = Tk()
root.title("Image Watermark")
cv = Canvas(width=400, height=250, highlightthickness=0)
cv.grid(row=0, column=0, columnspan=3)

def load_img():
    img = ImageTk.PhotoImage(img_open)
    label = Label(root, image=img)
    label.place(x=0, y=0)
    label.image = img
    
def root_button(text, func, position):
    btn = Button(root, text=text, width=15, height=2, bg=color_dark, fg=color_light, bd=border, command=func)
    btn.grid(row=1, column=position, sticky=E + W, padx=3, pady=5)

def upload():
    global img_open
    filetypes = [('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')]
    img_upload = fd.askopenfilename(title='Upload the Image', filetypes=filetypes)
    img_open = Image.open(img_upload)
    width, height = img_open.size
    if width > 1920:
        img_open.thumbnail((width / 2, height / 2))
        cv.configure(width=width / 2, height=height / 2)
    else:
        img_open.thumbnail((width, height))
        cv.configure(width=width, height=height)
    load_img()

def watermark():
    window = Toplevel()
    window.title("Name")
    window.geometry("330x70")
    def submit():
        fin_name = input_name.get()
        font = ImageFont.truetype('arial.ttf', 25)
        draw = ImageDraw.Draw(img_open)
        # get photo size
        img_size = ImageTk.PhotoImage(img_open)
        size_x, size_y = img_size.width(), img_size.height()
        # Draw in watermark
        draw.text((size_x - 10, size_y - 10), fin_name, font=font, fill="#FFF", anchor="rb")
        load_img()
        window.destroy()
    def enter(event):
        # Hit Enter
        submit()
    def onclick(event=None):
        # Mouse onclick
        submit()
    
    input_name = StringVar()
    window_label = Label(window, text="Name", bg=color_light, font=('calibri', 12, "italic"))
    window_label.grid(row=0, column=0, padx=5, pady=20)
    window_entry = Entry(window, textvariable=input_name, font=('calibri', 10))
    window_entry.grid(row=0, column=1, padx=5, pady=20)
    window_button = Button(window, text="Submit", width=15, bg=color_dark, fg=color_light, bd=border,  command=onclick)
    window_button.grid(row=0, column=2, padx=5, pady=20)
    window.bind('<Return>', enter)
    
def output():
    filetypes = [('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')]
    img_save = fd.asksaveasfilename(title='Save Image', filetypes=filetypes, defaultextension=".png")
    img_open.save(img_save)
    
root_button("Upload", upload, 0)
root_button("Water Mark", watermark, 1)
root_button("Ouput", output, 2)

root.mainloop()
