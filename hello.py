#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a 
mensagem correspodente.

Como usar:

Tenha a variável LANG devidamente configurada no ambiente exemplo:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Richelieu Valentin"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo",
    "fr_FR": "Bonjour, Monde",
}
   
print(msg[current_language])