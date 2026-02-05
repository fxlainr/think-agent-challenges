# L'Analyste de Réseau (LinkedIn Chat)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 180 |
| Prérequis | Compte LinkedIn, export de données |

---

## Vision & Impact

Ne plus scroller passivement mais "parler" à son réseau LinkedIn pour identifier des opportunités d'affaires cachées ou des experts spécifiques. Le réseau social devient une **base de données relationnelle active**.

## Le saviez-vous ?

L'IA peut désormais filtrer votre réseau pour extraire des signaux faibles d'intention d'achat ou de recrutement — changements de poste, publications, commentaires.

## Sources

- [Et si vous pouviez parler à votre réseau LinkedIn - Bruno Lu](https://www.linkedin.com/posts/brlu_et-si-vous-pouviez-parler-%C3%A0-votre-r%C3%A9seau-ugcPost-7422633809528926209-ZmRk)

---

## Description

> *Transformez votre réseau LinkedIn en base de données interrogeable.*

5000 connexions et aucune idée de qui peut vous aider ? Ce challenge vous fait créer un assistant qui connaît votre réseau et peut répondre : "Qui dans mon réseau travaille en cybersécurité à Lyon ?"

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Export et structuration de ses connexions LinkedIn
- [ ] Assistant capable de requêter le réseau
- [ ] Identification de 5 opportunités cachées

**Critères de réussite :**

- Requêtes en langage naturel fonctionnelles
- Au moins 1 opportunité non évidente découverte
- Workflow réutilisable

---

## Pistes de Solution

### Étape 1 : Exporter ses données LinkedIn

1. LinkedIn → Settings → Get a copy of your data
2. Sélectionner "Connections"
3. Recevoir le CSV par email (24-48h)

### Structure des données

```csv
First Name,Last Name,Email Address,Company,Position,Connected On
Jean,Dupont,jean@email.com,TechCorp,CTO,2023-05-15
```

### Enrichissement des données

```
Pour chaque connexion, enrichis avec :
- Secteur d'activité (déduit du Company)
- Séniorité (déduit du Position)
- Localisation (si disponible)
- Tags : [decision_maker, technical, same_industry...]
```

### Prompt système LinkedIn Assistant

```
Tu es un assistant d'analyse de réseau professionnel.

Voici mes connexions LinkedIn :
[INSÉRER DONNÉES CSV]

Tu peux m'aider à :
1. Trouver des profils selon des critères
2. Identifier des patterns dans mon réseau
3. Suggérer des introductions pertinentes
4. Détecter des opportunités business

Pour chaque recherche, donne :
- Les profils correspondants
- Pourquoi ils correspondent
- Comment les approcher (contexte commun)
```

### Requêtes types

**Recherche simple :**
- "Qui travaille dans la fintech ?"
- "Mes connexions CTO/VP Engineering ?"
- "Qui ai-je ajouté ces 6 derniers mois ?"

**Recherche croisée :**
- "Qui pourrait me présenter à quelqu'un chez Datadog ?"
- "Mes connexions qui ont changé de job récemment ?"
- "Qui dans mon réseau recrute en ce moment ?"

**Analyse :**
- "Quels secteurs sont surreprésentés dans mon réseau ?"
- "Où sont mes trous ? Quels profils me manquent ?"
- "Qui sont mes connexions les plus influentes ?"

### Détection d'opportunités

```
Analyse mon réseau et identifie :

## Opportunités de business development
- Entreprises en croissance (levée récente, recrutement massif)
- Décideurs accessibles (connexions de 2e degré proches)

## Opportunités de carrière
- Entreprises qui recrutent dans mon domaine
- Connexions qui pourraient recommander

## Opportunités de partenariat
- Profils complémentaires à mon activité
- Potentiels co-fondateurs ou associés

Pour chaque opportunité : Qui, Pourquoi maintenant, Comment approcher
```

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Exporter et structurer leurs données LinkedIn
- Créer un assistant de réseau intelligent
- Identifier des opportunités dans leurs connexions

### Prérequis

⚠️ **Demander l'export LinkedIn 48h AVANT l'atelier**

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-5 | Intro | Le problème du réseau inexploité |
| 5-15 | Démo | Assistant en action |
| 15-25 | Setup | Import des données dans l'assistant |
| 25-40 | Exploration | Requêtes et découvertes |
| 40-50 | Partage | Opportunités les plus surprenantes |
| 50-60 | Clôture | Stratégie de networking augmenté |

### Points d'attention animateur

- Rappeler l'export 48h avant
- Avoir un dataset de démo prêt
- Respecter la confidentialité des données

---

## Ressources complémentaires

- [LinkedIn Data Export](https://www.linkedin.com/help/linkedin/answer/50191)
- [Never Eat Alone - Keith Ferrazzi](https://keithferrazzi.com/never-eat-alone/)
