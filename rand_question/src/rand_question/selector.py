"""Random selection helpers."""

from __future__ import annotations

import random

from .data import name_list, question_list


def random_selection(n_list=None, q_list=None):
    """Return a random name and question pair."""
    names = n_list if n_list is not None else name_list
    questions = q_list if q_list is not None else question_list
    chosen_name = random.choice(names)
    chosen_question = random.choice(questions)
    return chosen_name, chosen_question


def demo_selection():
    """Generate the original three paired selections from the notebook."""
    random.seed(42)
    selections = []
    for _ in range(3):
        selections.append(random_selection())
    return selections
