# Podcast Running

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 30 min |
| Durée Dojo | 1h |
| Difficulté | ⭐ |
| Prérequis | Compte Google (pour NotebookLM) |

---

## Description

> *Générez un podcast pédagogique personnalisé à écouter pendant votre jogging — apprentissage passif au maximum.*

Vous courez 30 minutes ? C'est 30 minutes pour apprendre quelque chose. Ce challenge vous fait créer un podcast audio sur le sujet de votre choix, généré automatiquement par NotebookLM à partir de vos sources. Parfait pour le sport, les trajets ou la vaisselle.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Podcast audio de 5-15 minutes
- [ ] Sur un sujet de son choix
- [ ] Qualité audio écoutable pendant le sport

**Critères de réussite :**

- Le contenu est structuré et progressif
- Le ton est conversationnel (pas une lecture)
- On peut suivre sans regarder un écran

---

## Pistes de Solution

### Critères d'un bon sujet pour le sport

- **Narratif** — Histoires, anecdotes, parcours
- **Progressif** — Concepts qui s'enchaînent
- **Pas trop technique** — Éviter les schémas nécessaires

**Exemples :**
- Histoire d'une entreprise (Apple, Tesla, SpaceX)
- Biographie inspirante
- Concept expliqué simplement (blockchain, IA, quantique)
- Actualité décryptée

### Étape 1 : Rassembler les sources

Dans NotebookLM :
1. Créer un nouveau notebook
2. Ajouter 2-4 sources de qualité :
   - Articles Wikipedia
   - Vidéos YouTube (transcription)
   - Articles de blog/presse
   - PDF de livres/rapports

### Étape 2 : Structurer le contenu

**Prompt dans NotebookLM :**
```
Propose un plan de podcast de 10-15 minutes sur [sujet].

Structure :
1. Accroche (30 sec) - Pourquoi c'est intéressant
2. Contexte (2 min) - Le décor
3. Partie 1 (3 min) - Premier concept clé
4. Partie 2 (3 min) - Deuxième concept clé
5. Partie 3 (3 min) - Troisième concept clé
6. Conclusion (2 min) - Ce qu'il faut retenir
7. Ouverture (30 sec) - Pour aller plus loin

Ton conversationnel, comme si tu expliquais à un ami pendant un jogging.
```

### Étape 3 : Générer le podcast

1. Cliquer sur "Audio Overview" dans NotebookLM
2. Personnaliser si besoin :
   - "Ton dynamique et motivant"
   - "Focus sur [aspect spécifique]"
3. Générer (2-5 minutes)
4. Télécharger le MP3

### Exemple : "L'histoire de SpaceX en 10 minutes"

**Plan généré :**
```
1. ACCROCHE
   "En 2002, un entrepreneur sans expérience aérospatiale 
   décide de coloniser Mars. Tout le monde le prend pour un fou..."

2. CONTEXTE
   - Qui est Elon Musk en 2002
   - Pourquoi Mars ?

3. LES ÉCHECS
   - Falcon 1 : 3 échecs consécutifs
   - La quasi-faillite de 2008

4. LA RÉVOLUTION
   - Fusées réutilisables
   - L'atterrissage historique de 2015

5. AUJOURD'HUI
   - Starship et Mars
   - La nouvelle course à l'espace

6. CONCLUSION
   - Ce que SpaceX a changé
```

### Tips & astuces

- Sources en français = podcast en français
- La qualité du podcast dépend de la qualité des sources
- Télécharger sur le téléphone avant de partir courir !

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Utiliser NotebookLM pour synthétiser des sources
- Générer un podcast audio automatiquement
- Structurer un contenu pour l'écoute "en mobilité"

### Prérequis participants

- Compte Google
- Avoir identifié un sujet (ou en choisir un sur place)
- 2-3 sources sur leur sujet

### Matériel nécessaire

- [ ] Accès NotebookLM (notebook.google.com)
- [ ] Écouteurs pour écouter les podcasts
- [ ] Liste de sujets suggestions
- [ ] Sources prêtes pour les non-préparés

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Fait écouter 1 min d'un podcast généré | Découvrent le résultat | Inspiration |
| 5-15 | Sources | Aide à trouver des sources | Choisissent sujet + sources | Curation |
| 15-25 | Import | Vérifie les accès NotebookLM | Créent notebook, importent | Setup |
| 25-40 | Génération | Explique Audio Overview | Génèrent leur podcast | Production |
| 40-50 | Écoute | Fait écouter des extraits | Écoutent les créations | Valorisation |
| 50-60 | Clôture | Tips pour personnaliser | Partagent leurs sujets | Partage |

### Points d'attention animateur

**Pièges courants :**

- Sources anglaises = podcast anglais → Privilégier sources FR
- Temps de génération variable → Lancer tôt
- Sujet trop large → Cadrer ("L'IA" → "L'IA générative pour le marketing")

**Questions fréquentes :**

- "C'est long à générer ?" → 2-5 minutes
- "Je peux personnaliser la voix ?" → Partiellement via instructions
- "Ça marche hors connexion ?" → Oui une fois téléchargé

### Variantes

**Version express (30 min) :**
- Sources fournies (sujet commun)
- Génération directe sans structuration

**Version avancée (1h30) :**
- Multi-sources complexes
- Personnalisation poussée
- Série de podcasts thématiques

---

## Ressources complémentaires

- [NotebookLM](https://notebooklm.google.com/)
- [ElevenLabs](https://elevenlabs.io/) — alternative pour TTS personnalisé
