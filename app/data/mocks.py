# Données des étudiants avec statistiques
students = [
    {
        "id": 1, 
        "name": "Moberak", 
        "score": 453,
        "total_quizzes": 28,
        "correct_answers": 234,
        "level": "Expert",
        "rank": 1
    },
    {
        "id": 2, 
        "name": "Keya", 
        "score": 373,
        "total_quizzes": 22,
        "correct_answers": 189,
        "level": "Avancé",
        "rank": 3
    },
    {
        "id": 3, 
        "name": "Moni", 
        "score": 442,
        "total_quizzes": 26,
        "correct_answers": 221,
        "level": "Expert",
        "rank": 2
    },
    {
        "id": 4, 
        "name": "Kaosar", 
        "score": 224,
        "total_quizzes": 15,
        "correct_answers": 112,
        "level": "Intermédiaire",
        "rank": 4
    },
    {
        "id": 5, 
        "name": "Shakib", 
        "score": 163,
        "total_quizzes": 12,
        "correct_answers": 87,
        "level": "Débutant",
        "rank": 5
    },
    {
        "id": 6, 
        "name": "Muhib", 
        "score": 131,
        "total_quizzes": 10,
        "correct_answers": 68,
        "level": "Débutant",
        "rank": 6
    },
    {
        "id": 7, 
        "name": "Shama", 
        "score": 129,
        "total_quizzes": 9,
        "correct_answers": 64,
        "level": "Débutant",
        "rank": 7
    },
]

subjects = [
    {"id": 1, "name": "Mathematics"},
    {"id": 2, "name": "Physics"},
    {"id": 3, "name": "Chemistry"},
    {"id": 4, "name": "Biology"},
]

# Relation étudiants-matières
students_subjects = [
    {"student_id": 1, "subject_id": 1},
    {"student_id": 1, "subject_id": 3},
    {"student_id": 2, "subject_id": 2},
    {"student_id": 2, "subject_id": 4},
    {"student_id": 3, "subject_id": 1},
    {"student_id": 3, "subject_id": 2},
    {"student_id": 4, "subject_id": 3},
    {"student_id": 5, "subject_id": 1},
    {"student_id": 6, "subject_id": 4},
    {"student_id": 7, "subject_id": 2},
]

# Statistiques globales
global_stats = {
    "total_players": len(students),
    "total_quizzes": sum(s["total_quizzes"] for s in students),
    "active_categories": 6,
    "total_questions": 35
}

QUIZ_QUESTIONS = {
    "sports": [
        {"id": 1, "question": "Quelle est la ville la plus peuplée du monde ?", "options": ["San Francisco", "Tokyo", "Berlin", "Lisbonne"], "answer": "Tokyo"},
        {"id": 2, "question": "Combien de joueurs y a-t-il sur le terrain dans une équipe de basketball ?", "options": ["5", "6", "7", "11"], "answer": "5"},
        {"id": 3, "question": "Quel pays a accueilli les Jeux Olympiques d'été de 2016 ?", "options": ["Chine", "Brésil", "Royaume-Uni", "Japon"], "answer": "Brésil"},
        {"id": 4, "question": "Quel sport est connu comme 'le beau jeu' ?", "options": ["Basketball", "Tennis", "Football", "Cricket"], "answer": "Football"},
        {"id": 5, "question": "Combien y a-t-il de tournois du Grand Chelem en tennis ?", "options": ["2", "3", "4", "5"], "answer": "4"},
        {"id": 6, "question": "Quelle est la durée d'un match de football professionnel ?", "options": ["80 minutes", "90 minutes", "100 minutes", "120 minutes"], "answer": "90 minutes"},
    ],
    "chemistry": [
        {"id": 1, "question": "Quel est le symbole chimique de l'or ?", "options": ["Go", "Gd", "Au", "Ag"], "answer": "Au"},
        {"id": 2, "question": "Quel est le pH de l'eau pure ?", "options": ["5", "7", "9", "11"], "answer": "7"},
        {"id": 3, "question": "Quel gaz les plantes absorbent-elles de l'atmosphère ?", "options": ["Oxygène", "Azote", "Dioxyde de carbone", "Hydrogène"], "answer": "Dioxyde de carbone"},
        {"id": 4, "question": "Quel est l'élément le plus abondant dans l'univers ?", "options": ["Oxygène", "Carbone", "Hydrogène", "Hélium"], "answer": "Hydrogène"},
        {"id": 5, "question": "Comment appelle-t-on couramment H2O ?", "options": ["Sel", "Eau", "Sucre", "Acide"], "answer": "Eau"},
        {"id": 6, "question": "Quel est le numéro atomique du carbone ?", "options": ["4", "6", "8", "12"], "answer": "6"},
    ],
    "economics": [
        {"id": 1, "question": "Que signifie PIB ?", "options": ["Produit Intérieur Brut", "Protection des Données Générales", "Plan de Développement Global", "Période de Grande Dépression"], "answer": "Produit Intérieur Brut"},
        {"id": 2, "question": "Qu'est-ce que l'inflation ?", "options": ["Baisse des prix", "Augmentation des prix", "Prix stables", "Prix zéro"], "answer": "Augmentation des prix"},
        {"id": 3, "question": "Qui est considéré comme le père de l'économie moderne ?", "options": ["Karl Marx", "Adam Smith", "John Keynes", "Milton Friedman"], "answer": "Adam Smith"},
        {"id": 4, "question": "Qu'est-ce qu'un monopole ?", "options": ["Plusieurs vendeurs", "Un seul vendeur", "Deux vendeurs", "Aucun vendeur"], "answer": "Un seul vendeur"},
        {"id": 5, "question": "Quelle monnaie est utilisée au Japon ?", "options": ["Yuan", "Won", "Yen", "Roupie"], "answer": "Yen"},
        {"id": 6, "question": "Qu'est-ce que l'offre et la demande ?", "options": ["Loi économique", "Théorie politique", "Concept sociologique", "Principe mathématique"], "answer": "Loi économique"},
    ],
    "astronomy": [
        {"id": 1, "question": "Quelle est la planète la plus proche du Soleil ?", "options": ["Vénus", "Terre", "Mercure", "Mars"], "answer": "Mercure"},
        {"id": 2, "question": "Combien y a-t-il de planètes dans notre système solaire ?", "options": ["7", "8", "9", "10"], "answer": "8"},
        {"id": 3, "question": "Quelle est la plus grande planète de notre système solaire ?", "options": ["Saturne", "Jupiter", "Neptune", "Uranus"], "answer": "Jupiter"},
        {"id": 4, "question": "Dans quelle galaxie vivons-nous ?", "options": ["Andromède", "Voie Lactée", "Triangulum", "Whirlpool"], "answer": "Voie Lactée"},
        {"id": 5, "question": "Qu'est-ce qu'une année-lumière ?", "options": ["Temps", "Distance", "Vitesse", "Masse"], "answer": "Distance"},
        {"id": 6, "question": "Quelle est l'étoile la plus proche de la Terre ?", "options": ["Alpha Centauri", "Sirius", "Le Soleil", "Proxima Centauri"], "answer": "Le Soleil"},
    ],
    "math": [
        {"id": 1, "question": "Combien font 15 × 12 ?", "options": ["150", "180", "200", "175"], "answer": "180"},
        {"id": 2, "question": "Quelle est la racine carrée de 144 ?", "options": ["10", "11", "12", "13"], "answer": "12"},
        {"id": 3, "question": "π (pi) est approximativement égal à ?", "options": ["2,14", "3,14", "4,14", "5,14"], "answer": "3,14"},
        {"id": 4, "question": "Quel est 25 % de 200 ?", "options": ["25", "50", "75", "100"], "answer": "50"},
        {"id": 5, "question": "Quel est le nombre premier suivant après 7 ?", "options": ["9", "10", "11", "13"], "answer": "11"},
        {"id": 6, "question": "Combien font 8² ?", "options": ["16", "64", "32", "128"], "answer": "64"},
    ],
    "architecture": [
        {"id": 1, "question": "Qui a conçu la Tour Eiffel ?", "options": ["Le Corbusier", "Gustave Eiffel", "Antoni Gaudí", "Frank Lloyd Wright"], "answer": "Gustave Eiffel"},
        {"id": 2, "question": "Dans quelle ville se trouve le Burj Khalifa ?", "options": ["Abu Dhabi", "Dubaï", "Doha", "Riyad"], "answer": "Dubaï"},
        {"id": 3, "question": "Quel style architectural pour la Sagrada Familia ?", "options": ["Gothique", "Baroque", "Moderniste", "Renaissance"], "answer": "Moderniste"},
        {"id": 4, "question": "Quel est le plus haut bâtiment du monde ?", "options": ["Empire State Building", "Burj Khalifa", "Shanghai Tower", "Taipei 101"], "answer": "Burj Khalifa"},
        {"id": 5, "question": "Qui a conçu l'Opéra de Sydney ?", "options": ["Jørn Utzon", "Zaha Hadid", "Norman Foster", "Renzo Piano"], "answer": "Jørn Utzon"},
        {"id": 6, "question": "Quel monument égyptien est une des Sept Merveilles du monde antique ?", "options": ["Le Sphinx", "Les Pyramides de Gizeh", "Le Temple de Karnak", "Abou Simbel"], "answer": "Les Pyramides de Gizeh"},
    ]
}

QUIZ_CATEGORIES = {
    "sports": {
        "name": "Sports",
        "index": "sports",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2c2.5 4 2.5 8 0 12M2 12c4-2.5 8-2.5 12 0M12 22c-2.5-4-2.5-8 0-12M22 12c-4 2.5-8 2.5-12 0"/></svg>""",
        "color": "#FF6B6B",
        "description": "Testez vos connaissances sportives"
    },
    "chemistry": {
        "name": "Chimie",
        "index": "chemistry",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3v3M15 3v3M9 19c-1.5 1.5-2.5 3-2.5 4.5 0 1.38 1.12 2.5 2.5 2.5h6c1.38 0 2.5-1.12 2.5-2.5 0-1.5-1-3-2.5-4.5"/><path d="M14 6H10l-2 10h8l-2-10z"/><circle cx="12" cy="10" r="1" fill="currentColor"/><circle cx="10" cy="13" r="1" fill="currentColor"/><circle cx="14" cy="12" r="1" fill="currentColor"/></svg>""",
        "color": "#4ECDC4",
        "description": "Explorez les secrets de la chimie"
    },
    "economics": {
        "name": "Économie",
        "index": "economics",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>""",
        "color": "#FFD93D",
        "description": "Maîtrisez les concepts économiques"
    },
    "astronomy": {
        "name": "Astronomie",
        "index": "astronomy",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" fill="currentColor"/></svg>""",
        "color": "#A78BFA",
        "description": "Découvrez les mystères de l'univers"
    },
    "math": {
        "name": "Mathématiques",
        "index": "math",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 8h10M7 12h10M7 16h10"/></svg>""",
        "color": "#F472B6",
        "description": "Résolvez des problèmes mathématiques"
    },
    "architecture": {
        "name": "Architecture",
        "index": "architecture",
        "icon": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M4 18h16M6 18V9M10 18V9M14 18V9M18 18V9M12 2L4 9h16L12 2z"/></svg>""",
        "color": "#FB923C",
        "description": "Explorez les merveilles architecturales"
    }
}

