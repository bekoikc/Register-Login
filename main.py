import customtkinter
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTk
import tkinter as tk
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
kullanici_bilgileri = {}

root = customtkinter.CTk()
root.geometry("500x350")
root.title('BEKO')


def load_user_data():
    try:
        with open('kullanici_bilgileri.json', 'r') as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}
def save_user_data():
    with open('kullanici_bilgileri.json', 'w') as dosya:
        json.dump(kullanici_bilgileri, dosya)
def showinfos():
    CTkMessagebox(message="Kayıt Başarılı!", icon="check", option_1="Tamam")
def showinfosw():
    CTkMessagebox(title="Hata",
                  message="Bu kullanıcı adına ait zaten bir hesap var",
                  icon="cancel",
                  option_1="Tamam")
def showinfol():
    CTkMessagebox(message="Giriş Başarılı!", icon="check", option_1="Tamam")
def showinfolw():
    CTkMessagebox(title="Hata",
                  message="BU kullanıcı adına ait bir hesap bulunamadı",
                  icon="cancel",
                  option_1="Tamam")

def signin():
    username = entry1.get()
    password = entry2.get()
    if username in kullanici_bilgileri:
        showinfosw()
    else:
        kullanici_bilgileri[username] = password
        save_user_data()
        showinfos()

def login():
    user = entry1.get()
    passwd = entry2.get()
    if user in kullanici_bilgileri and kullanici_bilgileri[user] == passwd:
        showinfol()
    else:
        showinfolw()
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

kullanici_bilgileri = load_user_data()

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Sign in", command=signin)
button2.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()