# Brand Voice Designer

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun |

---

## Description

> *Créez un assistant qui audite votre ton de marque, définit vos guidelines et produit des textes cohérents avec votre identité.*

"On est accessible mais experts", "Chaleureux mais pas familiers"... Les guidelines brand voice sont souvent vagues. Cet assistant analyse vos contenus existants, benchmark vos concurrents, et produit un document de référence actionnable avec exemples concrets et do's/don'ts.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Audit du tone of voice d'une marque (existante ou fictive)
- [ ] Guidelines documentées avec do's/don'ts
- [ ] 5 exemples de contenus conformes aux guidelines

**Critères de réussite :**

- Les 4 dimensions de voix sont positionnées (formalité, émotion, humour, assertivité)
- Les guidelines sont applicables (pas juste "soyez sympas")
- Les exemples avant/après montrent une vraie différence

---

## Pistes de Solution

### Approche recommandée

L'assistant structure son travail en 4 étapes :
1. Audit de l'existant
2. Benchmark concurrentiel
3. Définition des guidelines
4. Production d'exemples

### Prompt système suggéré

```
Tu es un expert en Brand Voice et Content Design avec 10 ans d'expérience en agence et chez des marques tech.

## Ta mission
Aider les équipes à définir, documenter et appliquer une voix de marque cohérente.

## Cadre d'analyse de la voix

### Les 4 dimensions
1. **Formalité** : Formel ↔ Décontracté
2. **Émotion** : Rationnel ↔ Émotionnel
3. **Humour** : Sérieux ↔ Léger
4. **Assertivité** : Humble ↔ Affirmé

### Traits de personnalité
Exemples : Expert, Accessible, Audacieux, Chaleureux, Innovant, Fiable, Provocateur, Rassurant...

## Format des guidelines

# Brand Voice Guidelines - [Marque]

## Notre personnalité
Nous sommes [trait 1], [trait 2], [trait 3].
Nous ne sommes pas [anti-trait 1], [anti-trait 2].

## Notre ton selon le contexte

| Contexte | Ton | Exemple |
|----------|-----|---------|
| Réseaux sociaux | Décontracté, proche | "On vous présente..." |
| Emails transactionnels | Clair, efficace | "Votre commande est confirmée." |
| Support | Empathique, solution | "On comprend, voici comment..." |
| Site web | Expert, accessible | "Notre technologie vous permet de..." |

## Do's ✅
- Utiliser "vous" (proximité)
- Phrases courtes (clarté)
- Exemples concrets (pédagogie)

## Don'ts ❌
- Jargon technique non expliqué
- Ton condescendant
- Humour forcé

## Vocabulaire signature
- Préférer "solution" à "produit"
- Préférer "accompagner" à "vendre"
- Mots interdits : "révolutionnaire", "unique"

## Exemples avant/après

### Avant (générique)
"Notre solution innovante vous permet d'optimiser vos process."

### Après (brand voice)
"Gagnez 2h par jour sur vos tâches répétitives. On vous montre comment."

---

Commence par : "Quelle marque veux-tu travailler ? Partage-moi quelques exemples de contenus existants (site, réseaux, emails)."
```

### Exemple de livrable

**Guidelines générées pour une fintech :**

```markdown
# Brand Voice Guidelines - PayFlow

## Notre personnalité
Nous sommes **experts, accessibles et directs**.
Nous ne sommes pas condescendants, jargonneux ou froids.

## Notre ton selon le contexte

| Contexte | Ton | Exemple |
|----------|-----|---------|
| App | Clair, encourageant | "Bravo, premier virement envoyé !" |
| Support | Patient, solution | "Pas de souci, on règle ça ensemble." |
| LinkedIn | Expert, humain | "Ce que personne ne vous dit sur les virements SEPA..." |

## Do's ✅
- Tutoyer dans l'app, vouvoyer ailleurs
- Expliquer les termes bancaires en langage courant
- Célébrer les petites victoires utilisateur

## Don'ts ❌
- "Veuillez patienter" (dire plutôt "Encore 2 secondes...")
- Acronymes bancaires sans explication
- Messages d'erreur culpabilisants
```

### Tips & astuces

- Collecter des exemples réels de tous les touchpoints (site, emails, réseaux, support)
- Faire l'exercice "Si notre marque était une personne, ce serait..."
- Tester les guidelines sur des cas limites (message d'erreur, réclamation client)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Analyser le tone of voice d'une marque
- Positionner une marque sur les 4 dimensions de voix
- Rédiger des guidelines actionnables
- Appliquer les guidelines sur différents formats

### Prérequis participants

- Accès à un chat IA
- Idéalement : exemples de contenus d'une marque à travailler
- Sinon : utiliser une marque connue

### Matériel nécessaire

- [ ] Prompt système
- [ ] Grille des 4 dimensions (à remplir)
- [ ] Exemples de brand voices connues (Apple, Innocent, BlaBlaCar...)
- [ ] Textes à réécrire (exercice avant/après)

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Montre des exemples de brand voices distinctives | Devinent les marques | Sensibilisation |
| 10-20 | Audit | Guide l'analyse de 2-3 contenus d'une marque | Analysent, remplissent la grille | Diagnostic |
| 20-35 | Guidelines | Circule pendant la génération | Créent les guidelines avec l'assistant | Production |
| 35-50 | Application | Distribue des textes à réécrire | Réécrivent selon leurs guidelines | Mise en pratique |
| 50-60 | Partage | Fait comparer les avant/après | Présentent leurs réécritures | Validation |

### Points d'attention animateur

**Pièges courants :**

- Guidelines trop vagues ("soyez sympas") → Exiger des exemples concrets
- Confusion ton/contenu → Le ton c'est le "comment", pas le "quoi"
- Oublier les cas difficiles → Tester sur message d'erreur, refus, réclamation

**Questions fréquentes :**

- "On peut avoir plusieurs tons ?" → Oui, adapter selon le contexte (support ≠ pub)
- "Comment choisir entre tu et vous ?" → Dépend de la cible et du touchpoint
- "Ça marche pour le B2B ?" → Oui, le B2B aussi a besoin de personnalité

**Tips d'animation :**

- Faire deviner des marques à partir de leur ton (blind test)
- Comparer 2 concurrents sur le même message
- Faire voter pour le meilleur avant/après

### Variantes

**Version courte (30 min) :**
- Utiliser une marque connue (pas d'audit)
- Focus sur l'exercice avant/après uniquement

**Version longue (2h) :**
- Audit complet multi-touchpoints
- Benchmark de 3 concurrents
- Production d'un mini-playbook

---

## Ressources complémentaires

- [Voice and Tone (Mailchimp)](https://styleguide.mailchimp.com/voice-and-tone/)
- Livre : "Microcopy: The Complete Guide" (Kinneret Yifrah)
