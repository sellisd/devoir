#!/usr/bin/env python3
import random
import re

import click
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


def ask(question_number, a, b, type) -> bool:
    if type == 'multiplication':
        answer = input(f"{question_number}. {a} x {b} = ")
        result = a*b
    elif type == 'addition':
        answer = input(f"{question_number}. {a} + {b} = ")
        result = a+b
    elif type == 'soustraction':
        if a < b:
            a, b = b, a
        answer = input(f"{question_number}. {a} - {b} = ")
        result = a-b
    if answer == 'q':
        exit(0)
    if re.match('^\d+$', answer):
        answer = int(answer)
    else:
        print('Entré q pour quitter')
    if result == answer:
        return True
    else:
        return False


@click.command()
@click.option('--max_questions', default=10, help='Number of questions to ask.')
@click.option('--min', default=2, help='Smallest number.')
@click.option('--max', default=10, help='Largest number.')
@click.option('--question-type', type=click.Choice(['multiplication', 'addition', 'soustraction'], case_sensitive=False), default='addition')
def questions(max_questions, min, max, question_type):
    i = 1
    while i <= max_questions:
        a = random.randint(min, max)
        b = random.randint(min, max)

        success = False
        while not success:
            success = ask(f"{i}/{max_questions}", a, b, question_type)
        i += 1
        print(f"{Fore.GREEN}{random.choice(correct)}!{Fore.RESET}")


if __name__ == '__main__':
    questions()
