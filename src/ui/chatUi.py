import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from ai.ai import generate_structured_response, generate_content


def generateEssay(topic, word_count, additional_details):
    essay = generate_content(topic, word_count, additional_details)
    print(essay)

def chatUI(parent):
    entryBoxRow = ctk.CTkFrame(parent, fg_color="#00224B",  height= 50)
    entryBoxRow.grid(row=6, column=1, sticky="SEW", padx=5, pady=5)
    entryBoxRow.columnconfigure(3, weight=1)

    topic = ctk.CTkEntry(entryBoxRow, placeholder_text="Topic")
    topic.grid(row=1, column=1, sticky="ew", padx=5, pady=20)

    wordCount = ctk.CTkEntry(entryBoxRow, placeholder_text="Word Count")
    wordCount.grid(row=1, column=2, sticky="ew", padx=5, pady=20)

    additionalDetails = ctk.CTkEntry(entryBoxRow, placeholder_text="Additonal Details")
    additionalDetails.grid(row=1, column=3, sticky="ew", padx=5, pady=20)

    sendToAiButton: CTkButton = ctk.CTkButton(entryBoxRow, text="Send ↑", command=lambda: generateEssay(topic.get(), wordCount.get(), additionalDetails.get()))
    sendToAiButton.grid(row=1, column=4, sticky="ew", padx=5)

    