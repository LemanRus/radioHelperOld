import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'example title'},
    {'type': 'numeric',
     'title': 'Размер шрифта заголовков',
     'desc': 'Numeric description text',
     'section': 'font',
     'key': 'Размер шрифта заголовков'},
    {'type': 'numeric',
     'title': 'Размер шрифта текста',
     'desc': 'Numeric description text',
     'section': 'font',
     'key': 'Размер шрифта текста'},
])
