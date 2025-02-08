import os
import tkinter as tk
from tkinter import messagebox

# Chemin vers Minecraft
MINECRAFT_DIR = os.path.expanduser("~/.minecraft")
MINECRAFT_VERSION = "1.20.1"
JAR_PATH = os.path.join(MINECRAFT_DIR, "versions", MINECRAFT_VERSION, f"{MINECRAFT_VERSION}.jar")

def launch_minecraft():
    if os.path.exists(JAR_PATH):
        os.system(f"java -Xmx2G -jar \"{JAR_PATH}\"")
    else:
        messagebox.showerror("Erreur", "Minecraft n'est pas installé ou la version est manquante.")

# Interface graphique
root = tk.Tk()
root.title("MaxLuncher")

label = tk.Label(root, text="Bienvenue dans le Launcher !", font=("Arial", 14))
label.pack(pady=20)

play_button = tk.Button(root, text="Jouer", command=launch_minecraft, font=("Arial", 12))
play_button.pack(pady=10)

root.mainloop()
