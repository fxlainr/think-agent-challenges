-- Préparation de la base avant import
-- Exécuter UNE SEULE FOIS avant le premier import

-- 1. Ajouter la contrainte unique sur titre (nécessaire pour UPSERT)
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'challenges_titre_unique'
    ) THEN
        ALTER TABLE challenges ADD CONSTRAINT challenges_titre_unique UNIQUE (titre);
    END IF;
END $$;

-- 2. S'assurer que les nouveaux champs existent
ALTER TABLE challenges 
ADD COLUMN IF NOT EXISTS vision_impact TEXT,
ADD COLUMN IF NOT EXISTS le_saviez_vous TEXT,
ADD COLUMN IF NOT EXISTS sources JSONB DEFAULT '[]';
