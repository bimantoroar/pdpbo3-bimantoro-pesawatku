
from tkinter import Label
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title("TP3")
root.configure(bg="snow")
# Label
myLabel = Label(root, text="Nama : ", bg="snow").grid(column=0, row=0)
nama = Entry(root, width=20, borderwidth=5)
nama.insert(0, "")
nama.grid(column=1, row=0)

myLabel = Label(root, text="Seri : ", bg="snow").grid(column=0, row=1)
seri = Entry(root, width=20, borderwidth=5)
seri.insert(0, "")
seri.grid(column=1, row=1)

myLabel = Label(root, text="Harga : ", bg="snow").grid(column=0, row=2)
harga = Entry(root, width=20, borderwidth=5)
harga.insert(0, "")
harga.grid(column=1, row=2)
# Combobox
myLabel = Label(root, text="Tipe :", bg="snow").grid(column=0, row=3)
options = [
    "Jet Private",
    "Cargo",
    "Komersil",
    "Tempur"
]


tipe = StringVar()
tipe.set(options[0])

drop = OptionMenu(root, tipe, *options)
drop.configure(bg="white")
drop.grid(column=1, row=3)
# Checkbutton
var = StringVar()
myLabel = Label(root, text="Tiket :", bg="snow").grid(column=0, row=4)
c = Checkbutton(root, text="Firstclass", bg="snow",
                variable=var, onvalue="Firstclass", offvalue=" ")
c.deselect()
c.grid(column=1, row=4)

var2 = StringVar()
c = Checkbutton(root, text="Bussiness", bg="snow",
                variable=var2, onvalue="Business", offvalue=" ")
c.deselect()
c.grid(column=1, row=5)
var3 = StringVar()
c = Checkbutton(root, text="Economies", bg="snow",
                variable=var3, onvalue="Economies", offvalue=" ", width=15)
c.deselect()
c.grid(column=1, row=6)


# Radiobutton
myLabel = Label(root, text="Bagasi : ", bg="snow").grid(column=0, row=7)
Bagasi = [
    ("15kg", "15kg"),
    ("25kg", "25kg"),
    ("35kg", "35kg")
]

bagasi = StringVar()
bagasi.set("15kg")

i = 7
for text, bagasis, in Bagasi:
    Radiobutton(root, text=text, bg="snow", variable=bagasi,
                value=bagasis).grid(column=1, row=i)
    i = i+1

# openfile


def open():
    global my_image
    global filename
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    filename = root.filename
    messagebox.showinfo('Response', 'Alamat file berhasil Tersimpan!!')


my_btn = Button(root, text="Open Photo File", bg="white",
                command=open).grid(column=1, row=11)

# Submit button
my_btn = Button(root, text="Submit", bg="white",
                command=lambda: popup(nama.get(), seri.get(), harga.get(), tipe.get(), var.get(), var2.get(), var3.get(), bagasi.get())).grid(column=1, row=12)


def popup(Data, Data2, Data3, Data4, Data5, Data6, Data7, Data8):
    response = messagebox.showinfo(
        'This is my Popup', Data + Data2 + Data3 + Data4 + Data5 + Data6 + Data7 + Data8)
    Label(root, text=response).pack()


# see all button
my_btn = Button(root, text="See All", bg="white",
                command="").grid(column=1, row=13)
# clear button
my_btn = Button(root, text="Clear",  bg="white",
                command=lambda: delete).grid(column=1, row=14)


# def delete():

#     messagebox.showinfo('Response', 'Data Berhasil Dihapus!!')


# about button
my_btn = Button(root, text="About", bg="white",
                command=lambda: about()).grid(column=1, row=15)


def about():
    top = Toplevel()
    top.title("Detail")
    top.configure(bg='snow')
    d_frame = LabelFrame(top, text="Data", bg="snow", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    d_namaapl = Label(d_frame, text="Nama Aplikasi : PesawatKu ", anchor="w", bg="snow").grid(
        row=0, column=0, sticky="w")
    d_desk = Label(d_frame, text="Deskripsi Aplikasi : Aplikasi pemesanan pesawat ", anchor="w", bg="snow").grid(
        row=1, column=0, sticky="w")
    d_nim = Label(d_frame, text="NIM: 1900303 ", anchor="w", bg="snow").grid(
        row=2, column=0, sticky="w")
    d_nama = Label(d_frame, text="Nama : Bimantoro Aulia Rizky ",
                   anchor="w", bg="snow").grid(row=3, column=0, sticky="w")

    d_exit = Button(d_frame, text="Exit", bg="white", command=lambda: exit())
    d_exit.grid(row=6, column=1, sticky="w")


# exit button
my_btn = Button(root, text="Exit", bg="white",
                command=lambda: exit()).grid(column=1, row=16)


def exit():
    res = messagebox.askquestion('Konfirmasi', 'Tutup Aplikasi?')
    if res == 'yes':
        root.quit()
    elif res == 'no':
        messagebox.showinfo('Response', 'Okay')


root.mainloop()
