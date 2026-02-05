# Vibe Coding Sécurisé

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Notions de développement web |

---

## Description

> *Prototypez une application en "vibe coding" (génération par prompts) avec un audit de sécurité intégré — vitesse ET sécurité.*

Le "vibe coding" c'est magique : décrivez ce que vous voulez, l'IA génère le code. Mais c'est aussi risqué : injections SQL, tokens en dur, CORS ouverts... Ce challenge vous apprend à prototyper vite SANS sacrifier la sécurité.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Prototype fonctionnel créé en vibe coding
- [ ] Audit sécurité passé (checklist complète)
- [ ] Corrections documentées

**Critères de réussite :**

- Aucune vulnérabilité critique ou haute
- Les credentials ne sont pas dans le code
- Les inputs sont validés côté serveur

---

## Pistes de Solution

### Outils de vibe coding

| Outil | Type | Sécurité |
|-------|------|----------|
| **Cursor** | IDE IA | ⭐⭐⭐⭐ Code visible |
| **Replit Agent** | Cloud IDE | ⭐⭐⭐ |
| **Bolt.new** | Web builder | ⭐⭐ Boîte noire |
| **v0.dev** | UI generator | ⭐⭐⭐ |

### Checklist sécurité obligatoire

#### 1. Authentification
- [ ] Pas de credentials en dur dans le code
- [ ] Tokens/sessions sécurisés
- [ ] Rate limiting sur auth
- [ ] Validation des entrées

#### 2. Données
- [ ] Pas de données sensibles dans le frontend
- [ ] HTTPS obligatoire
- [ ] Validation côté serveur
- [ ] Sanitisation des inputs

#### 3. APIs
- [ ] Auth sur chaque endpoint
- [ ] CORS correctement configuré
- [ ] Pas de secrets dans les URLs

#### 4. Dépendances
- [ ] Packages à jour
- [ ] npm audit clean
- [ ] Sources de confiance

### Workflow sécurisé

```
Prompt → Code généré → Audit sécu → Review humain → Correctifs → ✅
```

### Prompt d'audit sécurité

```
Analyse ce code pour des vulnérabilités de sécurité.

Vérifie :
1. Injection (SQL, XSS, Command)
2. Authentification / Autorisation
3. Exposition de données sensibles
4. Configuration de sécurité
5. Dépendances vulnérables

Pour chaque problème :
- Sévérité (Critique/Haute/Moyenne/Basse)
- Localisation (fichier, ligne)
- Description du risque
- Code corrigé proposé

Code à auditer :
[Coller le code]
```

### Exemple d'audit

**Code généré :**
```javascript
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = db.query(`SELECT * FROM users WHERE username = '${username}'`);
  if (user.password === password) {
    res.json({ token: user.id });
  }
});
```

**Audit :**
```
🔴 CRITIQUE - Injection SQL (ligne 3)
→ Utiliser des requêtes préparées

🔴 CRITIQUE - Stockage mot de passe (ligne 4)
→ Utiliser bcrypt pour hash/compare

🟠 HAUTE - Token prédictible (ligne 5)
→ Utiliser JWT ou session sécurisée
```

**Code corrigé :**
```javascript
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await db.query(
    'SELECT * FROM users WHERE username = ?', 
    [username]
  );
  if (user && await bcrypt.compare(password, user.passwordHash)) {
    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET);
    res.json({ token });
  }
});
```

### Tips & astuces

- Préférer Cursor (code visible) à Bolt (boîte noire)
- Toujours auditer AVANT de déployer
- Les variables d'environnement sont vos amies

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Prototyper rapidement avec l'IA
- Identifier les vulnérabilités courantes
- Appliquer une checklist sécurité
- Corriger les failles avant déploiement

### Prérequis participants

- Notions de développement web
- Compte sur un outil de vibe coding (Cursor, Replit, Bolt)

### Matériel nécessaire

- [ ] Checklist sécurité imprimée
- [ ] Prompt d'audit
- [ ] Exemples de code vulnérable
- [ ] Exemples de corrections

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Démo vibe coding + risques | Voient la puissance et les dangers | Sensibilisation |
| 10-15 | Setup | Aide à choisir l'outil | Configurent leur environnement | Préparation |
| 15-30 | Prototypage | Circule, aide | Créent une mini-app par prompt | Production |
| 30-45 | Audit | Guide la checklist | Passent l'audit sécurité | Vérification |
| 45-55 | Correction | Montre les patterns de correction | Corrigent les vulnérabilités | Amélioration |
| 55-60 | Partage | Retour d'expérience | Partagent leurs découvertes | Apprentissage |

### Points d'attention animateur

**Pièges courants :**

- "Ça marche donc c'est OK" → Le code peut marcher ET être vulnérable
- Confiance aveugle dans l'IA → L'IA génère du code fonctionnel, pas sécurisé
- Oublier les .env → Les secrets finissent sur GitHub

**Questions fréquentes :**

- "L'IA devrait savoir faire du code sécurisé ?" → Non, elle optimise pour "ça marche"
- "Cursor vs Bolt ?" → Cursor = contrôle, Bolt = vitesse
- "Comment auditer automatiquement ?" → npm audit, Snyk, SonarQube

### Variantes

**Version simple (30 min) :**
- Code pré-généré à auditer
- Focus sur l'identification des failles

**Version avancée (2h) :**
- App complète avec auth
- Intégration CI/CD avec audit automatique

---

## Ressources complémentaires

- [OWASP Top 10](https://owasp.org/Top10/)
- [Snyk](https://snyk.io/) — audit de dépendances
- [Cursor](https://cursor.sh/)
