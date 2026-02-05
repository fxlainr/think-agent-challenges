# Le Phishing Simulator

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun |

---

## Description

> *Créez des campagnes de sensibilisation au phishing : emails de test réalistes + supports de formation pour vos collaborateurs.*

91% des cyberattaques commencent par un email de phishing. Vos équipes sauraient-elles le repérer ? Cet assistant génère des campagnes de phishing éducatives : emails réalistes avec différents niveaux de difficulté, grille de scoring et module de formation post-clic.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 5 emails de phishing test (du facile au difficile)
- [ ] Grille de scoring pour évaluer les résultats
- [ ] Module de sensibilisation post-clic

**Critères de réussite :**

- Les emails sont réalistes mais éthiques (pas de vrais liens malveillants)
- Chaque email a 3-5 indices identifiables (red flags)
- Le module de formation est pédagogique (pas culpabilisant)

---

## Pistes de Solution

### Types de phishing à simuler

| Type | Objectif | Exemple |
|------|----------|---------|
| Credential Harvesting | Récupérer identifiants | Faux portail Microsoft 365 |
| Business Email Compromise | Usurper un dirigeant | Demande de virement urgent |
| Spear Phishing | Cibler une personne | Référence à un projet réel |
| Generic | Masse | Colis en attente, alerte bancaire |

### Prompt système suggéré

```
Tu es un expert en sensibilisation cybersécurité spécialisé dans les campagnes de phishing éducatives.

## Ta mission
Créer des emails de phishing réalistes mais éthiques pour des campagnes de sensibilisation.

## Structure d'un email de phishing

### Métadonnées
- **Difficulté** : ⭐ / ⭐⭐ / ⭐⭐⭐
- **Type** : Credential / BEC / Spear / Generic
- **Prétexte** : [Scénario utilisé]

### Contenu
- **De** : [Adresse avec anomalie subtile]
- **Objet** : [Accroche créant l'urgence]
- **Corps** : [Message avec appel à l'action]
- **Lien** : [URL suspecte mais plausible]

### Indices à repérer (3-5)
- Red flag 1
- Red flag 2
- ...

### Point de formation associé
[Ce que le collaborateur doit retenir]

## Consignes éthiques
1. Pas de vrais liens malveillants
2. Objectif éducatif, pas piège
3. Pas de honte publique
4. Feedback immédiat si clic

Commence par : "Pour créer votre campagne, dites-moi le nombre d'emails, le niveau de difficulté et le contexte (nom d'entreprise, outils utilisés)."
```

### Exemple d'email généré

```markdown
## Email #1 : Reset mot de passe (Facile)

**Difficulté :** ⭐
**Type :** Credential Harvesting

### 📧 Email

**De :** Microsoft Security <security@microsft-account.com>
**Objet :** 🔒 Action requise : Votre mot de passe expire dans 24h

---

Bonjour,

Votre mot de passe Microsoft 365 expire dans les prochaines 24 heures.
Pour éviter toute interruption, mettez-le à jour immédiatement.

[Mettre à jour mon mot de passe]
https://login.microsft-secure.com/reset

Cordialement,
L'équipe Microsoft Security

---

### 🚩 Indices à repérer
1. "microsft" au lieu de "microsoft" (faute dans l'adresse)
2. Domaine du lien : "microsft-secure.com" (faux domaine)
3. Urgence artificielle : "24 heures"
4. Menace de perte d'accès
5. Pas de personnalisation (pas de nom)

### 📚 Formation
"Toujours vérifier l'adresse de l'expéditeur ET le domaine du lien avant de cliquer."
```

### Grille de scoring

| Score | Interprétation | Action |
|-------|----------------|--------|
| 0 clic / 5 | 🏆 Expert | Félicitations |
| 1 clic | ✅ Bon niveau | Rappel des bonnes pratiques |
| 2-3 clics | ⚠️ Sensibilisation recommandée | Module e-learning |
| 4-5 clics | 🚨 Formation obligatoire | Session présentielle |

### Module post-clic

```html
<h1>⚠️ Ceci était un test de sensibilisation</h1>

<p>Vous avez cliqué sur un lien de phishing simulé.
Pas d'inquiétude, c'est l'occasion d'apprendre !</p>

<h2>Ce qui aurait dû vous alerter :</h2>
<ul>
  <li>L'adresse de l'expéditeur</li>
  <li>L'urgence du message</li>
  <li>Le lien qui ne pointe pas vers notre domaine officiel</li>
</ul>

<h2>Les bons réflexes :</h2>
<ol>
  <li>Vérifiez TOUJOURS l'adresse de l'expéditeur</li>
  <li>Survolez les liens AVANT de cliquer</li>
  <li>En cas de doute, contactez l'IT</li>
</ol>
```

### Tips & astuces

- Mélanger les niveaux de difficulté dans une même campagne
- Personnaliser avec le contexte réel (nom d'entreprise, outils utilisés)
- Prévenir qu'une campagne aura lieu (sans dire quand)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Reconnaître les techniques de phishing courantes
- Créer des emails de test réalistes
- Identifier les indices de phishing (red flags)
- Construire un module de sensibilisation efficace

### Prérequis participants

- Aucune compétence technique requise
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Exemples de vrais phishing (anonymisés)
- [ ] Checklist des red flags
- [ ] Template de page post-clic

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente les stats phishing (91% des attaques) | Prennent conscience | Contexte |
| 5-10 | Quiz | Montre 3 emails (vrai ou phishing ?) | Votent, découvrent les indices | Mise en situation |
| 10-15 | Démo | Génère 1 email avec l'assistant | Observent | Voir le résultat |
| 15-20 | Setup | Distribue le prompt et contexte | Définissent leur contexte entreprise | Préparation |
| 20-35 | Création | Circule, aide sur les scénarios | Créent 3 emails de phishing | Production |
| 35-45 | Test croisé | Forme des binômes | Testent les emails du binôme | Challenge |
| 45-55 | Formation | Montre le template post-clic | Rédigent leur page de sensibilisation | Pédagogie |
| 55-60 | Clôture | Récapitule les bonnes pratiques | Notent les actions | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Emails trop évidents → Pousser vers plus de réalisme
- Oubli des indices → Chaque email doit avoir 3-5 red flags identifiés
- Éthique floue → Insister sur le caractère éducatif

**Questions fréquentes :**

- "C'est légal ?" → Oui si interne, avec accord DG/RH, sans harcèlement
- "Que faire des résultats ?" → Formation, pas de sanction
- "Peut-on utiliser les vrais noms ?" → Oui pour les scénarios BEC (DG, RH)

**Tips d'animation :**

- Montrer des exemples de phishing réels
- Faire un concours du phishing le plus réaliste
- Discuter des limites éthiques

### Variantes

**Version découverte (45 min) :**
- Analyser des phishing existants (pas en créer)
- Focus sur les indices à repérer
- Quiz interactif

**Version avancée (2h) :**
- Campagne complète (5 emails + planning + métriques)
- Intégration avec un outil (Gophish, KnowBe4)
- Simulation de BEC réaliste

---

## Ressources complémentaires

- [Gophish](https://getgophish.com/) — outil open source de simulation
- [ANSSI - Guide phishing](https://www.ssi.gouv.fr/)
