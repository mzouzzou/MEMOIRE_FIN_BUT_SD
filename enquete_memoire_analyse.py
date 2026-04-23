import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. IMPORT DES DONNÉES
# =========================

df = pd.read_csv("SID_Reponses_Analyse_IA_Form_Responses.csv")

print("Aperçu des données :")
print(df.head())

print("\nColonnes :")
print(df.columns)

print("\nInfos :")
print(df.info())


# =========================
# 2. FREQUENCE D'UTILISATION
# =========================

plt.figure(figsize=(8,5))

freq = df["Fréquence d’utilisation de l’IA au travail"].value_counts()
freq.plot(kind='bar')

plt.title("Fréquence d'utilisation de l'IA")
plt.xlabel("Fréquence")
plt.ylabel("Nombre de réponses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("frequence_utilisation_ia.png")

plt.show()


# =========================
# 3. OUTILS UTILISÉS
# =========================

outils = df["Quels outils d’IA utilisez-vous au travail ?"].str.split(", ").explode()

plt.figure(figsize=(8,5))

outils.value_counts().plot(kind='bar')

plt.title("Outils d'IA utilisés")
plt.xlabel("Outils")
plt.ylabel("Nombre de réponses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outils_ia.png")

plt.show()


# =========================
# 4. TYPES DE TÂCHES
# =========================

taches = df["Pour quels types de tâches utilisez-vous l’IA ?"].str.split(", ").explode()

plt.figure(figsize=(8,5))

taches.value_counts().plot(kind='bar')

plt.title("Types de tâches réalisées avec l'IA")
plt.xlabel("Types de tâches")
plt.ylabel("Nombre de réponses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("types_taches_ia.png")

plt.show()


# =========================
# 5. ANALYSE DES PERCEPTIONS
# =========================

likert_cols = [
    "L’IA me fait gagner du temps.",
    "L’IA améliore la qualité de mon travail.",
    "Je fais confiance aux résultats produits.",
    "Je maîtrise la rédaction de prompts efficaces.",
    "Je connais les règles de sécurité liées à l’IA.",
    "L’usage d’IA cloud présente un risque pour les données sensibles.",
    "Une solution IA interne serait plus sécurisée.",
    "Je serais favorable à une IA intégrée au SI."
]

# Conversion en numérique
df[likert_cols] = df[likert_cols].apply(pd.to_numeric)

# Moyennes
moyennes = df[likert_cols].mean()
print("\nMoyennes des perceptions :")
print(moyennes)

# Graphique
plt.figure(figsize=(10,6))

moyennes.plot(kind='bar')

plt.title("Perception des utilisateurs vis-à-vis de l'IA")
plt.xlabel("Indicateurs")
plt.ylabel("Moyenne (sur 5)")
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig("perception_utilisateurs.png")

plt.show()


# =========================
# 6. ADOPTION D’UNE IA SÉCURISÉE
# =========================

plt.figure(figsize=(8,5))

df["Si une solution IA sécurisée était mise à disposition, l'utiliseriez-vous ?"].value_counts().plot(kind='bar')

plt.title("Adoption d'une IA sécurisée")
plt.xlabel("Réponse")
plt.ylabel("Nombre de réponses")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("adoption_ia_securisee.png")

plt.show()