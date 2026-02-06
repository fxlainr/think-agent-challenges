# Mon Premier Agent n8n - Gestionnaire de Tâches

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 45 min |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐ |
| Prérequis | Compte n8n, Google Sheets, clé API OpenAI |

---

## Description

> *Construis ton premier agent IA capable d'agir sur des données réelles — le "Hello World" des agents autonomes.*

Les chatbots répondent. Les agents **agissent**. Dans ce challenge, tu vas créer un assistant conversationnel qui gère une liste de tâches dans Google Sheets : créer, lire, modifier, supprimer — tout ça en langage naturel.

C'est simple, mais les patterns que tu apprends ici s'appliquent à des cas bien plus complexes : CRM automatisé, support client intelligent, pilotage de projets...

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Workflow n8n fonctionnel exporté en JSON
- [ ] Screenshot de l'interface de chat avec une conversation de test
- [ ] Google Sheet avec quelques tâches créées via l'agent

**Critères de réussite :**

| Critère | Points |
|---------|--------|
| L'agent répond en langage naturel | 20 |
| Création de tâches fonctionnelle | 20 |
| Lecture des tâches fonctionnelle | 20 |
| Mise à jour de tâches fonctionnelle | 20 |
| Suppression avec confirmation | 10 |
| System prompt clair et structuré | 10 |

---

## Pistes de Solution

### Architecture cible

```
[Chat Trigger] → [AI Agent]
                     ↑
         ┌──────────┼──────────┐
         │          │          │
    [Model]    [Memory]    [Tools]
    GPT-4o     Buffer      - Get tasks
                           - Create task
                           - Update task  
                           - Delete task
```

### Étape 1 : Préparer Google Sheets

Crée une nouvelle Google Sheet avec les colonnes :

| Task | Status | Description | Deadline |
|------|--------|-------------|----------|
| (nom) | TODO/IN PROGRESS/DONE | (détails) | (date) |

### Étape 2 : Créer le workflow n8n

1. Nouveau workflow → Ajoute un nœud **Chat Trigger**
2. Ajoute un nœud **AI Agent** (LangChain)
3. Connecte le Chat Trigger à l'Agent

### Étape 3 : Configurer le LLM

1. Sous l'Agent, ajoute **OpenAI Chat Model**
2. Configure tes credentials OpenAI
3. Sélectionne `gpt-4o`

### Étape 4 : Ajouter la mémoire

1. Sous l'Agent, ajoute **Window Buffer Memory**
2. Configure `Context Window Length` à 10

### Étape 5 : Créer les 4 outils Google Sheets

**Tool 1 : Get tasks** (Read)
- Sélectionne ta Sheet

**Tool 2 : Create task** (Append)
```javascript
{
  "Task": "={{ $fromAI('Task', '', 'string') }}",
  "Status": "={{ $fromAI('Status', '', 'string') }}",
  "Description": "={{ $fromAI('Description', '', 'string') }}",
  "Deadline": "={{ $fromAI('Deadline', '', 'string') }}"
}
```

**Tool 3 : Update task** (Update)
- Matching column : `row_number`
- Mêmes mappings + `row_number`

**Tool 4 : Delete task** (Delete)
```javascript
startIndex: "={{ $fromAI('Start_Row_Number', '', 'number') }}"
numberToDelete: "={{ $fromAI('Number_of_Rows_to_Delete', '', 'number') }}"
```

### Étape 6 : System Prompt

```markdown
# Task Management Agent

Tu es un assistant de gestion de tâches via Google Sheets.

## Capacités
- Voir, créer, modifier et supprimer des tâches

## Structure des données
- **Task** : Nom de la tâche (obligatoire)
- **Status** : TODO, IN PROGRESS, ou DONE (défaut: TODO)
- **Description** : Détails optionnels
- **Deadline** : Date limite optionnelle

Note: Google Sheets fournit automatiquement un champ row_number.

## Règles importantes
- Statuts valides : "TODO", "IN PROGRESS", "DONE"
- Nouveau tâche = "TODO" par défaut
- "marquer comme terminé" → Status = "DONE"
- "commencer" → Status = "IN PROGRESS"
- TOUJOURS demander confirmation avant suppression

## Style
- Être utile et efficace
- Toujours confirmer les actions effectuées
- Langage amical et professionnel
```

### Tests de validation

Teste ces scénarios :
1. "Montre-moi mes tâches"
2. "Ajoute une tâche : Préparer la réunion client"
3. "Mets la tâche Réunion en cours"
4. "Marque Réunion comme terminée"
5. "Supprime la tâche terminée" → doit demander confirmation

### Tips & astuces

- **$fromAI()** est la magie : ça permet au LLM de comprendre quels champs remplir dynamiquement
- **row_number** est généré automatiquement par Google Sheets — pas besoin de le créer
- Commence par tester chaque tool individuellement avant de tout assembler

---

## Animation Dojo (1h30, 4-8 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Configurer un agent LangChain dans n8n
- Connecter un LLM comme "cerveau" de l'agent
- Créer des outils (Tools) que l'agent peut appeler
- Rédiger un System Prompt efficace

### Prérequis participants

- Laptop avec navigateur
- Compte n8n (cloud ou self-hosted)
- Compte Google
- Clé API OpenAI (ou clés de test fournies par l'animateur)

### Matériel nécessaire

- [ ] Workflow de démo fonctionnel à montrer
- [ ] Template de Google Sheet pré-formaté
- [ ] Clés API de secours si participants n'en ont pas
- [ ] Guide pas-à-pas projeté

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Présente agents vs chatbots. Démo live impressionnante ("Supprime toutes les tâches terminées") | Observent | Donner envie |
| 10-25 | Setup | Guide la création de la Sheet + credentials n8n/Google/OpenAI | Configurent leurs accès | Débloquer les prérequis |
| 25-45 | Build guidé | Écran partagé, construit le workflow étape par étape | Suivent et reproduisent | Construction |
| 45-60 | Tests | Fait tester chaque fonctionnalité, aide au debug | Testent, partagent leurs bugs | Validation |
| 60-80 | Personnalisation | Propose des variantes, circule pour aider | Customisent leur agent | Appropriation |
| 80-90 | Debrief | Fait présenter les meilleures variantes, Q&A | Partagent, posent questions | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- **Credentials Google OAuth** : C'est le blocage #1. Prévoir 10-15 min de marge.
- **$fromAI() mal configuré** : Vérifier les guillemets et la syntaxe
- **row_number introuvable** : Rappeler qu'il apparaît automatiquement après la première lecture

**Questions fréquentes :**

- "Pourquoi GPT-4o et pas GPT-3.5 ?" → GPT-4o comprend mieux les instructions complexes du system prompt
- "Ça coûte combien ?" → ~$0.01-0.02 par conversation de test
- "Je peux utiliser Claude ?" → Oui, n8n supporte Anthropic, setup quasi identique

**Tips d'animation :**

- Avoir un workflow backup prêt à importer si quelqu'un est bloqué
- Montrer les logs n8n pour debug — ça rassure de voir ce qui se passe
- Faire une démo "fail" volontaire (supprimer sans confirmation) pour montrer l'importance du system prompt

### Variantes pour les plus rapides

1. **Ajouter Priority** : Champ High/Medium/Low avec couleurs
2. **Notification Slack** : Message quand une tâche est créée
3. **Récap quotidien** : Cron qui liste les tâches "IN PROGRESS" chaque matin
4. **Multi-projets** : Champ "Projet" pour filtrer
5. **Alertes deadline** : Prévenir quand une deadline approche

---

## Le saviez-vous ?

Le concept d'agent IA remonte aux années 1990, mais c'est l'arrivée des LLM comme GPT-4 qui l'a rendu accessible. Aujourd'hui, avec des outils no-code comme n8n, tu peux créer en 45 minutes ce qui aurait demandé des semaines de développement il y a 2 ans.

---

## Ressources complémentaires

- [Documentation n8n AI Agents](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
- [Google Sheets Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-base.googlesheetstool/)
