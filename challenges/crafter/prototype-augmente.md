# Prototype Augmenté

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Figma (ou outil de prototypage), accès IA |

---

## Description

> *Enrichissez vos prototypes Figma avec du contenu réaliste généré par IA pour des tests utilisateurs plus immersifs.*

"Lorem ipsum dolor sit amet"... Vos testeurs passent plus de temps à deviner ce que représentent les faux textes qu'à évaluer l'UX. Ce challenge vous apprend à générer du contenu réaliste et personnalisé pour vos prototypes — noms, descriptions, données, edge cases.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un prototype enrichi avec du contenu réaliste (exit lorem ipsum)
- [ ] Un jeu de données cohérent (utilisateurs, produits, notifications...)
- [ ] Une variante "edge case" pour tester les limites

**Critères de réussite :**

- Le contenu est crédible et cohérent
- Les edge cases sont couverts (noms longs, nombres élevés...)
- Le workflow est réutilisable pour d'autres projets

---

## Pistes de Solution

### Cas d'usage

1. **Lorem ipsum → Contenu réaliste** — Textes crédibles
2. **Données de démo** — Jeux de données pour dashboards
3. **Personnalisation** — Adapter au profil du testeur
4. **Edge cases** — Tester les limites (noms longs, valeurs extrêmes)

### Méthode 1 : Génération par batch

```
Génère du contenu réaliste pour un prototype d'application [type].

## Besoins :
- 10 noms de produits avec descriptions (50 mots max)
- 5 profils utilisateurs avec nom, email, rôle
- 15 notifications types (succès, erreur, info)
- 8 éléments de menu avec icônes suggérées

## Format : JSON structuré
```

**Sortie :**
```json
{
  "products": [
    {
      "name": "AirPods Pro Max",
      "description": "Casque audio premium avec réduction de bruit active",
      "price": "549€",
      "category": "Audio"
    }
  ],
  "users": [
    {
      "name": "Marie Dubois",
      "email": "m.dubois@example.com",
      "role": "Product Manager",
      "avatar": "initials:MD"
    }
  ],
  "notifications": [
    {"type": "success", "message": "Votre commande a été confirmée"},
    {"type": "error", "message": "Échec du paiement - Vérifiez votre carte"}
  ]
}
```

### Méthode 2 : Plugins Figma + IA

| Plugin | Fonction |
|--------|----------|
| **Content Reel** | Génère du contenu contextuel |
| **Magician** | Génération IA intégrée |
| **JSON to Variables** | Import de données structurées |

### Méthode 3 : Variables Figma

1. Créer des **modes** dans Figma Variables :
   - Mode "Demo" — contenu générique
   - Mode "Test User A" — personnalisé pour un persona
   - Mode "Edge Case" — cas limites

2. Switcher entre les modes en un clic pour tester différents scénarios

### Exemple : Dashboard financier

**Avant (lorem ipsum) :**
- "Lorem ipsum dolor..."
- Graphique avec données aléatoires
- KPIs sans sens

**Après (contenu généré) :**
```json
{
  "kpis": [
    {"label": "Chiffre d'affaires", "value": "2.4M€", "trend": "+12%"},
    {"label": "Marge brute", "value": "42%", "trend": "-2pts"},
    {"label": "Clients actifs", "value": "1,847", "trend": "+156"}
  ],
  "alerts": [
    "Objectif Q2 atteint avec 3 semaines d'avance",
    "3 clients grands comptes en négociation"
  ]
}
```

### Edge cases à générer

| Type | Exemple | Pourquoi tester |
|------|---------|-----------------|
| Nom très long | "Jean-Baptiste de La Fontaine-Montmorency" | Overflow texte |
| Nombre élevé | "1,234,567€" | Formatage |
| Liste vide | 0 notifications | État vide |
| Texte multilingue | "Müller, 日本語" | Encodage |
| Valeur négative | "-15%" | Affichage rouge/vert |

### Tips & astuces

- Générer le contenu en JSON pour réutilisation facile
- Créer un "kit de contenu" par type de projet (e-commerce, SaaS, fintech...)
- Penser aux edge cases dès la génération

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Générer du contenu réaliste pour leurs prototypes
- Utiliser les variables Figma pour switcher entre contextes
- Identifier et tester les edge cases UX
- Gagner du temps sur la préparation des tests utilisateurs

### Prérequis participants

- Fichier Figma avec textes à remplacer
- Accès à un chat IA
- Optionnel : plugins Figma (Magician, Content Reel)

### Matériel nécessaire

- [ ] Prototype Figma exemple (avec lorem ipsum)
- [ ] Template de prompt de génération
- [ ] Liste des edge cases courants
- [ ] Guide d'import JSON → Figma

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Pourquoi le contenu compte pour les tests UX | Découvrent l'impact | Motivation |
| 10-20 | Génération | Génère un jeu de données pour le prototype exemple | Observent le process | Voir le résultat |
| 20-35 | Application | Montre comment intégrer dans Figma | Enrichissent leur prototype | Production |
| 35-50 | Edge cases | Crée une variante "cas limites" | Créent leur variante edge case | Robustesse |
| 50-60 | Partage | Fait comparer avant/après | Présentent leurs prototypes | Validation |

### Points d'attention animateur

**Pièges courants :**

- Contenu incohérent → Générer par batch avec contexte
- Oubli des edge cases → Checklist obligatoire
- Trop de variantes → 2-3 modes suffisent

**Questions fréquentes :**

- "Ça marche avec Sketch/Adobe XD ?" → Oui, le JSON est universel
- "Comment personnaliser pour chaque testeur ?" → Variables avec modes
- "C'est pas du plagiat de marques ?" → Générer des noms fictifs

**Tips d'animation :**

- Avoir un prototype "avant" bien moche (lorem ipsum partout)
- Montrer l'impact sur un vrai test utilisateur
- Partager un "starter kit" de contenu par secteur

### Variantes

**Version découverte (30 min) :**
- Juste la génération de contenu
- Copier-coller dans Figma
- Pas de variables ni edge cases

**Version avancée (2h) :**
- Workflow complet avec variables Figma
- Génération conditionnelle (persona A vs B)
- Intégration avec Airtable/Notion pour centraliser

---

## Ressources complémentaires

- [Figma Variables](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma)
- [Content Reel plugin](https://www.figma.com/community/plugin/731627216655469013)
- [Magician plugin](https://magician.design/)
