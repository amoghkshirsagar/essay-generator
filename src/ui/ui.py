import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from ui.chatUi import chatUI

def addAppContent(app: CTkFrame):

    appContent: CTkFrame = ctk.CTkFrame(app, fg_color="black")
    appContent.grid(row=0, sticky="NSEW")
    appContent.rowconfigure(0, weight=1)
    appContent.columnconfigure(1, weight=1)

    frame1: CTkFrame = ctk.CTkFrame(appContent)
    frame1.grid(row=0, column=0, sticky="NSEW")
    frame1.rowconfigure(2, weight=1)

    mainArea = ctk.CTkFrame(appContent, fg_color="#003166")
    mainArea.grid(row=0, column=1, sticky="NSEW")
    mainArea.rowconfigure(1, weight=1)
    mainArea.columnconfigure(1, weight=1)

    titleRow: CTkFrame = ctk.CTkFrame(mainArea, height=50, fg_color="#00224B")
    titleRow.grid(row=0, column=1, sticky="NSEW", pady=5)
    titleRow.columnconfigure(1, weight=1)

    titleLabel: CTkLabel = ctk.CTkLabel(titleRow, fg_color="#001B3A", text="Essay writer")
    titleLabel.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

    chatArea = ctk.CTkFrame(mainArea, fg_color="#003166")
    chatArea.grid(row=1, column=1, sticky="NSEW")
    chatArea.rowconfigure(6, weight=1)
    chatArea.columnconfigure(1, weight=1)

    chatUI(chatArea)

def buildAppUi():
    app: CTk = ctk.CTk()
    app.geometry("900x800")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    addAppContent(app)

    app.mainloop()