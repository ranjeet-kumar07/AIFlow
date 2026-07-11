from pathlib import Path


class PromptRepository:

    ROOT = (
        Path(__file__)
        .resolve()
        .parents[2]
    )

    PROMPTS_DIR = ROOT / "prompts"

    @classmethod
    def load(
        cls,
        workflow: str,
        filename: str
    ) -> str:

        path = (
            cls.PROMPTS_DIR
            / workflow
            / filename
        )

        return path.read_text(
            encoding="utf-8"
        )