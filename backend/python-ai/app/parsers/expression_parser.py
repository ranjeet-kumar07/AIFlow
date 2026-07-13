import re


class ExpressionParser:

    @staticmethod
    def extract(prompt: str) -> str:

        prompt = prompt.lower()

        prompt = (
            prompt
            .replace("calculate", "")
            .replace("what is", "")
            .replace("compute", "")
            .replace("evaluate", "")
            .strip()
        )

        match = re.search(
            r"[0-9+\-*/(). ]+",
            prompt
        )

        if not match:
            raise ValueError(
                "No mathematical expression found."
            )

        return match.group().strip()