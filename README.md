# 🏨 Mini-Projet : Analyse Exploratoire de la Demande Hôtelière (EDA)

**Cours :** 8PRO408 - Outils de programmation pour la science des données
**Date de remise :** 10 décembre 2025

## 📋 Description du Projet
Ce projet consiste en une analyse exploratoire (EDA) du jeu de données `hotel_bookings.csv` (119 390 réservations). L'objectif est de comparer les performances, les tendances tarifaires (ADR) et les comportements d'annulation entre les **City Hotels** et les **Resort Hotels**, et de synthétiser ces résultats dans un rapport et une application interactive.

## ⚙️ Exécution du Projet

### 1. Prérequis
Pour exécuter le notebook et l'application Streamlit, vous devez disposer de Python 3.8+ et des librairies suivantes.

Le fichier `requirements.txt` contient la liste complète des dépendances.

```bash
# Créer et activer un environnement virtuel (optionnel mais recommandé)
# python -m venv venv
# source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate   # Windows
```

# Installation des dépendances

```bash
pip install -r requirements.txt
```

### 2. Organisation des Fichiers

Assurez-vous que les fichiers sont organisés comme suit :

```
.
├── data/
│   └── hotel_bookings.csv  # Le jeu de données
├── EDA_Hotel_Bookings.ipynb  # Notebook Jupyter (L'analyse complète)
├── Streamlit_app.py              # L'application Streamlit interactive
├── Rapport_Final.pdf   # Le rapport de synthèse (1-2 pages)
├── requirements.txt    # Liste des dépendances (si tu l'as créée)
└── README.md           # Ce fichier
```

### 3. Étapes d'exécution

#### A. Exécution du Notebook Jupyter

Le notebook EDA_Hotel_Bookings.ipynb contient toutes les étapes de nettoyage, d'analyse et les visualisations statiques (Matplotlib/Seaborn).

Lancer Jupyter Lab ou Jupyter Notebook :

``` Bash
jupyter notebook
```

Ouvrir et exécuter le notebook EDA_Hotel_Bookings.ipynb de haut en bas.

#### B. Lancement de l'application Streamlit

L'application app.py fournit un tableau de bord interactif pour explorer la saisonnalité, la provenance des clients et la distribution des prix (Plotly).

S'assurer d'être dans le répertoire du projet.

Lancer l'application :

``` Bash
streamlit run Streamlit_app.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut (http://localhost:8501).

### 🔑 Variables Clés Analysées
**hotel** : Type d'hôtel (City Hotel ou Resort Hotel).

**is_canceled** : Indique si la réservation a été annulée (1) ou non (0).

**adr** (Average Daily Rate) : Prix moyen par jour.

**lead_time** : Nombre de jours entre la date de réservation et la date d'arrivée.

**arrival_date_month** : Pour l'analyse de la saisonnalité.