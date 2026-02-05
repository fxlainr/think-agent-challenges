# L'Architecte de Systèmes Souverains

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | VALUE |
| Durée solo | 8h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐⭐⭐ |
| XP | 420 |
| Prérequis | Architecture logicielle, vision stratégique |

---

## Vision & Impact

Pour garantir une agilité réelle, il faut envisager de **fabriquer ses propres outils** et ses propres workflows plutôt que de dépendre uniquement de solutions tierces. Ce challenge consiste à bâtir une infrastructure logicielle interne sur mesure.

## Le saviez-vous ?

Le risque majeur actuel est de s'attacher à des compétences ou des outils qui seront **obsolètes dans quelques mois**. La souveraineté technologique devient un avantage compétitif.

## Sources

- [L'IA va détruire des millions d'emplois - Carlos Diaz](https://www.linkedin.com/posts/carlosdiazprofile_lia-va-d%C3%A9truire-des-millions-demplois-activity-7419371381898964992-oL6f)

---

## Description

> *Construisez votre propre stack d'outils plutôt que d'en dépendre.*

SaaS qui augmente ses prix. API dépréciée. Vendor lock-in. Ce challenge vous fait concevoir et construire des outils internes qui vous rendent maître de votre destin technologique.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Audit de dépendances critiques
- [ ] 1 outil interne remplaçant une dépendance
- [ ] Stratégie de souveraineté documentée

**Critères de réussite :**

- Réduction d'une dépendance critique
- Outil interne fonctionnel et maintenable
- ROI documenté

---

## Pistes de Solution

### Audit des dépendances

```
POUR CHAQUE OUTIL EXTERNE :

1. CRITICITÉ
   - Que se passe-t-il s'il disparaît demain ?
   - Combien de temps pour remplacer ?
   - Impact business ?

2. RISQUES
   - Vendor lock-in ?
   - Augmentation de prix probable ?
   - Pérennité du fournisseur ?
   - Données sensibles hébergées ?

3. ALTERNATIVES
   - Open source existant ?
   - Faisable en interne ?
   - Coût de construction vs coût de licence ?

MATRICE DE DÉCISION :
| Outil | Criticité | Risque | Build interne ? |
|-------|-----------|--------|-----------------|
```

### Outils candidats au remplacement

```
SOUVENT REMPLAÇABLES :
├── Analytics → Plausible/Umami self-hosted
├── Email marketing → Listmonk
├── CMS → Strapi/Payload
├── Formulaires → Custom + Supabase
└── Notifications → Novu self-hosted

PARFOIS REMPLAÇABLES :
├── Slack → Matrix + Element
├── Notion → AppFlowy / Custom
├── Linear → Custom issue tracker
└── Calendly → Cal.com self-hosted

RAREMENT REMPLAÇABLES (pour l'instant) :
├── AWS/GCP/Azure → Trop d'effort
├── Stripe → Régulation complexe
├── Figma → Pas d'alternative viable
└── GitHub → Gitlab self-hosted possible
```

### Framework de décision

```
CONSTRUIRE SI :
✅ Criticité haute + Risque élevé
✅ ROI positif sur 18 mois
✅ Compétences disponibles en interne
✅ Maintenance soutenable
✅ Différenciation potentielle

ACHETER SI :
✅ Non critique
✅ Pas de lock-in
✅ Coût < coût de construction
✅ Pas de données sensibles
✅ Standards ouverts (export facile)
```

### Architecture d'un outil souverain

```
PRINCIPES :

1. DONNÉES FIRST
   - Base de données sous votre contrôle
   - Export facile et documenté
   - Backup automatique

2. MODULARITÉ
   - Composants remplaçables
   - APIs internes documentées
   - Pas de couplage fort

3. SIMPLICITÉ
   - Faire une chose bien
   - Pas de feature creep
   - Maintenable par l'équipe

4. OPEN STANDARDS
   - Formats ouverts
   - Protocoles standards
   - Intégrations via API
```

### Exemple : Internal Analytics Tool

```python
"""
Remplacer Google Analytics par un outil interne

Fonctionnalités :
- Page views
- Unique visitors
- Referrers
- Top pages
- Simple dashboard

Stack :
- PostgreSQL (données)
- FastAPI (collecte)
- React (dashboard)
- ~2 jours de dev
"""

# Collecte (1 endpoint)
@app.post("/track")
async def track_event(event: Event):
    await db.execute("""
        INSERT INTO events (timestamp, page, referrer, session_id)
        VALUES ($1, $2, $3, $4)
    """, event.timestamp, event.page, event.referrer, event.session_id)
    return {"status": "ok"}

# Dashboard : quelques requêtes SQL simples
# C'est tout. Pas besoin de plus.
```

---

## Animation Dojo (4h workshop)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-30 | Intro | Souveraineté : pourquoi maintenant |
| 30-90 | Audit | Cartographier les dépendances |
| 90-120 | Sélection | Choisir 1 outil à remplacer |
| 120-180 | Build | Construire un MVP |
| 180-210 | Test | Valider le remplacement |
| 210-240 | Clôture | Stratégie long terme |

### Points d'attention

- Ne pas tout reconstruire (piège)
- Commencer par le plus critique
- La maintenance est le vrai coût
