from pathlib import Path

# Root folder
ROOT = Path("CONSULTANAMIKA")

# Folder structure
folders = [
    ROOT,
    ROOT / "articles",
    ROOT / "field-notes",
    ROOT / "case-reflections",
    ROOT / "resume",
    ROOT / "css",
    ROOT / "js",
    ROOT / "images",
    ROOT / "images" / "articles",
    ROOT / "images" / "camps",
    ROOT / "images" / "cases",
    ROOT / "data",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Basic HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{css_path}">
</head>

<body>

<nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
    <div class="container">
        <a class="navbar-brand" href="{home_link}">
            Dr. Anamika Kumari
        </a>
    </div>
</nav>

<div class="container py-5">

    <h1>{title}</h1>

    <p>
        Placeholder content for {title}.
    </p>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
"""

files = {
    ROOT / "index.html": ("Home", "css/style.css", "index.html"),
    ROOT / "about.html": ("About", "css/style.css", "index.html"),
    ROOT / "contact.html": ("Contact", "css/style.css", "index.html"),

    ROOT / "articles" / "index.html":
        ("Articles", "../css/style.css", "../index.html"),

    ROOT / "articles" / "diabetes-awareness.html":
        ("Diabetes Awareness", "../css/style.css", "../index.html"),

    ROOT / "articles" / "hypertension-silent-risk.html":
        ("Hypertension Silent Risk", "../css/style.css", "../index.html"),

    ROOT / "articles" / "preventive-healthcare.html":
        ("Preventive Healthcare", "../css/style.css", "../index.html"),

    ROOT / "field-notes" / "index.html":
        ("Field Notes", "../css/style.css", "../index.html"),

    ROOT / "field-notes" / "rural-health-camp-2025.html":
        ("Rural Health Camp 2025", "../css/style.css", "../index.html"),

    ROOT / "field-notes" / "community-screening-observations.html":
        ("Community Screening Observations", "../css/style.css", "../index.html"),

    ROOT / "case-reflections" / "index.html":
        ("Case Reflections", "../css/style.css", "../index.html"),

    ROOT / "case-reflections" / "lessons-from-diabetes-management.html":
        ("Lessons From Diabetes Management", "../css/style.css", "../index.html"),

    ROOT / "case-reflections" / "importance-of-follow-up.html":
        ("Importance Of Follow-Up", "../css/style.css", "../index.html"),
}

for filepath, (title, css_path, home_link) in files.items():
    filepath.write_text(
        html_template.format(
            title=title,
            css_path=css_path,
            home_link=home_link
        ),
        encoding="utf-8"
    )

# style.css
(ROOT / "css" / "style.css").write_text(
"""
body {
    font-family: 'Segoe UI', sans-serif;
    background: #f8fafc;
}
""",
    encoding="utf-8"
)

# main.js
(ROOT / "js" / "main.js").write_text(
"""
console.log("ConsultAnamika loaded.");
""",
    encoding="utf-8"
)

# articles database placeholder
(ROOT / "data" / "articles.json").write_text(
"""
{
    "articles": []
}
""",
    encoding="utf-8"
)

# CNAME placeholder
(ROOT / "CNAME").write_text(
"consultanamika.com",
    encoding="utf-8"
)

print("Website structure created successfully.")
