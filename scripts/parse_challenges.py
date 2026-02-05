#!/usr/bin/env python3
"""
Parse tous les challenges markdown et génère :
1. SYNC_STATE.json - État de la synchronisation
2. challenges_import.sql - Script SQL UPSERT
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

def parse_markdown_table(content, start_marker="## Métadonnées"):
    """Extrait les métadonnées du tableau markdown."""
    metadata = {}
    
    # Trouver la section métadonnées
    start = content.find(start_marker)
    if start == -1:
        return metadata
    
    # Trouver la fin de la section (prochaine section ## ou fin)
    section = content[start:start+1500]
    
    # Parser les lignes du tableau
    lines = section.split('\n')
    for line in lines:
        if '|' in line and '---' not in line:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                key = parts[0].lower().replace(' ', '_').replace('**', '')
                value = parts[1].replace('**', '').strip()
                if key and value and key not in ['propriété', 'valeur']:
                    metadata[key] = value
    
    return metadata

def extract_section(content, section_name):
    """Extrait le contenu d'une section markdown."""
    pattern = rf"## {section_name}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def parse_challenge_file(filepath):
    """Parse un fichier challenge et retourne ses données structurées."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Titre (première ligne # )
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else Path(filepath).stem
    
    # Métadonnées du tableau
    metadata = parse_markdown_table(content)
    
    # Sections spécifiques
    vision = extract_section(content, "Vision & Impact")
    saviez_vous = extract_section(content, "Le saviez-vous \\?")
    description_section = extract_section(content, "Description")
    sources_section = extract_section(content, "Sources")
    
    # Parser les sources (liens)
    sources = []
    if sources_section:
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', sources_section)
        sources = [url for _, url in links]
    
    # Nettoyer la description
    description = ""
    if description_section:
        # Enlever la citation > et prendre le reste
        lines = description_section.split('\n')
        desc_lines = []
        for line in lines:
            if line.startswith('>'):
                continue
            if line.strip():
                desc_lines.append(line.strip())
        description = ' '.join(desc_lines[:3])  # Premiers paragraphes
    
    # Mapper les niveaux
    niveau_map = {
        'explorer': 'Explorer',
        'crafter': 'Crafter', 
        'architecte': 'Architecte'
    }
    
    # Déterminer le niveau depuis le path
    path_parts = filepath.split('/')
    niveau_from_path = None
    for part in path_parts:
        if part in niveau_map:
            niveau_from_path = niveau_map[part]
            break
    
    # Difficulté -> nombre d'étoiles
    difficulte_str = metadata.get('difficulté', '⭐⭐')
    difficulte = difficulte_str.count('⭐')
    if difficulte == 0:
        difficulte = 2
    
    # XP
    xp_str = metadata.get('xp', '100')
    try:
        xp = int(re.sub(r'[^\d]', '', xp_str))
    except:
        xp = 100
    
    # Slug depuis le nom de fichier
    slug = Path(filepath).stem
    
    return {
        'slug': slug,
        'titre': title,
        'description': description[:500] if description else f"Challenge {title}",
        'niveau_associe': niveau_from_path or metadata.get('type', 'Crafter'),
        'type': 'Exercice',  # Par défaut
        'difficulte': difficulte,
        'duree_estimee': metadata.get('durée_solo', '1h'),
        'xp': xp,
        'marque': metadata.get('marque', 'Tous'),
        'vision_impact': vision,
        'le_saviez_vous': saviez_vous,
        'sources': sources,
        'filepath': filepath,
        'parsed_at': datetime.now().isoformat()
    }

def generate_sql_upsert(challenges):
    """Génère le SQL UPSERT pour tous les challenges."""
    sql_lines = [
        "-- Script de synchronisation des challenges",
        f"-- Généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"-- Total: {len(challenges)} challenges",
        "",
        "-- Utilise slug comme identifiant unique pour l'upsert",
        "-- Créer une contrainte unique sur titre si pas déjà fait",
        "-- ALTER TABLE challenges ADD CONSTRAINT challenges_titre_unique UNIQUE (titre);",
        "",
    ]
    
    for c in challenges:
        # Escape les apostrophes
        titre = c['titre'].replace("'", "''")
        description = (c['description'] or '').replace("'", "''")
        vision = (c['vision_impact'] or '').replace("'", "''") if c['vision_impact'] else 'NULL'
        saviez = (c['le_saviez_vous'] or '').replace("'", "''") if c['le_saviez_vous'] else 'NULL'
        sources_json = json.dumps(c['sources']) if c['sources'] else '[]'
        
        vision_sql = f"'{vision}'" if vision != 'NULL' else 'NULL'
        saviez_sql = f"'{saviez}'" if saviez != 'NULL' else 'NULL'
        
        sql = f"""
INSERT INTO challenges (
    titre, description, niveau_associe, type, difficulte, 
    duree_estimee, xp, marque, vision_impact, le_saviez_vous, sources,
    type_evaluation, statut, participants, outils_recommandes, livrables
) VALUES (
    '{titre}',
    '{description}',
    '{c['niveau_associe']}',
    'Exercice',
    {c['difficulte']},
    '{c['duree_estimee']}',
    {c['xp']},
    '{c['marque']}',
    {vision_sql},
    {saviez_sql},
    '{sources_json}'::jsonb,
    'Manuelle',
    'Actif',
    'Solo',
    '[]'::jsonb,
    '[]'::jsonb
)
ON CONFLICT (titre) DO UPDATE SET
    description = EXCLUDED.description,
    niveau_associe = EXCLUDED.niveau_associe,
    difficulte = EXCLUDED.difficulte,
    duree_estimee = EXCLUDED.duree_estimee,
    xp = EXCLUDED.xp,
    marque = EXCLUDED.marque,
    vision_impact = EXCLUDED.vision_impact,
    le_saviez_vous = EXCLUDED.le_saviez_vous,
    sources = EXCLUDED.sources,
    updated_at = NOW();
"""
        sql_lines.append(sql)
    
    return '\n'.join(sql_lines)

def main():
    base_dir = Path(__file__).parent.parent / 'challenges'
    challenges = []
    
    # Parser tous les fichiers
    for level_dir in ['explorer', 'crafter', 'architecte']:
        level_path = base_dir / level_dir
        if level_path.exists():
            for md_file in level_path.glob('*.md'):
                try:
                    challenge = parse_challenge_file(str(md_file))
                    challenges.append(challenge)
                    print(f"✓ {challenge['niveau_associe']}: {challenge['titre']}")
                except Exception as e:
                    print(f"✗ Erreur {md_file}: {e}")
    
    # Trier par niveau puis titre
    niveau_order = {'Explorer': 0, 'Crafter': 1, 'Architecte': 2}
    challenges.sort(key=lambda x: (niveau_order.get(x['niveau_associe'], 1), x['titre']))
    
    # Générer SYNC_STATE.json
    sync_state = {
        'generated_at': datetime.now().isoformat(),
        'total_challenges': len(challenges),
        'by_niveau': {
            'Explorer': len([c for c in challenges if c['niveau_associe'] == 'Explorer']),
            'Crafter': len([c for c in challenges if c['niveau_associe'] == 'Crafter']),
            'Architecte': len([c for c in challenges if c['niveau_associe'] == 'Architecte']),
        },
        'challenges': [
            {
                'slug': c['slug'],
                'titre': c['titre'],
                'niveau': c['niveau_associe'],
                'marque': c['marque'],
                'xp': c['xp']
            }
            for c in challenges
        ]
    }
    
    # Écrire les fichiers
    output_dir = Path(__file__).parent.parent
    
    with open(output_dir / 'SYNC_STATE.json', 'w', encoding='utf-8') as f:
        json.dump(sync_state, f, indent=2, ensure_ascii=False)
    print(f"\n✓ SYNC_STATE.json généré ({len(challenges)} challenges)")
    
    sql = generate_sql_upsert(challenges)
    with open(output_dir / 'scripts' / 'challenges_import.sql', 'w', encoding='utf-8') as f:
        f.write(sql)
    print(f"✓ scripts/challenges_import.sql généré")

if __name__ == '__main__':
    main()
