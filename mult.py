#!/usr/bin/env python3
import random
import re

from colorama import Fore

correct = ['Bravo',
           'Magnifique',
           'Merveilleux',
           'Formidable',
           'Génial',
           'Bien',
           'Épatant',
           'Wow',
           'Extraordinaire',
           'Sensationnel',
           'Exceptionnel',
           'Ingénieux',
           'Parfait',
           'Fantastique',
           'Admirable',
           'Époustouflant',
           'Fabuleux',
           'Félicitations',
           'Tu as réussi',
           'Tu as fait un excellent travail',
           'Bon travail',
           'Je suis ravie de te voir travailler ainsi',
           'Bon travail',
           'Bien pensé'
           ]
max_questions = 10
success_rate = 0
for i in range(max_questions):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    answer = 0
    question_number = 0
    while a*b != answer:
        question_number += 1
        answer = input(f"{question_number}. {a} x {b} = ")
        if answer == 'q':
            break
        if re.match('^\d+$', answer):
            answer = int(answer)
        else:
            print('Entre q pour quitter')
    print(f"{Fore.GREEN}{random.choice(correct)}!{Fore.RESET}")
