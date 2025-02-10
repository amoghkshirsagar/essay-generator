import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from ai.ai import generate_structured_response, generate_content


def generateEssay(entryList, parent):
    topic = entryList['topic']['entry']
    wordCount = entryList['wordCount']['entry']
    additionalDetails = entryList['additionalDetails']['entry']

    essay = generate_content(topic.get(), wordCount.get(), additionalDetails.get())

    essayFrame = ctk.CTkScrollableFrame(parent, fg_color="#00224B",  height= 50)
    essayFrame.grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)
    essayFrame.rowconfigure(0, weight=1)
    essayFrame.columnconfigure(0, weight=1)

    essayDisplay: CTkLabel = ctk.CTkLabel(essayFrame, fg_color="#001B3A", text=essay, wraplength=300)
    essayDisplay.grid(row=0, column=0, sticky="NSEW", padx=10, pady=5)

def chatUI(parent):
    entryBoxRow = ctk.CTkFrame(parent, fg_color="#00224B",  height= 50)
    entryBoxRow.grid(row=6, column=1, sticky="SEW", padx=5, pady=5)
    entryBoxRow.columnconfigure(3, weight=1)

    entryList = {
        "topic": {"label": "Topic", "entry": None},
        "wordCount": {"label": "Word Count", "entry": None},
        "additionalDetails": {"label": "Additional Details", "entry": None}
    }

    for i, (key, value) in enumerate(entryList.items()):
        value['entry'] = ctk.CTkEntry(entryBoxRow, placeholder_text=value['label'])
        value['entry'].grid(row=1, column=i+1, sticky="ew", padx=5, pady=20)

    sendToAiButton: CTkButton = ctk.CTkButton(entryBoxRow, text="Send ↑", command=lambda: generateEssay(entryList, parent))
    sendToAiButton.grid(row=1, column=4, sticky="ew", padx=5)
