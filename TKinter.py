from tkinter import *
from tkinter import messagebox, simpledialog

# Initialise les variables à 0
soldes_comptes = [0] * 10
tableau_des_nom_comptes = []
mot_de_passe_comptes = []
nombres_comptes = 0
compte_selection_num = 0
compte_selection_name = 0

fenetre = Tk()  # Initialise la variable fenetre
menubar = Menu(fenetre)  # Initialise la variable menubar

def apropos():  # test
    messagebox.showinfo("[Infos Développeurs]", "[Développé par Maxence HINCELIN et Lilah BRYANT]")  # Affiche les infos développeur dans fenetre externe

def Quitter():  # Quitter le programme
    if messagebox.askyesno('[Confirmation]', '[Êtes-vous sûr de vouloir faire cela ?]'):  # confirmation
        fenetre.destroy()
    else:
        messagebox.showinfo('[Annulation]', '[Fermeture du Programme Annulé]')  # annulation

def CreationCompte():  # créer un compte
    global nombres_comptes, tableau_des_nom_comptes
    supprimer_widgets()
    
    frame = LabelFrame(fenetre, bd=15, text="[Création de Comptes]", fg="blue", font=("Arial", 25, "bold")) 
    frame.pack(pady=(150, 0))
    
    boutonCreerCompte = Button(frame, text="[Créer un compte]", relief=RAISED, fg="green", font=("Arial", 15, "bold"), command=DemandeCreationCompte)
    boutonCreerCompte.pack()  # Bouton créer compte
    
    boutonAnnuler = Button(frame, text="[Annulation]", fg="red", relief=RAISED, font=("Arial", 15, "bold"), command=supprimer_widgets)
    boutonAnnuler.pack()  # Bouton pour annulé la création du compte
    
def DemandeCreationCompte():  # Vérification pour la création du compte
    global nombres_comptes, tableau_des_nom_comptes, mot_de_passe_comptes
    supprimer_widgets()

    nom_compte = simpledialog.askstring("[Nouveau Compte]", "[Entrer votre nom de compte] =>")  # entrer le nom de compte
    if nom_compte:
        tableau_des_nom_comptes.append(nom_compte)
        mot_de_passe = simpledialog.askstring("[Nouveau Compte]", "[Entrer votre mot de passe] =>", show='*')  # entrer le mot de passe
        if mot_de_passe:
            mot_de_passe_comptes.append(mot_de_passe)
            nombres_comptes += 1  # nombres de comptes augmente de 1
            
            supprimer_widgets()
            
            frame = LabelFrame(fenetre, bd=15, text="[Validation de La Création]", fg="blue", font=("Arial", 25, "bold")) 
            frame.pack(pady=(150, 0))
            
            AfficheNC = Label(frame, text=f'[Voici votre Numéro de Compte] => {nombres_comptes}\n[Propriétaire du Compte] => {nom_compte}', fg="green", font=("Arial", 15, "bold"))  # affiche le numéro de compte et son nom
            AfficheNC.pack()  # Place le label dans le cadre
            
            boutonValidCC = Button(frame, text="[Valider la Creation du Compte]", fg="green", font=("Arial", 15, "bold"), command=valider_creation_compte)  # cas comptes créer
            boutonValidCC.pack(pady=(20, 0))
            
            boutonAnnuler = Button(frame, text="[Annulation]", fg="red", relief=RAISED, font=("Arial", 15, "bold"), command=supprimer_widgets_annulationc)  # cas annulation
            boutonAnnuler.pack(pady=(20, 0))
        else:
            messagebox.showerror("Erreur", "Le mot de passe ne peut pas être vide.")
    else:
        messagebox.showerror("Erreur", "Le nom de compte ne peut pas être vide.")

def valider_creation_compte():  # cas comptes créer
    supprimer_widgets()
    frame = LabelFrame(fenetre, bd=15) 
    frame.pack(pady=(150, 0))
    VCC = Label(frame, text='[Validation de la Creation du Compte]', fg='green', font=("Arial", 15, "bold"))
    VCC.pack()
    fenetre.after(3000, StatusQuo)  # Détruit le cadre et le label après 3 secondes

def supprimer_widgets_annulationc():  # cas comptes créer annulation
    global nombres_comptes, tableau_des_nom_comptes, mot_de_passe_comptes
    for widget in fenetre.winfo_children():
        if widget != menubar:
            widget.destroy()
    if nombres_comptes > 0:
        nombres_comptes -= 1
        tableau_des_nom_comptes.pop()
        mot_de_passe_comptes.pop()

def supprimer_widgets():  # suppression de la fenetre hormis menu principal
    for widget in fenetre.winfo_children():
        if widget != menubar:
            widget.destroy()

def AfficheComptes():
    global nombres_comptes, tableau_des_nom_comptes

    supprimer_widgets()  # Efface tous les widgets actuellement affichés

    frame = LabelFrame(fenetre, text=f"[Liste des Comptes] || [{nombres_comptes} Présents]", fg="blue", bd=18, font=("Arial", 25, "bold"))  # Crée un LabelFrame pour afficher les comptes avec une bordure de 15 pixels
    frame.pack(pady=(150, 0))  # Place le cadre à 50 pixels du haut et ajoute un padding horizontal de 50 pixels

    for i in range(nombres_comptes):
        nom_compte = tableau_des_nom_comptes[i]  # Récupère le nom du compte à partir du tableau
        num_compte = i + 1  # Numéro du compte (commence à 1)

        # Affiche le nom du compte à gauche
        label_nom_compte = Label(frame, text=f'[Numéro du Compte] => {num_compte} \n [Propriétaire] => {nom_compte}\n')
        label_nom_compte.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        
        # Affiche le bouton "Sélectionner" à droite
        bouton_selectionner = Button(frame, text="[Sélectionner]", fg="green", relief=RAISED, font=("Arial", 15, "bold"), command=lambda num=num_compte: selectionner_compte(num))
        bouton_selectionner.grid(row=i, column=1, padx=10, pady=5, sticky="e")

def selectionner_compte(num_compte):
    global mot_de_passe_comptes, tableau_des_nom_comptes, compte_selection_name, compte_selection_num
    mdp = simpledialog.askstring("Vérification du mot de passe", "Entrez votre mot de passe:", show='*')
    if mdp == mot_de_passe_comptes[num_compte - 1]:
        compte_selection_name = tableau_des_nom_comptes[num_compte - 1]
        compte_selection_num = num_compte
        supprimer_widgets()
        frame = LabelFrame(fenetre, text=f"[Compte Chargé]", fg="blue", bd=18, font=("Arial", 25, "bold"))  # Crée un LabelFrame pour afficher les comptes avec une bordure de 15 pixels
        frame.pack(pady=(150, 0))
        SelecC = Label(frame, text=f"[Vous avez sélectionné le compte {num_compte} => {compte_selection_name}]", fg="green", font=("Arial", 15, "bold"))
        SelecC.pack()
        fenetre.after(3000, StatusQuo)  # Retour à l'état initial après 3 secondes
    else:
        messagebox.showerror("[Erreur]", "[Mot de passe incorrect]")
        selectionner_compte(num_compte)

def SuppresionCompte(num_comptes):
    global nombres_comptes, tableau_des_nom_comptes

    supprimer_widgets()  # Efface tous les widgets actuellement affichés

    frame = LabelFrame(fenetre, text=f"[Liste des Comptes] || [{nombres_comptes} Présents]", fg="red", bd=18, font=("Arial", 25, "bold"))  # Crée un LabelFrame pour afficher les comptes avec une bordure de 15 pixels
    frame.pack(pady=(150, 0))  # Place le cadre à 50 pixels du haut et ajoute un padding horizontal de 50 pixels

    for i in range(nombres_comptes):
        nom_compte = tableau_des_nom_comptes[i]  # Récupère le nom du compte à partir du tableau
        num_compte = i + 1  # Numéro du compte (commence à 1)

        # Affiche le nom du compte à gauche
        label_nom_compte = Label(frame, text=f'[Numéro du Compte] => {num_compte} \n [Propriétaire] => {nom_compte}\n')
        label_nom_compte.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        
        # Affiche le bouton "Sélectionner" à droite
        bouton_selectionner = Button(frame, text="[Supprimer]", fg="red", relief=RAISED, font=("Arial", 15, "bold"), command=lambda num=num_compte: active_supprimer(num))
        bouton_selectionner.grid(row=i, column=1, padx=10, pady=5, sticky="e")

def verif_supp(num_compte):
    global mot_de_passe_comptes, tableau_des_nom_comptes, compte_selection_name, compte_selection_num
    
    mdp = simpledialog.askstring("[Vérification du mot de passe]", "[Entrez votre mot de passe] => ", show='*')#verif mot de passe
    supprimer_widgets()  # Efface tous les widgets actuellement affichés
    
    frame = LabelFrame(fenetre, text=f"[Etes-vous ceertain de la suppresion du compte ?]", fg="red", bd=18, font=("Arial", 25, "bold"))  # Crée un LabelFrame pour afficher les comptes avec une bordure de 15 pixels
    frame.pack(pady=(150, 0))  # Place le cadre à 50 pixels du haut et ajoute un padding horizontal de 50 pixels
    
    verifvalide = Button(frame, text="[Valider la suppression]", fg="red", font=("Arial", 15, "bold"), command=verif_supp_ok)
    verifvalide.pack(pady=(20, 0))
            
    verifannule = Button(frame, text="[Annulation]", fg="green", relief=RAISED, font=("Arial", 15, "bold"), command=supprimer_widgets_annulationc)  # cas annulation
    verifannule.pack(pady=(20, 0))
    
    
    supprimer_widgets()  # Efface tous les widgets actuellement affichés
    
    if mdp == mot_de_passe_comptes[num_compte - 1] & verifvalide==1:
        compte_selection_name = tableau_des_nom_comptes[num_compte - 1]
        compte_selection_num = num_compte
        supprimer_widgets()
        frame = LabelFrame(fenetre, text=f"[Compte Supprimer]", fg="red", bd=18, font=("Arial", 25, "bold"))  # Crée un LabelFrame pour afficher les comptes avec une bordure de 15 pixels
        frame.pack(pady=(150, 0))
        fenetre.after(3000, StatusQuo)  # Retour à l'état initial après 3 secondes
    else:
        messagebox.showerror("[Erreur]", "[Mot de passe incorrect]")
           
def StatusQuo():
    global compte_selection_name, compte_selection_num
    supprimer_widgets()
    frame = LabelFrame(fenetre, bd=15, text="[Menu Principal des Comptes]", fg="green", font=("Arial", 25, "bold")) 
    frame.pack(pady=(150, 0))

    # Création du libellé pour afficher le compte actif
    label_compte_actif = Label(frame, font=("Arial", 25, "bold"))

    if compte_selection_num != 0:
        label_compte_actif.config(text=f"[Compte Actif => {compte_selection_name}] \n [Numéro] => {compte_selection_num}", fg="blue")              
    else:
        label_compte_actif.config(text="[Compte non-chargé !]", fg="red")

    # Ajout du libellé à la fenêtre principale
    label_compte_actif.pack()

def Menu_Principal():  # menu principal
    global fenetre, menubar, compte_selection
    
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="[Ouverture]", command=apropos)
    menu1.add_separator()
    menu1.add_command(label="[Edition]", command=apropos)
    menu1.add_separator()
    menu1.add_command(label="[Quitter]",  command=Quitter)
    menubar.add_cascade(label="[Fichier]", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="[Création Compte]", command=CreationCompte)
    menu2.add_separator()
    menu2.add_command(label="[Suppresion Compte]", command=SuppresionCompte)
    menu2.add_separator()
    menu2.add_command(label="[Choix du Compte]",  command=AfficheComptes)
    menubar.add_cascade(label="[Compte]", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="[Développeurs]", command=apropos)
    menubar.add_cascade(label="[Infos]", menu=menu3)

    fenetre.config(menu=menubar)

    StatusQuo()
    fenetre.mainloop()

Menu_Principal()
