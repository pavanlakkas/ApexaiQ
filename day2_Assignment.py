import re


class CreditCardValidator:
    """
    A class to validate credit card numbers based on ABCD Bank's specifications.

    Validation Rules:
    1. Must start with 4, 5, or 6
    2. Must be exactly 16 digits
    3. Can be divided into groups of 4 separated by hyphens
    4. Must not contain any other separators
    5. Must not have 4 or more consecutive repeated digits
    """

    def __init__(self):
        # Compile regex patterns for better performance
        self.structure_pattern = re.compile(
            r'^([4-6]\d{3}-\d{4}-\d{4}-\d{4}|[4-6]\d{15})$'
        )
        self.consecutive_pattern = re.compile(r'(\d)\1{3}')

    def validate(self, card_number: str) -> bool:

        # Main validation method that combines all checks.

        return all([
            self._check_structure(card_number),
            self._check_consecutive_digits(card_number)
        ])

    def _check_structure(self, card_number: str) -> bool:
        """
        Validates the basic structure of the credit card number.

        1. Checks starting digit
        2. Validates length and hyphen placement
        3. Ensures only digits and valid hyphens

        """
        return bool(self.structure_pattern.match(card_number))

    def _check_consecutive_digits(self, card_number: str) -> bool:

        # Remove hyphens and check for consecutive digits
        clean_number = card_number.replace('-', '')
        return not bool(self.consecutive_pattern.search(clean_number))


def main():
    """
    Main function to handle input/output and process validation.
    """
    n = int(input())
    validator = CreditCardValidator()

    for _ in range(n):
        card = input().strip()
        if validator.validate(card):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()