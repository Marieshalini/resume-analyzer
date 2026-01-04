import re

def clean_text(text):
    text = text.lower()

    # 🔥 FIX broken words like: h t m l → html
    text = re.sub(r'h\s*t\s*m\s*l', 'html', text)
    text = re.sub(r'c\s*s\s*s', 'css', text)
    text = re.sub(r'j\s*a\s*v\s*a\s*s\s*c\s*r\s*i\s*p\s*t', 'javascript', text)

    # common fixes
    text = re.sub(r'g\s*i\s*t\s*h\s*u\s*b', 'github', text)
    text = re.sub(r'r\s*e\s*s\s*t', 'rest', text)

    # clean remaining noise
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
