import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk  # Importieren von Pillow für die Bildverarbeitung
import os
import time
from datetime import datetime
from tkinter import Tk, Button, LEFT, TOP
from PIL import Image, ImageTk
import pandas as pd
from plyer import notification


print ("Hallo! Herzlich Willkommen zurück zu deinem WellBee Tracker. Schön, dich wiederzusehen!")
print("Hier ist eine Übersicht deiner Tracking-Daten von dieser Woche, lass uns gemeinsam deine Fortschritte anschauen und neue Ziele setzen.")

#Tabelle für die getrackten Infos der Woche
data = [
    ["Mo", "Chaos", 50, 9, 1804],
    ["Di", "Super-duper!", 30, 8, 2399],
    ["Mi", "Geht so", 30, 10, 2131],
    ["Do", "Super-duper!", 60, 9, 2114],
    ["Fr", "Ganz okay", 65, 11, 2043],
    ["Sa", "Meh", 0, 7, 1999]
]
columns = ["Tag", "Stimmung", "Dauer Sporteinheit (min)", "Wasserzufuhr (Gläser)", "Kalorienaufnahme (kcal)"]
 
# DataFrame erstellen
df = pd.DataFrame(data, columns=columns)
 
# Als Tabelle anzeigen
print(df.to_string(index=False))

print("Heute ist Sonntag, der letzte Tag der Woche. Was möchtest du jetzt tracken?")

#Variablen zur Verwendung der Definitionen
training_duration = 0
total_calories = 0
total_water = 0

# Funktion zum Abfragen der Kalorien
def ask_calories(meal, button):
    # Öffnet ein Eingabefenster für die Kalorien der jeweiligen Mahlzeit
    calories = simpledialog.askinteger("Kalorien eingeben", f"Wie viele Kalorien hast du zum {meal} zu dir genommen?")
    if calories is not None:
        # Kalorien zum Gesamtwert hinzufügen
        global total_calories
        total_calories += calories
        # Zeigt die Gesamtzahl der Kalorien an
        total_label.config(text=f"Gesamtzahl der Kalorien heute: {total_calories} kcal")
        # Button wird grün, nachdem ein Eintrag erfolgt ist
        button.config(bg="green", state="disabled")  # Button wird grün und deaktiviert
        

# Funktion zum Abfragen der Wasseraufnahme
def ask_water(button):
    # Öffnet ein Eingabefenster für die Wasseraufnahme in Litern
    glasses = simpledialog.askinteger("Wasseraufnahme", "Wie viele Gläser Wasser hast du getrunken? (250ml pro Glas)")
    if glasses is not None:
        # Wasseraufnahme zum Gesamtwert hinzufügen (1 Glas = 0.25 Liter)
        global total_water
        total_water += glasses * 0.25
        # Zeigt die Gesamtzahl der Wasseraufnahme an
        water_label.config(text=f"Gesamtwasseraufnahme heute: {total_water} Liter")
        # Button wird grün, nachdem ein Eintrag erfolgt ist
        button.config(bg="green", state="disabled")  # Button wird grün und deaktiviert


# Funktion für die Eingabe der Trainingszeit
def get_training_time():
    reminder_time = simpledialog.askstring("Trainingszeit festlegen", "Zu welcher Uhrzeit möchtest du einen Trainings-Reminder erhalten (HH:MM)?")
    if reminder_time:
        try:
            # Eingabe in ein Zeitobjekt umwandeln
            reminder_time_obj = datetime.strptime(reminder_time, "%H:%M").time()
            messagebox.showinfo("Erfolgreich", f"Erinnerung für {reminder_time_obj.strftime('%H:%M')} Uhr wurde erfolgreich gesetzt.")
            return reminder_time_obj  # Gibt die Zeit zurück
        except ValueError:
            messagebox.showerror("Ungültiges Format", "Bitte gib die Zeit im Format HH:MM ein.")
            return None
    return None

# Funktion, um eine Erinnerung mit Tkinter after() auszulösen
def check_and_remind_with_after(reminder_time, root):
    current_time = datetime.now().time()
    
    # Fall 1: Angegebene Zeit liegt in der Vergangenheit
    if current_time > reminder_time:
        messagebox.showinfo(
            "Training-Reminder",
            f"Deine eingegebene Zeit {reminder_time.strftime('%H:%M')} Uhr liegt in der Vergangenheit, aber hey, besser spät als nie – Zeit, loszulegen!"
        )
    else:
        # Fall 2: Angegebene Zeit liegt in der Zukunft
        def check_time():
            current_time = datetime.now().time()
            if current_time >= reminder_time:
                messagebox.showinfo(
                    "Erinnerung",
                    f"Es ist {reminder_time.strftime('%H:%M')} Uhr. Zeit für dein Training!"
                )
            else:
                root.after(1000, check_time)

        # Initialer Aufruf
        messagebox.showinfo(
            "Erinnerung geplant",
            f"Genieß die Ruhe vor dem Sturm, etwas Zeit hast du noch. Erinnerung wird ausgelöst."
        )
        check_time()

# Funktion zum Setzen der Trainingszeit
def set_training_time(root):
    reminder_time = get_training_time()
    if reminder_time:  # Nur wenn die Zeit gültig ist
        check_and_remind_with_after(reminder_time, root)
     
def track_training(training_label):
    global training_duration
    training_duration = simpledialog.askinteger("Trainingszeit eingeben", "Wie lange hast du trainiert? (Eingabe in Minuten)")
    if training_duration is not None:
        training_label.config(text=f"Deine heutige Trainingszeit beträgt {training_duration} Minuten")
        messagebox.showinfo("Training gespeichert", f"Trainingszeit gespeichert: {training_duration} Minuten")

def exit_application():
    # Verabschiedungsnachricht anzeigen
    messagebox.showinfo("Auf Wiedersehen!", "Danke, dass du WellBee genutzt hast. \n"
                        "Wir schicken dein Wochenergebnis an deine Email-Adresse\n"
                        "Bis bald! 😊")
    # GUI schließen
    root.destroy()


# Funktion zur Initialisierung des GUI
def create_gui():
    global total_calories, total_label, total_water, water_label, training_duration, training_label

    # Gesamtkalorien und Gesamtwasseraufnahme beginnen bei 0
    total_calories = 0
    total_water = 0

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Well Bee")
  
def handle_mood_selection(mood):
        if mood == "1":
            messagebox.showinfo("Reaktion", "Das ist großartig! Schön, dass es dir so gut geht! 😊")
            
        elif mood == "2":
            messagebox.showinfo("Reaktion", "Freut mich zu hören, dass es dir gut geht! 🙂")
            
        elif mood == "3":
            messagebox.showinfo("Reaktion", "It's me, hi, I'm the problem, it's me. Kaffee rettet dir den Tag! 😐")
            
        elif mood == "4":
            messagebox.showinfo("Reaktion", "Oh nein, Meh-Tage passieren. Morgen ist ein neuer Tag. 😕")
            
        elif mood == "5":
            messagebox.showinfo("Reaktion", "Hello darkness, my old friend. Tut mir leid zu hören, dass du einen schlechten Tag hast. 😔")
            

tk.Label(root, text="Willkommen zu deinem Habit Tracker!", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Tracke hier deine heutige Laune", font=("Arial", 16, "bold")).pack(pady=10)

# Bilder laden
very_happy_img = Image.open("very_happy_bee.png")  # Ersetze mit deinem Bildpfad
happy_img = Image.open("happy_bee.png")  # Ersetze mit deinem Bildpfad
coffee_img = Image.open("coffee_bee.png")  # Ersetze mit deinem Bildpfad
not_well_img = Image.open("not_well_bee.png")  # Ersetze mit deinem Bildpfad
very_sad_img = Image.open("very_sad_bee.png")  # Ersetze mit deinem Bildpfad

# Bilder: richtige Size definieren
very_happy_img = very_happy_img.resize((60,60), Image.Resampling.LANCZOS)
happy_img = happy_img.resize((60,60), Image.Resampling.LANCZOS)
coffee_img = coffee_img.resize((60,60), Image.Resampling.LANCZOS)
not_well_img = not_well_img.resize((60,60), Image.Resampling.LANCZOS)
very_sad_img = very_sad_img.resize((60,60), Image.Resampling.LANCZOS)

# Bilder in tkinter-kompatible Formate umwandeln
very_happy_img_tk = ImageTk.PhotoImage(very_happy_img)
happy_img_tk = ImageTk.PhotoImage(happy_img)
coffee_img_tk = ImageTk.PhotoImage(coffee_img)
not_well_img_tk = ImageTk.PhotoImage(not_well_img)
very_sad_img_tk = ImageTk.PhotoImage(very_sad_img)
    
  # Buttons erstellen
very_happy = Button(root, text="Super-duper fantastisch!", font=(8), image=very_happy_img_tk, bg="yellow", compound="left", command=lambda: handle_mood_selection("1"))
very_happy.image = very_happy_img_tk
very_happy.pack(side=TOP, padx=10, pady=5)

happy = Button(root, text="Ganz okay, ich bin ein Champion!", font=(8), image=happy_img_tk, bg="yellow", compound="left", command=lambda: handle_mood_selection("2"))
happy.image = happy_img_tk
happy.pack(side=TOP, padx=10, pady=5)

coffee = Button(root, text="Geht so... Kaffee hilft vielleicht.", font=(8), image=coffee_img_tk, bg="yellow", compound="left", command=lambda: handle_mood_selection("3"))
coffee.image = coffee_img_tk
coffee.pack(side=TOP, padx=10, pady=5)

not_well = Button(root, text="Meh, ich habe schon bessere Tage erlebt.", font=(8), image=not_well_img_tk, bg="yellow", compound="left", command=lambda: handle_mood_selection("4"))
not_well.image = not_well_img_tk
not_well.pack(side=TOP, padx=10, pady=5)

very_sad = Button(root, text="Ein wandelndes Chaos.", font=(8), image=very_sad_img_tk, bg="yellow", compound="left", command=lambda: handle_mood_selection("5"))
very_sad.image = very_sad_img_tk
very_sad.pack(side=TOP, padx=10, pady=5)

# Trennlinie (horizontal)
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=20)  


button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

#Frame für Trainingsabfrage    
training_frame = tk.Frame(root)
training_frame.pack(side=tk.TOP, pady=10)
    
tk.Label(training_frame, text="Tracke hier dein Training", font=("Arial", 16, "bold")).pack(pady=5)

#Lade Bilder für Trainingszeit festlegen
training_time_img = Image.open("trainingszeit.png")
training_time_img = training_time_img.resize((60,60), Image.Resampling.LANCZOS) 
training_time_img_tk = ImageTk.PhotoImage(training_time_img)

#Lade Bilder für Tracker
track_time_img = Image.open("tracker.png")
track_time_img = track_time_img.resize((60,60), Image.Resampling.LANCZOS) 
track_time_img_tk = ImageTk.PhotoImage(track_time_img)


# Button: Trainingszeit festlegen
training_time_button = tk.Button(training_frame, text="Trainingszeit festlegen", font=(8), image=training_time_img_tk, compound="top", bg="yellow", command=lambda: set_training_time())
training_time_button.pack(pady=5)

    
# Button: Training tracken
training_button = tk.Button(training_frame, text="Training tracken", font=(8), image=track_time_img_tk, compound="top", bg="yellow", command=lambda: track_training(training_label))
training_button.pack(pady=5)

training_label = tk.Label(training_frame, text=f'Deine heutige Trainingszeit beträgt {training_duration} Minuten', font=(6))
training_label.pack(side=tk.TOP, pady=10)

def set_training_time():
        reminder_time = get_training_time()
        if reminder_time:  # Nur wenn die Zeit gültig ist
            check_and_remind_with_after(reminder_time, root)

# Trennlinie (horizontal)
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=5)  # "fill='x'" sorgt dafür, dass die Linie die Breite des Fensters einnimmt

            
# Lade Bilder für die Mahlzeiten und Wasser
breakfast_img = Image.open("frühstück.png")  # Ersetze mit deinem Bildpfad
lunch_img = Image.open("mittag.png")  # Ersetze mit deinem Bildpfad
dinner_img = Image.open("abendessen.png")  # Ersetze mit deinem Bildpfad
snacks_img = Image.open("snack.png")  # Ersetze mit deinem Bildpfad
water_img = Image.open("wasser.png")  # Ersetze mit deinem Bildpfad für ein Glas Wasser

# Ändere die Größe der Bilder für die Labels
breakfast_img = breakfast_img.resize((60,60), Image.Resampling.LANCZOS)
lunch_img = lunch_img.resize((60,60), Image.Resampling.LANCZOS)
dinner_img = dinner_img.resize((60,60), Image.Resampling.LANCZOS)
snacks_img = snacks_img.resize((60,60), Image.Resampling.LANCZOS)
water_img = water_img.resize((60,60), Image.Resampling.LANCZOS)

# Konvertiere Bilder zu tkinter-kompatiblen Formaten
breakfast_img_tk = ImageTk.PhotoImage(breakfast_img)
lunch_img_tk = ImageTk.PhotoImage(lunch_img)
dinner_img_tk = ImageTk.PhotoImage(dinner_img)
snacks_img_tk = ImageTk.PhotoImage(snacks_img)
water_img_tk = ImageTk.PhotoImage(water_img)
    
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

tk.Label(button_frame, text="Tracke hier deine Nahrungsmittelzufuhr", font=("Arial", 16, "bold")).pack(pady=10)

# Erstelle Buttons mit Bild und Text für jede Mahlzeit und Wasseraufnahme
breakfast_button = tk.Button(button_frame, text="Frühstück", font=(4),image=breakfast_img_tk, compound="top", bg="yellow", command=lambda: ask_calories("Frühstück", breakfast_button))
breakfast_button.image = breakfast_img_tk  # Bild referenzieren
breakfast_button.pack(side=tk.LEFT, padx=10, pady=5)
    

lunch_button = tk.Button(button_frame, text="Mittagessen", font=(4), image=lunch_img_tk, compound="top", bg="yellow", command=lambda: ask_calories("Mittagessen", lunch_button))
lunch_button.image = lunch_img_tk  # Bild referenzieren
lunch_button.pack(side=tk.LEFT, padx=10, pady=5)
    

dinner_button = tk.Button(button_frame, text="Abendessen", font=(4), image=dinner_img_tk, compound="top", bg="yellow", command=lambda: ask_calories("Abendessen", dinner_button))
dinner_button.image = dinner_img_tk  # Bild referenzieren
dinner_button.pack(side=tk.LEFT, padx=10, pady=5)
    

snacks_button = tk.Button(button_frame, text="Snacks", font=(4), image=snacks_img_tk, compound="top", bg="yellow", command=lambda: ask_calories("Snacks", snacks_button))
snacks_button.image = snacks_img_tk  # Bild referenzieren
snacks_button.pack(side=tk.LEFT, padx=10, pady=5)
    
    
water_button = tk.Button(button_frame, text="Wasseraufnahme", font=(4), image=water_img_tk, compound="top", bg="yellow", command=lambda: ask_water(water_button))
water_button.image = water_img_tk  # Bild referenzieren
water_button.pack(side=tk.LEFT, padx=10, pady=5)
    
    
label_frame = tk.Frame(root)
label_frame.pack(side=tk.TOP, pady=10)

# Label zur Anzeige der Gesamtzahl der Kalorien
total_label = tk.Label(label_frame, text=f"Gesamtzahl der Kalorien heute: {total_calories} kcal", font=(6))
total_label.pack(side=tk.TOP, pady=10)
    

# Label zur Anzeige der Gesamtwasseraufnahme
water_label = tk.Label(label_frame, text=f"Gesamtwasseraufnahme heute: {total_water} Liter", font=(6))
water_label.pack(side=tk.TOP, pady=10)


# Button zum Beenden der Anwendung
exit_button = tk.Button(label_frame, text="Beenden", bg="yellow", fg="black", font=("Arial", 16, "bold"), command=exit_application, width=10, height=1)
exit_button.pack(pady=10)



# Startet das GUI
root.mainloop()
