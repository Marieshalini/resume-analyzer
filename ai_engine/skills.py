import re

MASTER_SKILLS = [
    "python", "java", "c", "c++", "sql", "mysql", "postgresql",
    "machine learning", "deep learning", "data analysis",
    "pandas", "numpy", "scikit-learn",
    "flask", "django",
    "html", "css", "javascript",
    "git", "github",
    "linux", "api", "rest"
]

SKILL_SYNONYMS = {
    "python": ["python", "python3"],
    "java": ["java"],                     # ⚠️ strict
    "c": ["c"],                           # ⚠️ strict
    "c++": ["c++", "cpp"],
    "sql": ["sql"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "data analysis": ["data analysis", "analytics"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "flask": ["flask"],
    "django": ["django"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "git": ["git", "github"],
    "linux": ["linux"],
    "api": ["api", "rest", "rest api"]
}

# skills that MUST be matched as whole words
STRICT_TOKENS = {"java", "c", "ml", "dl"}

def extract_skills(text):
    text = text.lower()
    found = set()

    for skill, patterns in SKILL_SYNONYMS.items():
        for p in patterns:
            if p in STRICT_TOKENS:
                # word-boundary match
                if re.search(r'\b' + re.escape(p) + r'\b', text):
                    found.add(skill)
                    break
            else:
                # safe substring match
                if p in text:
                    found.add(skill)
                    break

    return sorted(found)
