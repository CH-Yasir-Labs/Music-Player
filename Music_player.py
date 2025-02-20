#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     15/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Create main Tkinter window
root = tk.Tk()
root.title("Advanced Music Player")
root.geometry("600x500")
root.configure(bg="#1E1E1E")  # Dark theme background

# Global variables
playlist = []
current_song = None
paused = False

# Function to add music files
def add_music():
    global playlist
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    if files:
        playlist.extend(files)
        update_playlist()
    else:
        messagebox.showinfo("No Selection", "No file was selected.")

# Function to update playlist display
def update_playlist():
    playlist_box.delete(0, tk.END)
    for song in playlist:
        playlist_box.insert(tk.END, os.path.basename(song))

# Function to play selected song
def play_music():
    global current_song, paused
    try:
        selected_index = playlist_box.curselection()[0]
        song_path = playlist[selected_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        current_song = song_path
        paused = False
        status_label.config(text=f"Playing: {os.path.basename(song_path)}", fg="green")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a song to play.")

# Function to pause music
def pause_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
        status_label.config(text="Music Paused", fg="orange")

# Function to resume music
def resume_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        status_label.config(text=f"Playing: {os.path.basename(current_song)}", fg="green")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Music Stopped", fg="red")

# UI Design with ttk Widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), background="#1E1E1E", foreground="white")

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(pady=10)

playlist_box = tk.Listbox(frame, width=60, height=12, bg="#292929", fg="white", font=("Arial", 12), selectbackground="#444", selectforeground="white")
playlist_box.pack()

buttons_frame = tk.Frame(root, bg="#1E1E1E")
buttons_frame.pack(pady=10)

add_button = ttk.Button(buttons_frame, text="🎵 Add Music", command=add_music)
add_button.grid(row=0, column=0, padx=8, pady=5)

play_button = ttk.Button(buttons_frame, text="▶ Play", command=play_music)
play_button.grid(row=0, column=1, padx=8, pady=5)

pause_button = ttk.Button(buttons_frame, text="⏸ Pause", command=pause_music)
pause_button.grid(row=0, column=2, padx=8, pady=5)

resume_button = ttk.Button(buttons_frame, text="⏯ Resume", command=resume_music)
resume_button.grid(row=0, column=3, padx=8, pady=5)

stop_button = ttk.Button(buttons_frame, text="⏹ Stop", command=stop_music)
stop_button.grid(row=0, column=4, padx=8, pady=5)

status_label = ttk.Label(root, text="🎶 Welcome to Advanced Music Player", font=("Arial", 14, "bold"))
status_label.pack(pady=10)

# Run the GUI Event Loop
root.mainloop()
