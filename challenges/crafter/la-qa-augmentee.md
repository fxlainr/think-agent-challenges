# La QA Augmentée

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | SHIELD |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 230 |
| Prérequis | Notions de base en test logiciel |

---

## Vision & Impact

Faire tourner des tests d'utilisabilité de manière autonome via des agents qui naviguent sur le prototype pour identifier les frictions. L'IA permet de gagner **18 minutes par test de recette globale**.

## Le saviez-vous ?

Le logiciel cesse d'être un outil manipulé pour devenir un système que l'on dirige par l'intention pure. L'IA n'est pas magique ; elle doit être utilisée pour résoudre de réelles difficultés de production.

## Sources

- [L'IA m'a fait gagner 18 min par test QA - Marion Jachimski](https://www.linkedin.com/posts/marion-jachimski-7010996b_lia-ma-fait-gagner-18-min-par-test-qa-activity-7417822957655236608-Cpwn)

---

## Description

> *Générez automatiquement des plans de tests exhaustifs à partir de vos spécifications — plus d'edge cases oubliés.*

Rédiger des cas de test prend du temps, et on oublie toujours des edge cases. Cet assistant analyse une spec produit et génère un plan de test complet : cas nominaux, cas d'erreur, valeurs limites, tests de régression. Format prêt à être utilisé par l'équipe QA.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un assistant fonctionnel qui génère des plans de test
- [ ] Plan de test généré à partir d'une spec réelle
- [ ] Couverture des edge cases et cas d'erreur

**Critères de réussite :**

- Matrice de couverture complète (requirements → tests)
- Cas de test précis et reproductibles
- Edge cases identifiés systématiquement

---

## Pistes de Solution

### Approche recommandée

L'assistant applique 4 techniques de test :
1. **Equivalence Partitioning** — Regrouper les entrées similaires
2. **Boundary Value Analysis** — Tester les limites
3. **Decision Table** — Combinaisons de conditions
4. **State Transition** — Changements d'état

### Prompt système suggéré

```
Tu es un QA Engineer senior avec 10 ans d'expérience. Tu excelles dans la création de plans de tests exhaustifs qui capturent les cas nominaux ET les edge cases.

## Ta mission
Analyser une spécification produit (PRD, user story, feature spec) et générer un plan de test complet.

## Structure du plan de test

### 1. Résumé du périmètre
- Feature testée, version, environnement, prérequis

### 2. Matrice de couverture
Mapping entre requirements et cas de test.

### 3. Cas de test détaillés

Pour chaque cas :
**ID** : TC-XXX
**Titre** : [Action] [Objet] [Condition]
**Priorité** : Critique / Haute / Moyenne / Basse
**Type** : Fonctionnel / Régression / Performance / Sécurité

**Préconditions :**
- Condition 1, Condition 2

**Étapes :**
1. Action précise
2. Action précise

**Résultat attendu :**
- Ce qu'on doit observer

**Données de test :**
- Données nécessaires

### 4. Cas aux limites (Edge Cases)
- Valeurs limites (min, max, zéro, négatif)
- Entrées invalides
- Timeouts et erreurs réseau
- Permissions et droits d'accès

### 5. Tests de régression
- Fonctionnalités impactées
- Intégrations à vérifier

## Priorisation
- P0 : Bloquant si KO (critique business)
- P1 : Important mais contournable
- P2 : Confort utilisateur

Commence par : "Envoie-moi la spec ou les user stories à couvrir."
```

### Exemple de livrable

**User Story source :**
```
En tant qu'utilisateur connecté
Je veux réinitialiser mon mot de passe
Afin de récupérer l'accès à mon compte

Critères : Email envoyé, lien valide 24h, règles de sécurité MDP, confirmation
```

**Plan de test généré (extraits) :**

```markdown
## TC-001 : Demande reset avec email valide
**Priorité** : Critique | **Type** : Fonctionnel

**Préconditions :** Utilisateur avec compte actif

**Étapes :**
1. Aller sur "Mot de passe oublié"
2. Saisir email valide
3. Cliquer "Envoyer"

**Résultat attendu :**
- Message "Email envoyé" affiché
- Email reçu dans les 2 minutes
- Lien de reset valide

---

## TC-005 : Lien expiré (>24h)
**Priorité** : Haute | **Type** : Fonctionnel

**Préconditions :** Lien généré il y a 25h

**Résultat attendu :**
- Message "Lien expiré"
- Redirection vers page de demande

---

## TC-007 : MDP trop court
**Priorité** : Critique | **Type** : Sécurité

**Données :** Nouveau MDP = "abc" (3 car.)

**Résultat attendu :**
- Erreur "Minimum 8 caractères"
- MDP non modifié
```

### Tips & astuces

- Toujours demander "qu'est-ce qui peut mal tourner ?"
- Penser aux cas de sécurité (injection, permissions)
- Préciser les données de test pour la reproductibilité

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Analyser une spec pour identifier les cas de test
- Appliquer les techniques de test (boundary, equivalence...)
- Rédiger des cas de test précis et reproductibles
- Identifier les edge cases souvent oubliés

### Prérequis participants

- Accès à un chat IA
- Une spec/user story à tester (ou utiliser l'exemple fourni)
- Notions de base en test (pas obligatoire)

### Matériel nécessaire

- [ ] Prompt système
- [ ] 2-3 specs exemple de difficulté croissante
- [ ] Checklist des edge cases classiques
- [ ] Template de cas de test

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente l'importance d'une bonne couverture | Contexte | Motivation |
| 5-10 | Techniques | Explique les 4 techniques de test | Comprennent les concepts | Théorie |
| 10-15 | Démo | Génère un plan de test sur l'exemple | Observent le résultat | Voir le livrable |
| 15-20 | Setup | Distribue le prompt et les specs | Choisissent leur spec | Préparation |
| 20-40 | Génération | Circule, aide à identifier les edge cases | Génèrent leur plan de test | Production |
| 40-50 | Challenge croisé | Forme des binômes | Cherchent les cas manqués dans le plan du binôme | Revue critique |
| 50-55 | Synthèse | Collecte les edge cases les plus créatifs | Partagent leurs découvertes | Apprentissage |
| 55-60 | Clôture | Tips pour intégrer dans le workflow | Notent les next steps | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Plans trop vagues → Insister sur les étapes précises
- Oubli des cas d'erreur → "Qu'est-ce qui peut mal tourner ?"
- Tests non reproductibles → Préciser les données de test

**Questions fréquentes :**

- "Combien de tests c'est assez ?" → Dépend du risque, viser 80% des cas critiques
- "On teste tout manuellement ?" → Prioriser, automatiser le répétitif
- "Et les tests de perf ?" → Mentionner, mais focus fonctionnel ici

**Tips d'animation :**

- Faire le jeu "trouve le bug" : donner une spec avec un trou
- Montrer des exemples de bugs réels évitables
- Faire voter pour le meilleur edge case trouvé

### Variantes

**Version courte (45 min) :**
- Spec simple fournie
- Focus sur happy path + 3-4 edge cases

**Version longue (1h30) :**
- Spec complexe avec multiples parcours
- Génération de scripts de test automatisés (Playwright, Cypress)

**Duo Dev + QA :**
- Dev fournit la spec
- QA génère le plan avec l'IA
- Discussion sur la testabilité

---

## Ressources complémentaires

- [ISTQB Foundation Level](https://www.istqb.org/)
- Techniques de test (Boundary, Equivalence, Decision Table)
