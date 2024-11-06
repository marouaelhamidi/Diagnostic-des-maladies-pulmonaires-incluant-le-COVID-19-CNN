import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import customtkinter as ctk
from tkinter.ttk import Progressbar, Style
import warnings

# Suppress specific TensorFlow warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Compiled the loaded model, but the compiled metrics have yet to be built.")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Covid-19 Prediction")
        screen_width = int(self.winfo_screenwidth() * 0.99)
        screen_height = int(self.winfo_screenheight() * 0.90)
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Configuration du thème CustomTkinter
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Configuration de la couleur de fond
        self.configure(fg_color='#f0f8ff')  # Bleu clair comme arrière-plan
        
        try:
            # Chargement du modèle .h5
            self.model = tf.keras.models.load_model("model_28-06-2024.h5")
            # Optionally, print the model summary to ensure it's loaded correctly
            # print("Model summary:\n", self.model.summary())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {e}")
            self.destroy()
            return
        
        # Création de l'interface utilisateur
        self.create_ui()

    def create_ui(self):
        # Chargement et affichage du logo
        try:
            self.logo_image = Image.open("ISGA.png").resize((240, 150))
            self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
            self.logo_image_label = tk.Label(self, image=self.logo_image_tk, bg='#ccffcc')
            self.logo_image_label.image = self.logo_image_tk  # reference img tkinter
            self.logo_image_label.pack(padx=20, pady=30)
      
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load logo: {e}")
        
        # Titre de l'application
        title_label = ctk.CTkLabel(self, text="Diagnostic des maladies pulmonaires", font=("Arial", 30, "bold"), text_color="#0056a0", fg_color='#f0f8ff')
        title_label.pack(pady=(10, 30))
        
        # Bouton pour importer une image
        self.import_button = ctk.CTkButton(self, text="Importer Image", command=self.perform_prediction, width=250, height=70, font=("Arial", 20, "bold"), fg_color="#4da6ff", hover_color="#3399ff")
        self.import_button.pack(pady=20)
        
        # Cadre pour l'image importée
        self.image_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#ffffff", border_width=2, border_color="#cccccc")
        self.image_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Label pour l'image importée
        self.lung_img = ctk.CTkLabel(self.image_frame, text="", fg_color="#ffffff")
        self.lung_img.pack(padx=10, pady=10)
        
        # Cadre pour les résultats
        self.result_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#ffffff", border_width=2, border_color="#cccccc")
        self.result_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Label pour le résultat
        self.result_label = ctk.CTkLabel(self.result_frame, text="", font=("Arial", 24, "bold"), text_color="#000000", fg_color="#ffffff")
        self.result_label.pack(pady=10)
        
        # Label pour la confiance
        self.confidence_label = ctk.CTkLabel(self.result_frame, text="", font=("Arial", 18), fg_color="#ffffff")
        self.confidence_label.pack(pady=10)
        
        # Barre de progression
        style = Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=30, troughcolor='#f0f8ff', background='#4da6ff')

        self.progress_bar = Progressbar(self, orient="horizontal", length=500, mode="determinate", style="TProgressbar")
        self.progress_bar.pack(pady=20)
        
        # Étiquette de progression
        self.progress_label = ctk.CTkLabel(self, text="0%", font=("Arial", 16), fg_color='#f0f8ff')
        self.progress_label.pack()

    def open_image(self):
        image_path = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                                filetypes=(("All files", "*.*"), ("PNG files", "*.png")))
        if not image_path:
            return None
        
        img = Image.open(image_path)
        resized_img = img.resize((400, 400))
        img_tk = ImageTk.PhotoImage(resized_img)
        self.lung_img.configure(image=img_tk)
        self.lung_img.image = img_tk  # Référence pour l'image tkinter
        return image_path

    def predict_covid(self, img_path):
        try:
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0  # Normalisation

            # Prédiction
            results = self.model.predict(img_array)
            return results
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {e}")
            return None

    def perform_prediction(self):
        path = self.open_image()
        if path:
            # Réinitialiser la barre de progression
            self.progress_bar['value'] = 0
            self.progress_label.configure(text="0%")
            self.update_idletasks()

            results = self.predict_covid(path)
            if results is not None:
                if results[0][0] > 0.5:
                    self.result_label.configure(text='Covid-19', text_color='#FF4C4C')
                elif results[0][1] > 0.5:
                    self.result_label.configure(text='Normal', text_color='#4DA6FF')
                elif results[0][2] > 0.5:
                    self.result_label.configure(text='Virus Pulmonaire', text_color='#FF9999')
                else:
                    self.result_label.configure(text='Inconnu', text_color='#000000')
                
                confidence = results[0][np.argmax(results)] * 100
                self.confidence_label.configure(text=f'Confidence: {confidence:.2f}%')
                self.progress_bar['value'] = confidence
                self.progress_label.configure(text=f'{confidence:.2f}%')
                self.update_idletasks()

if __name__ == "__main__":
    app = App()
    app.mainloop()
