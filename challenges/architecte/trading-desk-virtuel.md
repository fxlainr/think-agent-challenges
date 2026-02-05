# Le Trading Desk Virtuel

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 16h |
| Durée Dojo | 2 jours (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Python, notions de finance de marché |

---

## Description

> *Construisez un système de backtesting de stratégies avec agents IA : un agent analyse les signaux, un autre gère le risque, un troisième exécute.*

Trois cerveaux valent mieux qu'un. Ce challenge vous fait créer un trading desk virtuel où des agents spécialisés collaborent : l'analyste génère des signaux, le risk manager valide et dimensionne, l'exécuteur simule les ordres.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Architecture multi-agents fonctionnelle
- [ ] Backtest sur données historiques
- [ ] Dashboard de performance avec métriques clés

**Critères de réussite :**

- Les 3 agents ont des rôles distincts et interagissent
- Le backtest produit des métriques réalistes (Sharpe, drawdown)
- Le système est paramétrable (stratégie, limites de risque)

---

## Pistes de Solution

### Architecture multi-agents

```
┌─────────────────────────────────────────────────────────┐
│                  VIRTUAL TRADING DESK                    │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Signal    │    │    Risk     │    │  Execution  │  │
│  │   Analyst   │───▶│   Manager   │───▶│   Agent     │  │
│  │             │    │             │    │             │  │
│  │ • Génère    │    │ • Valide    │    │ • Exécute   │  │
│  │   signaux   │    │ • Size      │    │ • Log       │  │
│  │ • Score     │    │ • Stop-loss │    │ • P&L       │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         ▲                                      │         │
│         └──────────────── Market Data ─────────┘         │
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │                    BACKTEST ENGINE                   ││
│  │  • Historical data • Order simulation • Metrics      ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
```

### Rôle de chaque agent

| Agent | Input | Output | Décision |
|-------|-------|--------|----------|
| Signal Analyst | Market data, indicators | Signal + score | Quoi trader |
| Risk Manager | Signal, portfolio, limits | Approved + size | Combien, quel stop |
| Execution Agent | Order approved | Execution report | Comment exécuter |

### Prompts des agents

**Signal Analyst :**
```
Tu es un analyste quantitatif. Analyse les données et génère des signaux.

Input : Données OHLCV + indicateurs
Output JSON :
{
  "signal": "LONG" | "SHORT" | "FLAT",
  "score": 0-100,
  "entry_price": X,
  "rationale": "..."
}

Règles : Score > 70 pour générer un signal
```

**Risk Manager :**
```
Tu es le risk manager. Tu valides ou rejettes les signaux.

Input : Signal + Portfolio + Limits
Output JSON :
{
  "approved": true/false,
  "position_size": X,
  "stop_loss": X,
  "take_profit": X
}

Règles : Max 2% risque/trade, max 10% exposition/asset
```

### Métriques de backtest

| Métrique | Formule | Interprétation |
|----------|---------|----------------|
| Total Return | (Pf final - initial) / initial | Performance absolue |
| Sharpe Ratio | (Return - Rf) / Volatility | Return ajusté du risque |
| Max Drawdown | Max peak-to-trough | Pire perte |
| Win Rate | Trades gagnants / Total | Taux de succès |
| Profit Factor | Gains / Pertes | Qualité stratégie |

### Structure de données

```python
trade = {
    "id": "T001",
    "timestamp": "2024-01-15T10:30:00Z",
    "signal_score": 85,
    "direction": "LONG",
    "asset": "AAPL",
    "entry_price": 185.50,
    "size": 100,
    "stop_loss": 182.00,
    "exit_price": 192.00,
    "pnl": 650.00,
    "pnl_pct": 3.5
}
```

### Tips & astuces

- Commencer simple : 1 asset, 1 stratégie (ex: croisement de moyennes)
- Attention au overfitting : tester sur données out-of-sample
- Les frais de transaction changent tout — les inclure

---

## Animation Dojo (2 jours, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Concevoir une architecture multi-agents
- Implémenter un système de backtest
- Calculer et interpréter les métriques de performance
- Collaborer entre agents spécialisés

### Prérequis participants

- Python niveau intermédiaire
- Notions de finance de marché (OHLCV, ordres)
- Curiosité pour le trading algorithmique

### Matériel nécessaire

- [ ] Données historiques (Yahoo Finance, gratuit)
- [ ] Prompts des 3 agents
- [ ] Code de démarrage (backtest engine)
- [ ] Template de dashboard

### Déroulé (2 jours)

| Jour | Demi-journée | Contenu | Livrable |
|------|--------------|---------|----------|
| J1 | Matin | Théorie trading + architecture multi-agents | Compréhension |
| J1 | Après-midi | Signal Analyst + Risk Manager | 2 agents fonctionnels |
| J2 | Matin | Execution Agent + Backtest engine | Système complet |
| J2 | Après-midi | Tests + Dashboard | Démo finale |

### Points d'attention animateur

**Pièges courants :**

- Stratégie trop complexe au départ → Commencer par croisement de moyennes
- Pas de frais de transaction → Les inclure (impact énorme)
- Overfitting → Séparer données train/test

**Questions fréquentes :**

- "C'est légal de trader avec ça ?" → C'est du backtest, pas du vrai trading
- "Pourquoi 3 agents ?" → Séparation des responsabilités, comme dans un vrai desk
- "Ça marche vraiment ?" → En backtest oui, en live c'est une autre histoire

### Variantes

**Version découverte (4h) :**
- 1 agent uniquement (Signal Analyst)
- Backtest pré-construit
- Focus sur la stratégie

**Version production (1 semaine) :**
- Multi-assets, multi-stratégies
- Paper trading temps réel
- Alertes et monitoring

---

## Ressources complémentaires

- [Backtrader](https://www.backtrader.com/) — framework Python de backtest
- [QuantConnect](https://www.quantconnect.com/) — plateforme de trading algorithmique
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
