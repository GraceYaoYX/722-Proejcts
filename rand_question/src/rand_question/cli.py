"""Command-line interface for the random question selector."""

from __future__ import annotations

from .data import name_list, question_list
from .selector import random_selection


def main() -> None:
    """Run the interactive prompt loop."""
    response = input("Press 'Y' to continue, any other key to exit:")
    print(f"User response is: {response}")

    while True:
        response = input("Press 'Y' to continue, any other key to exit:")
        if response.upper() != "Y":
            break

        chosen_name, chosen_question = random_selection(name_list, question_list)
        print(f"{chosen_name}, please answer: {chosen_question}")


if __name__ == "__main__":
    main()
