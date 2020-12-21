"""
Function called by views.py when GrandPy Bot answers a question.
Returns a random message depending on the question is valid or not.
"""

import random

base_msg = "N'oublie pas que je suis un robot, je ne comprends donc pas tout. Tu peux en savoir plus en consultant la documentation disponible sur le repo GitHub du projet. Tu trouveras le lien dans le bas de la page."

error_msg = [
    "Désolé mon grand, mais je ne comprends pas ta demande... ",
    "Ahahah.. Il s'agit sûrement d'une de ces phrases de 'jeunes'. ",
    "Mmmmh... Je connais beaucoup de choses mais pas tout. Je n'ai peut-être simplement pas compris ta demande ? ",
    "Mais qu'est ce que c'est que ce charabia... "
]

valid_msg = [
    "Ah oui, je vois tout à fait ce dont tu veux parler. L'adresse est ",
    "Je me souviens avoir déjà visité cet endroit il y a quelques temps. Il se situe au ",
    "Mmmmmhhh... Oui cela me reviens très bien. Si je ne dis pas de bêtises (et je n'en dis presque jamais) l'adresse est ",
]


def get_answer(state):
    # Defines if the question is "valid" or not
    if state == 'error':
        lst = error_msg
    elif state == 'valid':
        lst = valid_msg

    # Create random answer according to state
    i = random.randrange(len(lst)-1)
    if state == 'error':
        msg = lst[i] + base_msg
    elif state == 'valid':
        msg = lst[i]

    return msg
