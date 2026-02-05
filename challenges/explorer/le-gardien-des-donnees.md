# Le Gardien des Données

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 30 min |
| Durée Dojo | 1h |
| Difficulté | ⭐ |
| Prérequis | Aucun |

---

## Description

> *Maîtrisez les bonnes pratiques de confidentialité avec l'IA et créez votre charte personnelle pour protéger les données sensibles.*

"Je peux coller cet email client dans ChatGPT ?" — Cette question, tout le monde se la pose. Ce challenge vous fait valider votre compréhension des règles de confidentialité et créer une charte personnelle qui vous servira au quotidien.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Score ≥ 80% au quiz de confidentialité
- [ ] Charte personnelle complétée et signée
- [ ] 3 exemples d'anonymisation pratiques

**Critères de réussite :**

- Distinction claire entre données partageables et non partageables
- Réflexes de protection identifiés
- Charte applicable au quotidien

---

## Pistes de Solution

### Les règles d'or de la confidentialité IA

#### ❌ Ne JAMAIS partager :

| Type | Exemples |
|------|----------|
| Données personnelles | Noms, emails, téléphones, adresses |
| Données sensibles RGPD | Santé, opinions politiques, orientation |
| Secrets d'entreprise | Code propriétaire, stratégies, données financières |
| Credentials | Mots de passe, tokens API, clés SSH |
| Données clients | Sauf anonymisation complète |

#### ✅ Ce qu'on peut partager :

| Type | Condition |
|------|-----------|
| Données publiques | Infos disponibles sur internet |
| Données anonymisées | Impossible de remonter à l'individu |
| Données synthétiques | Fictives mais représentatives |
| Données personnelles | Avec consentement explicite |

### Techniques d'anonymisation

| Technique | Description | Exemple |
|-----------|-------------|---------|
| Pseudonymisation | Remplacer par identifiants | Jean Dupont → User_A42 |
| Généralisation | Réduire la précision | 28 ans → 25-30 ans |
| Suppression | Retirer les champs sensibles | Supprimer colonne email |
| Bruit | Ajouter des variations | Salaire ± 5% |

### Quiz type (extraits)

1. **Peut-on partager un email client pour rédiger une réponse ?**
   → ❌ Non, sauf à anonymiser nom et email

2. **Peut-on analyser du code open source avec l'IA ?**
   → ✅ Oui, c'est public

3. **Peut-on partager un extrait de contrat client ?**
   → ❌ Non, confidentiel

4. **Peut-on analyser des données de santé anonymisées ?**
   → ⚠️ Dépend du contexte et des garanties d'anonymisation

### Template de charte personnelle

```markdown
# Ma Charte IA

## Ce que je ne partage JAMAIS avec une IA publique :
- [ ] Noms et coordonnées de vrais clients
- [ ] Code source propriétaire
- [ ] Données RH (salaires, évaluations)
- [ ] Mots de passe et tokens
- [ ] [Ajouter selon votre contexte]

## Mes réflexes avant de copier-coller :
1. Est-ce que cette donnée est publique ?
2. Peut-elle identifier une personne ?
3. Est-elle couverte par un NDA ?
4. Mon client autoriserait-il ce partage ?

## Mes techniques d'anonymisation :
- Remplacer les noms par [CLIENT], [PERSONNE]
- Remplacer les emails par xxx@example.com
- Généraliser les chiffres sensibles

## En cas de doute :
- Je demande à mon manager
- Je ne partage pas

Signé : ________________
Date : ________________
```

### Tips & astuces

- L'objectif est de pouvoir utiliser l'IA, pas de l'interdire
- En cas de doute → anonymiser ou ne pas partager
- Créer des templates d'anonymisation pour gagner du temps

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les données qu'on peut/ne peut pas partager
- Appliquer les techniques d'anonymisation de base
- Avoir des réflexes de protection systématiques

### Prérequis participants

- Aucun prérequis technique
- Accès à un chat IA

### Matériel nécessaire

- [ ] Quiz interactif (20 questions)
- [ ] Template de charte personnelle
- [ ] Exemples d'anonymisation
- [ ] Cas pratiques (emails, données)

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro RGPD | Contexte légal et exemples de fuites | Comprennent les risques | Sensibilisation |
| 10-25 | Quiz interactif | "Je partage ou pas ?" (15 cas) | Votent, découvrent les pièges | Validation des acquis |
| 25-40 | Atelier anonymisation | Donne un email et un dataset | Anonymisent en pratique | Mise en pratique |
| 40-50 | Création charte | Guide la rédaction | Rédigent leur charte personnelle | Engagement |
| 50-60 | Partage | Tour de table, signature symbolique | Partagent leurs ajouts perso | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- Ton moralisateur → Être pratique, pas punitif
- Trop de règles → Focus sur les 5 règles d'or
- Oublier le contexte → Adapter aux métiers présents

**Questions fréquentes :**

- "Et si j'utilise une IA d'entreprise ?" → Les règles peuvent être différentes (vérifier la policy)
- "Le RGPD s'applique aux USA ?" → Oui si données de résidents EU
- "Quid des données anciennes ?" → Mêmes règles

**Tips d'animation :**

- Montrer des cas réels de fuites (anonymisés)
- Faire le "jeu du doute" : si hésitation → pas de partage
- Donner des extensions/outils d'anonymisation

### Variantes

**Version courte (30 min) :**
- Quiz uniquement (pas d'atelier anonymisation)
- Charte pré-remplie à compléter

**Version avancée (1h30) :**
- Cas complexes par métier (RH, Finance, Dev)
- Création d'un guide équipe
- Simulation d'audit RGPD

---

## Ressources complémentaires

- [CNIL - Guide RGPD](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on)
- [ANSSI - Recommandations IA](https://www.ssi.gouv.fr/)
