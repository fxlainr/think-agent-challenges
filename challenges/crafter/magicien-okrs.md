# Le Magicien des OKRs (Tability AI)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 190 |
| Prérequis | Notions d'OKRs |

---

## Vision & Impact

"Parler" à ses OKRs. Utiliser le mode IA de **Tability** pour poser des questions sur l'état d'avancement des objectifs sans manipuler de filtres complexes.

## Le saviez-vous ?

L'IA peut générer des rétrospectives hebdomadaires sur vos objectifs de revenus en quelques secondes. Plus besoin de compiler manuellement vos dashboards.

## Sources

- [Tability IA - David Serrault](https://www.linkedin.com/posts/davidserrault_ia-activity-7404768876007428096-i97T)

---

## Description

> *Créez un assistant conversationnel pour suivre et piloter vos OKRs.*

"On en est où sur l'OKR 3 ?" → 15 min à chercher dans Notion. Ce challenge vous fait créer un assistant qui connaît vos OKRs, leur avancement, et peut répondre instantanément à toutes vos questions de suivi.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant connaissant les OKRs de l'équipe/projet
- [ ] Capacité à générer des check-ins automatiques
- [ ] Alertes sur les OKRs en danger

**Critères de réussite :**

- Questions en langage naturel fonctionnelles
- Check-ins générés en < 30 secondes
- Recommandations actionnables

---

## Pistes de Solution

### Structure OKRs à charger

```json
{
  "quarter": "Q1 2026",
  "objectives": [
    {
      "id": "O1",
      "title": "Accélérer l'adoption produit",
      "key_results": [
        {
          "id": "KR1.1",
          "title": "Atteindre 1000 utilisateurs actifs",
          "target": 1000,
          "current": 650,
          "unit": "users",
          "owner": "Marie",
          "confidence": 0.7
        }
      ]
    }
  ]
}
```

### Prompt système OKR Assistant

```
Tu es un assistant de pilotage OKRs. Tu connais nos objectifs et leur avancement.

Voici nos OKRs actuels :
[INSÉRER STRUCTURE OKRs]

Tu peux :
1. Répondre aux questions sur l'avancement
2. Générer des check-ins hebdomadaires
3. Identifier les OKRs en danger (confidence < 0.5)
4. Suggérer des actions correctives
5. Préparer des rétrospectives

Format tes réponses avec :
- 📊 pour les métriques
- 🚨 pour les alertes
- 💡 pour les recommandations
- ✅ pour les succès
```

### Exemples de questions

- "On en est où globalement ce trimestre ?"
- "Quels KRs sont en danger ?"
- "Génère le check-in de cette semaine"
- "Qu'est-ce qu'il faudrait faire pour sauver KR1.2 ?"
- "Compare notre avancement avec le trimestre dernier"

### Prompt de check-in automatique

```
Génère un check-in hebdomadaire pour nos OKRs.

Structure :
## 📊 État global
- Score global : X%
- Tendance : ↑↓→

## ✅ Victoires de la semaine
[KRs qui ont progressé significativement]

## 🚨 Points d'attention
[KRs en dessous de la trajectoire]

## 💡 Actions recommandées
[3 actions prioritaires pour la semaine prochaine]

## 🎯 Focus de la semaine
[L'OKR qui mérite toute notre attention]
```

### Intégration Notion/Airtable

Si les OKRs sont dans Notion :
```
1. Export JSON depuis Notion (API ou Zapier)
2. Injection dans le contexte de l'assistant
3. Mise à jour hebdomadaire automatique
```

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Structurer des OKRs pour une IA
- Créer un assistant de pilotage conversationnel
- Automatiser les check-ins

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-5 | Intro | Le problème du suivi OKR manuel |
| 5-15 | Démo | Assistant en action sur OKRs exemple |
| 15-25 | Setup | Chacun structure ses OKRs en JSON |
| 25-40 | Création | Configuration de l'assistant |
| 40-50 | Test | Questions et check-ins |
| 50-60 | Clôture | Automatisation et intégrations |

### Points d'attention animateur

- Avoir des OKRs exemple prêts
- Insister sur la qualité de la structure initiale
- Les confidence scores sont clés

---

## Ressources complémentaires

- [Tability](https://www.tability.io/)
- [Measure What Matters - John Doerr](https://www.whatmatters.com/)
