# L'Auditeur GRC Augmenté

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun (les référentiels seront expliqués) |

---

## Description

> *Créez un assistant d'audit de conformité qui analyse vos politiques de sécurité et identifie les écarts par rapport aux référentiels (ISO 27001, NIST, RGPD).*

"On est conformes ISO 27001 ?" Au lieu de lire 93 contrôles à la main, laissez l'IA faire le travail. Ce challenge vous fait créer un auditeur GRC qui analyse vos documents et produit un rapport d'écarts priorisé.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant capable d'analyser une politique de sécurité
- [ ] Rapport d'audit avec matrice de conformité
- [ ] Recommandations priorisées et actionnables

**Critères de réussite :**

- Les écarts sont identifiés avec le bon niveau de criticité
- Les recommandations sont concrètes (pas juste "améliorer")
- Le rapport est utilisable par un RSSI

---

## Pistes de Solution

### Référentiels couverts

| Référentiel | Périmètre | Contrôles |
|-------------|-----------|-----------|
| **ISO 27001** | SMSI | 93 contrôles |
| **NIST CSF** | Cybersécurité | 5 fonctions, 108 sous-catégories |
| **RGPD** | Données personnelles | 99 articles |

### Prompt système suggéré

```
Tu es un auditeur GRC senior avec 15 ans d'expérience.

## Tes référentiels
- ISO 27001:2022 (93 contrôles)
- NIST Cybersecurity Framework
- RGPD / GDPR

## Ton processus

### 1. Cadrage
- Quel référentiel ?
- Quel périmètre ?
- Certifications existantes ?

### 2. Analyse documentaire
Pour chaque contrôle :
- ✅ Couvert
- ⚠️ Partiel
- ❌ Manquant
- N/A Non applicable

### 3. Rapport
- Score global
- Matrice de conformité
- Écarts par criticité
- Recommandations priorisées

Commence par : "Pour démarrer l'audit :
1. Quel référentiel ciblez-vous ?
2. Quel périmètre ?
3. Avez-vous des documents à partager ?"
```

### Format du rapport

```markdown
# Rapport d'Audit GRC
## [Organisation] - [Périmètre]

### 1. Synthèse
**Score global :** XX/100
**Niveau :** [Initial/Géré/Défini/Maîtrisé/Optimisé]

### 2. Matrice de Conformité

| Domaine | Contrôles | ✅ | ⚠️ | ❌ |
|---------|-----------|-----|-----|-----|
| A.5 Politiques | 2 | 1 | 1 | 0 |
| A.6 Organisation | 5 | 2 | 2 | 1 |

### 3. Écarts Critiques

#### ❌ A.8.9 Configuration Management
**Exigence :** Configurations documentées et maintenues
**Constat :** Aucune politique identifiée
**Risque :** Vulnérabilités non détectées
**Recommandation :** Mettre en place une CMDB
**Effort :** M (1-3 mois)

### 4. Plan de Remédiation

| # | Écart | Criticité | Effort | Quick Win |
|---|-------|-----------|--------|-----------|
| 1 | Config Management | Critique | M | Non |
| 2 | Signature charte | Modéré | S | Oui |
```

### PSSI fictive pour l'exercice

```markdown
# Politique de Sécurité - ACME Corp v1.0

### 1. Objet
Règles de sécurité applicables aux SI d'ACME Corp.

### 2. Engagement Direction
La direction fournira les ressources nécessaires.

### 3. Classification
- Public, Interne, Confidentiel

### 4. Gestion des Accès
Principe du moindre privilège. Administrateurs valident.

### 5. Postes de Travail
Antivirus. Mises à jour automatiques.

### 6. Mots de Passe
Minimum 8 caractères. Changement 90 jours.

### 7. Télétravail
VPN obligatoire.
```

*(Lacunes volontaires : pas d'incidents, pas de sauvegarde, pas de formation...)*

### Tips & astuces

- Fournir le document en entier pour une analyse complète
- Toujours demander les preuves d'implémentation
- Les recommandations doivent être actionnables

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Comprendre la structure d'ISO 27001
- Analyser un document vs un référentiel
- Identifier et prioriser les écarts
- Rédiger des recommandations actionnables

### Prérequis participants

- Aucune connaissance GRC préalable
- Accès à un chat IA
- Intérêt pour la sécurité/conformité

### Matériel nécessaire

- [ ] Prompt système
- [ ] PSSI fictive (fournie)
- [ ] Extrait ISO 27001 (contrôles clés)
- [ ] Template de rapport

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-7 | Intro GRC | Présente ISO 27001, NIST, RGPD | Découvrent les référentiels | Contexte |
| 7-12 | Démo | Analyse un extrait de PSSI | Observent le processus | Voir en action |
| 12-17 | Setup | Distribue PSSI et prompt | Préparent leur assistant | Préparation |
| 17-35 | Audit | Circule, aide sur les référentiels | Auditent la PSSI | Production |
| 35-45 | Rapport | Montre le format attendu | Génèrent leur rapport | Formalisation |
| 45-55 | Partage | Fait présenter 2-3 écarts | Comparent leurs constats | Benchmark |
| 55-60 | Clôture | Comment adapter en vrai | Notent les next steps | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Perdus dans la complexité → Version simplifiée ISO
- Confusion référentiels → Clarifier les différences
- Recommandations vagues → Insister sur l'actionnable

**Questions fréquentes :**

- "Utilisable pour un vrai audit ?" → Aide à la préparation, pas de remplacement
- "Quel référentiel choisir ?" → Dépend du contexte (B2B=ISO, données=RGPD)
- "Comment obtenir ISO complet ?" → Norme payante, résumés gratuits

### Variantes

**Version simple (45 min) :**
- Focus RGPD uniquement
- PSSI 1 page

**Version avancée (2h) :**
- Multi-référentiels (ISO + RGPD)
- Document réel (anonymisé)
- Plan de remédiation chiffré

---

## Ressources complémentaires

- [ISO 27001:2022](https://www.iso.org/standard/27001)
- [NIST CSF](https://www.nist.gov/cyberframework)
- [CNIL RGPD](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on)
