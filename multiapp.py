import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

# Funkcja do utworzenia tabeli użytkowników w bazie danych
def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT)''')
    conn.commit()
    conn.close()

# Funkcja do dodawania nowego użytkownika do bazy danych
def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Funkcja do sprawdzania danych logowania
def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        login_label.config(text=f"Witaj, {username}!")
    else:
        login_label.config(text="Zły login. Czy chcesz się zarejestrować?")

# Funkcja do czyszczenia pól
def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    login_label.config(text="")

# Utwórz tabelę użytkowników, jeśli nie istnieje
create_users_table()

main_window = tk.Tk()
main_window.title("Aplikacja Logowania")

# Ustaw tło
background_image = Image.open("tlo.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(main_window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Okno powitalne
welcome_label = tk.Label(main_window, text="Witaj w Aplikacji", font=("Arial", 18))
welcome_label.pack(pady=20)

# Pola do wprowadzenia danych logowania
username_label = tk.Label(main_window, text="Użytkownik:")
username_label.pack()
username_entry = tk.Entry(main_window)
username_entry.pack()

password_label = tk.Label(main_window, text="Hasło:")
password_label.pack()
password_entry = tk.Entry(main_window, show="*")  # Ukryj hasło
password_entry.pack()

login_button = tk.Button(main_window, text="Zaloguj", command=login)
login_button.pack(pady=10)

clear_button = tk.Button(main_window, text="Wyczyść", command=clear_fields)
clear_button.pack(pady=5)

login_label = tk.Label(main_window, text="")
login_label.pack(pady=10)

main_window.mainloop()
