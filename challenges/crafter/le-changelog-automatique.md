# Le Changelog Automatique

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Compte GitHub, n8n ou Python |

---

## Description

> *Créez un pipeline qui analyse vos Pull Requests et génère automatiquement des release notes claires pour vos utilisateurs.*

Écrire les release notes à la main, c'est pénible et souvent oublié. Ce challenge automatise tout : le pipeline collecte les PRs mergées, les classifie par type (feature, bug, amélioration) et génère un changelog orienté utilisateur — pas développeur.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline de collecte des PRs (GitHub API)
- [ ] Classification automatique par type
- [ ] Changelog lisible et orienté utilisateur
- [ ] Publication automatique (Slack, Notion ou fichier MD)

**Critères de réussite :**

- Les changements techniques sont traduits en bénéfices utilisateur
- Les catégories sont cohérentes (feature, bug, amélioration)
- Le changelog est publiable tel quel

---

## Pistes de Solution

### Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   GitHub    │───▶│   n8n        │───▶│   LLM       │───▶│   Output     │
│  (API)      │    │   (process)  │    │  (rédige)   │    │  (Slack/MD)  │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
```

### Catégories standard

| Emoji | Catégorie | Labels GitHub |
|-------|-----------|---------------|
| 🚀 | Nouvelles fonctionnalités | feature |
| 🐛 | Corrections de bugs | bug, fix |
| ⚡ | Améliorations | enhancement |
| 🔧 | Technique | tech, refactor |
| ⚠️ | Breaking Changes | breaking |
| 📚 | Documentation | docs |
| 🔒 | Sécurité | security |

### Prompt de classification

```
Analyse cette liste de PRs et classe chaque changement.

PRs à analyser :
{{prs_json}}

Pour chaque PR, détermine :
1. Catégorie : feature | bug | enhancement | tech | breaking | docs | security
2. Impact utilisateur : Oui/Non (visible par l'utilisateur final ?)
3. Résumé : Une phrase claire pour le changelog

Retourne en JSON.
```

### Prompt de rédaction

```
Tu es un rédacteur technique qui écrit des release notes claires et engageantes.

## Contexte
Application : {{app_name}}
Version : {{version}}
Audience : Utilisateurs finaux (pas les développeurs)

## Consignes
1. Résumé des points forts (2-3 phrases)
2. Grouper par catégorie (emoji + titre)
3. Pour chaque changement visible utilisateur :
   - Phrase simple et actionable
   - Bénéfice concret, pas de jargon
4. Section "Sous le capot" pour le technique
5. Remerciements aux contributeurs

Génère au format Markdown.
```

### Exemple de changelog généré

```markdown
# Release Notes - MonApp v2.4.0

📅 15 janvier 2025

## ✨ En bref
Export PDF enfin disponible, bug de déconnexion mobile corrigé, et performances améliorées de 40%.

## 🚀 Nouvelles fonctionnalités
- **Export PDF** : Exportez vos rapports en un clic. Parfait pour partager !
- **Filtres sauvegardés** : Vos filtres préférés sont mémorisés.

## 🐛 Corrections
- Déconnexion intempestive sur mobile après mise en veille
- Notifications manquantes sur Firefox

## ⚡ Améliorations
- Temps de chargement du dashboard réduit de 40%
- Meilleure lisibilité en mode sombre

## 🔧 Sous le capot
- Migration vers PostgreSQL 15
- Refactoring du cache

---
Merci à @alice, @bob et @charlie ! 🙏
```

### Tips & astuces

- Audience = utilisateurs, pas développeurs
- Fréquence recommandée : hebdo ou à chaque release
- Les labels GitHub bien utilisés simplifient la classification

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Automatiser la collecte depuis GitHub
- Utiliser l'IA pour classifier et rédiger
- Créer des release notes orientées utilisateur
- Mettre en place un pipeline reproductible

### Prérequis participants

- Compte GitHub avec accès à un repo
- Token GitHub (Settings → Developer settings → PAT)
- Compte n8n ou environnement Python

### Matériel nécessaire

- [ ] Template de workflow n8n
- [ ] Prompts de classification et rédaction
- [ ] Exemple de bon changelog
- [ ] Repo exemple avec PRs

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Bon vs mauvais changelog | Comprennent l'objectif | Motivation |
| 5-10 | Démo | Exécute le workflow complet | Voient le résultat | Vision |
| 10-15 | Setup | Aide à configurer le token | Créent leur token | Préparation |
| 15-25 | Collecte | Guide l'appel API GitHub | Configurent la collecte | Extraction |
| 25-35 | Classification | Montre le prompt | Adaptent à leur contexte | Intelligence |
| 35-45 | Rédaction | Guide la génération | Testent la génération | Rédaction |
| 45-55 | Publication | Montre les outputs (Slack, MD) | Choisissent leur canal | Distribution |
| 55-60 | Clôture | Planification de l'automatisation | Notent la prochaine étape | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Token GitHub avec mauvais scopes → Vérifier `repo` scope
- Pas de PRs récentes → Avoir un repo exemple prêt
- Changelog trop technique → Insister sur l'audience utilisateur

**Questions fréquentes :**

- "Commits au lieu des PRs ?" → Possible, mais PRs donnent plus de contexte
- "Repos privés ?" → Token avec scope `repo` suffit
- "Quelle fréquence ?" → Hebdo ou à chaque release

### Variantes

**Version simple (45 min) :**
- PRs manuellement sélectionnées
- Focus sur le prompt de rédaction
- Output fichier Markdown

**Version avancée (2h) :**
- Multi-repos
- Versioning automatique (semver)
- Push du CHANGELOG.md dans le repo

---

## Ressources complémentaires

- [Keep a Changelog](https://keepachangelog.com/)
- [GitHub REST API](https://docs.github.com/en/rest)
