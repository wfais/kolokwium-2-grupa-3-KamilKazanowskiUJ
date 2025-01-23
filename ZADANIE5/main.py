import tkinter as tk
from tkinter import Label, StringVar, Entry, Button

# Napisz funkcję create_app(), która:
# Tworzy główne okno Tkinter,
# Dodaje etykietę (label) z jakimś wstępnym tekstem (np. "Wpisz coś:"),
# Dodaje pole tekstowe (Entry), w którym użytkownik może coś wpisać,
# Dodaje przycisk (Button), po którego kliknięciu tekst z pola Entry zostanie wyświetlony w drugiej etykiecie (np. "Wpisałeś: <tekst>").


def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """
    okno = tk.Tk()
    okno.resizable(False, False)
    okno.title("Prosta aplikacja tkinter")

    # label_instruct = umocuj przez pack
    label = Label(okno, text="Wpisz coś:", padx=200, pady=20, font=('Arial', 16))
    label.pack()

    # entry_text = 
    entry = Entry(okno, bd=5, width=20, font=('Arial', 16), bg="gray", fg="white", justify='right')
    entry.pack()

    # label_result = tk.Label(...
    label_result = Label(okno, text="---", padx=200, pady=20, font=('Arial', 16))
    label_result.pack()

    # zdefiniuj funkcję show_text() pobierającą wpisany tekst i wyświetlającą w label_result
    def show_text():
        ans = StringVar()
        ans = entry.get()
        label_result.config(text="Wpisałeś: " + ans)

    button_show = Button(okno, text="przycisk", padx=20, pady=10, font=('Arial', 16), command=show_text)
    button_show.pack()

    return okno

if __name__ == '__main__':
    app = create_app()
    app.mainloop()
