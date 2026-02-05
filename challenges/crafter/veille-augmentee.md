# Veille Augmentée

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | Tous |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 170 |
| Prérequis | Compte n8n (cloud ou self-hosted) |

---

## Vision & Impact

Créer une machine à veille autonome qui filtre les bruits du marché pour n'extraire que les **signaux faibles pertinents**. L'IA peut corréler des informations provenant de flux RSS et de réseaux sociaux pour identifier des tendances émergentes avant vos concurrents.

## Le saviez-vous ?

Les meilleurs Product Managers ne scrollent plus passivement — ils font travailler l'IA pour eux. Une veille automatisée bien configurée peut vous faire économiser 5-10h par semaine tout en ne manquant aucune information critique.

## Sources

- [J'ai créé une machine à veille avec l'IA - MATS Automation](https://www.linkedin.com/posts/matsautomation_jai-cr%C3%A9%C3%A9-une-machine-%C3%A0-veille-avec-lia-activity-7407313725482954752-j-wO)

---

## Description

> *Construisez un pipeline de veille automatisée qui filtre les pépites du web et vous livre une synthèse quotidienne personnalisée.*

Trop d'infos tue l'info. Newsletters, flux RSS, alertes... Impossible de tout suivre. Ce challenge vous fait créer un workflow n8n qui agrège vos sources, filtre avec l'IA ce qui est vraiment pertinent pour vous, et vous livre une synthèse quotidienne actionnable.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Workflow n8n fonctionnel avec au moins 2 sources
- [ ] Filtrage par pertinence (IA qui score les articles)
- [ ] Livraison automatique (Slack, email ou Notion)

**Critères de réussite :**

- Le workflow se déclenche automatiquement (schedule)
- Les articles non pertinents sont filtrés (pas de spam)
- La synthèse est lisible et actionnable

---

## Pistes de Solution

### Architecture du workflow

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│ Sources     │───▶│ Agrégation   │───▶│ Filtrage IA │───▶│ Distribution │
│ (RSS, API)  │    │ (n8n)        │    │ (LLM)       │    │ (Slack/Mail) │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
```

### Sources recommandées

**Veille technologique :**
- Hacker News : `https://hnrss.org/newest?points=100`
- TechCrunch : flux RSS du site
- Newsletters : TLDR, Ben's Bites (via email parsing)

**Veille concurrentielle :**
- Google Alerts (via email)
- LinkedIn des dirigeants (scraping)
- Communiqués de presse (Bodacc, societe.com)

### Nœuds n8n principaux

1. **Schedule Trigger** — Toutes les 4 heures
2. **RSS Feed Read** — Récupérer les articles
3. **OpenAI** — Scorer la pertinence
4. **IF** — Filtrer si pertinence ≥ 7
5. **Aggregate** — Regrouper les articles retenus
6. **OpenAI** — Générer la synthèse
7. **Slack/Email** — Envoyer

### Prompt de scoring

```
Analyse cet article et réponds en JSON :
{
  "pertinence": 1-10,
  "résumé": "2 phrases max",
  "tags": ["tag1", "tag2"],
  "actionable": true/false,
  "raison_pertinence": "pourquoi ce score"
}

Contexte : Je suis consultant en [domaine]. Je m'intéresse à [sujets].
Ignore les articles purement promotionnels ou hors sujet.
```

### Prompt de synthèse quotidienne

```
Voici les articles pertinents du jour. Génère une synthèse structurée :

## 🔥 À retenir absolument (1-3 points)
Les actualités les plus importantes

## 📊 Tendances observées
Ce qui émerge des différentes sources

## 💡 Opportunités identifiées
Ce que ça peut signifier pour notre activité

## 📚 Pour aller plus loin
Les liens vers les articles les plus intéressants
```

### Tips & astuces

- Commencer avec 1 seule source, ajouter ensuite
- Ajuster le seuil de pertinence (7 est un bon départ)
- Personnaliser le contexte dans le prompt de scoring

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les bonnes sources de veille pour leur métier
- Créer un workflow n8n de base (trigger → process → output)
- Utiliser l'IA pour filtrer et synthétiser l'information
- Automatiser une tâche récurrente de bout en bout

### Prérequis participants

- Compte n8n (cloud ou self-hosted)
- Accès aux credentials (Slack, OpenAI)
- 2-3 thèmes de veille identifiés

### Matériel nécessaire

- [ ] Instance n8n partagée ou comptes individuels
- [ ] Liste de flux RSS par domaine
- [ ] Template de workflow à importer
- [ ] Credentials pré-configurés (si environnement partagé)

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Montre un exemple de bulletin généré | Découvrent le livrable cible | Motivation |
| 5-15 | Démo workflow | Construit le workflow en live (simplifié) | Suivent, posent des questions | Comprendre n8n |
| 15-20 | Setup | Vérifie accès n8n, distribue le template | Importent le template | Préparation |
| 20-25 | Sources | Aide à identifier les bonnes sources | Choisissent leurs flux RSS | Personnalisation |
| 25-40 | Construction | Circule, debug | Adaptent le workflow | Pratique |
| 40-50 | Test | Fait tourner les workflows | Testent, corrigent | Validation |
| 50-55 | Synthèse | Montre les différentes approches | Partagent leurs choix | Apprentissage |
| 55-60 | Clôture | Explique comment étendre | Notent les idées | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Credentials mal configurés → Tester avant l'atelier
- Trop de sources d'un coup → Commencer avec 1
- Prompt de scoring trop vague → Donner le contexte métier précis

**Questions fréquentes :**

- "Comment trouver le flux RSS d'un site ?" → Extensions browser, ajouter /feed ou /rss
- "Mon workflow ne se déclenche pas" → Vérifier le trigger, activer le workflow
- "Les scores sont toujours à 10" → Affiner le prompt, donner des exemples de notes basses

**Tips d'animation :**

- Avoir un workflow de démo prêt
- Préparer une liste de flux RSS par domaine
- Montrer comment debugger avec les logs n8n

### Variantes

**Version simple (45 min) :**
- Workflow pré-construit, juste personnaliser les sources
- 1 seul flux RSS
- Pas de scoring IA, juste agrégation

**Version avancée (2h) :**
- Multi-sources (RSS + API + scraping)
- Stockage en base (Notion, Airtable)
- Alertes conditionnelles (si mention concurrent → notification urgente)

---

## Ressources complémentaires

- [Documentation n8n](https://docs.n8n.io/)
- [Liste de flux RSS tech](https://github.com/plenber/awesome-rss-feeds)
