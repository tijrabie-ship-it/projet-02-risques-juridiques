# Projet 02 — Risques juridiques de la mourabaha

Application académique développée en Python avec Streamlit.
Elle applique des règles de contrôle aux réponses renseignées
par l’utilisateur.

## Fonctionnalités

Le contrôle principal porte sur quatre critères :
- Documentation du contrat auprès d’une autorité compétente.
- Paiement des droits d’enregistrement et de timbre.
- Présence d’une clause de force exécutoire.
- Désignation des juridictions marocaines dans la clause de règlement des litiges.

Selon les réponses, l’application affiche un message de conformité
aux critères, d’insuffisance juridique ou de risque élevé.

Une seconde unité évalue conjointement la documentation,
la clause de force exécutoire et l’enregistrement du contrat.

## Fichiers
- `app.py` : interface et règles de contrôle.
- `requirements.txt` : dépendance nécessaire.

## Exécution locale

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

Ouvrir l’adresse locale indiquée dans le terminal.

## Portée

Ce prototype effectue un contrôle fondé sur les réponses de
l’utilisateur. Il ne vérifie pas automatiquement les documents
ni la validité juridique effective du contrat.
