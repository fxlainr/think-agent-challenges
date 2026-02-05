-- Préparation de la base avant import
-- Exécuter UNE SEULE FOIS avant le premier import

-- 1. Ajouter la contrainte unique sur titre (nécessaire pour UPSERT)
ALTER TABLE challenges 
ADD CONSTRAINT IF NOT EXISTS challenges_titre_unique UNIQUE (titre);

-- 2. S'assurer que les nouveaux champs existent
ALTER TABLE challenges 
ADD COLUMN IF NOT EXISTS vision_impact TEXT,
ADD COLUMN IF NOT EXISTS le_saviez_vous TEXT,
ADD COLUMN IF NOT EXISTS sources JSONB DEFAULT '[]';

-- Note: Si "IF NOT EXISTS" ne fonctionne pas sur votre version PostgreSQL,
-- ignorer les erreurs "already exists"
