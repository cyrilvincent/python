json = {
    "title": "Gitbook - Mode d'emploi",
    "author": "équipe Formateurs & Référents SIG",
    "description": "fake-document pour tester gitbook integré à gitlab, nottament les plugins",
    "license": "CC BY-NC-SA 3.0 FR",
    "language": "fr",
    "repo": "https://gitlab.com/formationsig/gitbook",
    "structure": {
        "readme": "README.md"
    },
    "plugins": [
        "advanced-emoji",
        "copy-code-button",
        "get-book",
        "embed-pdf",
        "local-pagefooter",
        "page-toc",
        "-lunr", "-search", "search-plus",
        "hints",
        "livereload"        
    ],
    "pluginsConfig": {
        "get-book": {
            "url": "https://gitlab.com/formationsig/gitbook/-/jobs/artifacts/master/raw/public/gitbook.pdf?job=pages",
            "label": "Télécharger le PDF"
        },
        "page-toc": {
            "selector": ".markdown-section h1, .markdown-section h2, .markdown-section h3, .markdown-section h4",
            "position": "before-first",
            "showByDefault": True
        }, 
        "local-pagefooter": {
            "islocal": True,
            "modify_label": "Inrap - équipe Formateurs & Référents SIG - document généré le ",
            "modify_format": "DD-MM-YYYY HH:mm:ss"
        }
    },
    "links": {
        "sidebar": {
            "Accueil - Formations SIG": "https://formationsig.gitlab.io/toc/"
        },
        "sharing": {
            "all": ["twitter", "facebook"],
            "facebook": False,
            "google": False,
            "twitter": False
        }
    },
    "pdf": {
        "margin": {
            "left": 56,
            "right": 99,
            "top": 56,
            "bottom": 56
        },
        "pageNumbers": False,
        "fontSize": 11,
        "fontFamily": "Roboto",
        "paperSize": "a4",
        "toc": True
    }
}
print(json["title"])
print(json["pdf"]["margin"]["right"])
print(json["plugins"][-1])