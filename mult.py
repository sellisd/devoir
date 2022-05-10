#!/usr/bin/env python3
import random
from colorama import Fore, Style, init

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
wrong = ['Faux',
         'Mauvaise réponse']
max_questions = 10
success_rate = 0
for i in range(max_questions):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    answer = input(f"{a} x {b} = ")
    if a*b == int(answer):
        success_rate += 1
        print(f"{Fore.GREEN}{random.choice(correct)}!{Fore.RESET}")
    else:
        print(f"{Fore.RED}{random.choice(wrong)}{Fore.RESET} La bonne réponse est: {a*b}")
print("FIN")
print(f"{random.choice(correct)}! {success_rate/max_questions*100} %")