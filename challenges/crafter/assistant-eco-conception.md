# L'Assistant Éco-Conception

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun (les concepts ACV seront expliqués) |

---

## Description

> *Créez un assistant d'éco-conception qui analyse le cycle de vie de vos produits, identifie les hotspots carbone et propose des alternatives durables.*

"C'est quoi le plus polluant : le transport ou la fabrication ?" Ce challenge vous donne les outils pour répondre. Analysez n'importe quel produit, estimez son empreinte carbone et identifiez les vrais leviers d'amélioration.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Analyse de cycle de vie d'un produit
- [ ] Estimation chiffrée de l'empreinte carbone
- [ ] Recommandations d'alternatives durables

**Critères de réussite :**

- Les 5 phases du cycle de vie sont couvertes
- Les hotspots sont identifiés et quantifiés
- Les alternatives sont concrètes et priorisées

---

## Pistes de Solution

### Les 5 phases du cycle de vie

1. **Extraction** des matières premières
2. **Fabrication** / Production
3. **Distribution** / Transport
4. **Utilisation**
5. **Fin de vie** (recyclage, déchet)

### Facteurs d'émission (ordres de grandeur)

**Matériaux (kg CO2eq/kg) :**
| Matériau | Vierge | Recyclé |
|----------|--------|---------|
| Acier | 2.0-2.5 | 0.5-1.0 |
| Aluminium | 8.0-12.0 | 0.5-1.5 |
| Plastique | 2.0-3.0 | 0.5-1.5 |
| Coton | 5.0-8.0 | - |

**Transport (kg CO2eq/tonne.km) :**
| Mode | Facteur |
|------|---------|
| Maritime | 0.01-0.02 |
| Ferroviaire | 0.02-0.05 |
| Routier | 0.10-0.15 |
| Aérien | 0.50-1.50 |

### Prompt système suggéré

```
Tu es un expert en éco-conception et ACV avec 12 ans d'expérience.

## Ton processus

### 1. Comprendre le produit
- Fonction, matériaux, poids
- Lieu de fabrication
- Durée de vie, fin de vie

### 2. Cartographier les impacts
Pour chaque phase : flux entrants/sortants, émissions

### 3. Identifier les hotspots
Où se concentrent les impacts ? (souvent : matériaux, transport, énergie)

### 4. Proposer des alternatives
- Matériaux alternatifs
- Optimisation process
- Économie circulaire

### 5. Chiffrer
Estimer les gains potentiels de chaque alternative.

Commence par : "Décris-moi le produit : fonction, matériaux, poids, lieu de fabrication..."
```

### Format de rapport

```markdown
# Rapport Éco-Conception - [Produit]

## Fiche produit
| Attribut | Valeur |
|----------|--------|
| Fonction | ... |
| Poids | X kg |
| Matériaux | ... |
| Fabrication | Pays |
| Durée de vie | X ans |

## Bilan carbone

| Phase | kg CO2eq | % |
|-------|----------|---|
| Matières premières | X | X% |
| Fabrication | X | X% |
| Transport | X | X% |
| Utilisation | X | X% |
| Fin de vie | X | X% |
| **TOTAL** | **X** | 100% |

## Hotspots
🔴 [Phase/Matériau] : X kg CO2eq (X%)
→ Levier : [Alternative]

## Alternatives recommandées

| Actuel | Alternative | Gain | Faisabilité |
|--------|-------------|------|-------------|
| ... | ... | -X% | ⭐⭐⭐ |
```

### Tips & astuces

- Accepter les ordres de grandeur quand les données manquent
- Alerter sur les fausses bonnes idées (bioplastique ≠ toujours mieux)
- Toujours comparer à un usage de référence

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Comprendre les 5 phases du cycle de vie
- Identifier les hotspots d'un produit
- Estimer un bilan carbone simplifié
- Proposer des alternatives d'éco-conception

### Prérequis participants

- Avoir un produit en tête à analyser
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Tableau des facteurs d'émission
- [ ] Produits exemples (bouteille, t-shirt, smartphone)
- [ ] Template de rapport

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-7 | Intro ACV | Présente les 5 phases | Comprennent le concept | Théorie |
| 7-12 | Facteurs | Explique les ordres de grandeur | Découvrent les chiffres | Référentiel |
| 12-18 | Démo | Analyse une bouteille inox | Observent le processus | Voir en action |
| 18-23 | Choix | Aide à choisir un produit | Sélectionnent leur produit | Préparation |
| 23-43 | Analyse | Circule, aide sur les estimations | Analysent leur produit | Production |
| 43-53 | Partage | Fait présenter 3 analyses | Présentent leurs hotspots | Benchmark |
| 53-60 | Clôture | Récapitule les leviers | Notent les actions | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- Données trop précises → Accepter les estimations
- Oublier la phase d'usage → "Et pendant 10 ans ?"
- Fausses bonnes idées → "Le bio n'est pas toujours mieux"

**Questions fréquentes :**

- "C'est vraiment précis ?" → L'objectif est d'identifier les leviers
- "Comment avoir les vraies données ?" → Base Carbone ADEME
- "Et le numérique ?" → GreenIT.fr pour les données

### Variantes

**Version simple (45 min) :**
- Produit fourni (t-shirt)
- Focus CO2 uniquement

**Version avancée (2h) :**
- Produit complexe
- Multi-indicateurs (eau, ressources)
- Comparaison de scénarios

---

## Ressources complémentaires

- [Base Carbone ADEME](https://base-empreinte.ademe.fr/)
- [ISO 14040](https://www.iso.org/standard/37456.html)
