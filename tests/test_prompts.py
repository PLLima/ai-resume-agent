"""
Unit tests for prompt generators, strategy rules, and CLI parsing.
"""

import unittest

from src.prompts.coder_prompts import get_coder_prompt
from src.prompts.reasoner_prompts import get_reasoner_prompt
from src.prompts.strategy_rules import (
    COVER_LETTER_STRATEGY,
    GENERALIST_ONLINE_RESUME_STRATEGY,
    MASTER_CV_STRATEGY,
    NETWORKING_RESUME_STRATEGY,
    TARGETED_RESUME_STRATEGY,
    get_default_profile_photo,
    get_strategy_rules,
)


class TestStrategyRules(unittest.TestCase):
    """Test cases for strategy rule selection and photo asset defaults."""

    def test_strategy_routing(self):
        """Verify routing for all 5 document strategies and legacy aliases."""
        self.assertEqual(get_strategy_rules("master_cv"), MASTER_CV_STRATEGY.strip())
        self.assertEqual(
            get_strategy_rules("targeted_resume"), TARGETED_RESUME_STRATEGY.strip()
        )
        self.assertEqual(
            get_strategy_rules("networking_resume"),
            NETWORKING_RESUME_STRATEGY.strip(),
        )
        self.assertEqual(
            get_strategy_rules("generalist_online_resume"),
            GENERALIST_ONLINE_RESUME_STRATEGY.strip(),
        )
        self.assertEqual(
            get_strategy_rules("cover_letter", document_type="cover_letter"),
            COVER_LETTER_STRATEGY.strip(),
        )

        # Legacy aliases
        self.assertEqual(
            get_strategy_rules("online_ats"), TARGETED_RESUME_STRATEGY.strip()
        )
        self.assertEqual(
            get_strategy_rules("in_person"), NETWORKING_RESUME_STRATEGY.strip()
        )
        self.assertEqual(
            get_strategy_rules("general"), TARGETED_RESUME_STRATEGY.strip()
        )

    def test_default_profile_photo(self):
        """Verify default profile photo asset selection per strategy."""
        self.assertEqual(get_default_profile_photo("master_cv"), "ProfilePhoto.jpg")
        self.assertEqual(
            get_default_profile_photo("networking_resume"), "ProfilePhoto.jpg"
        )
        self.assertEqual(
            get_default_profile_photo("in_person"), "ProfilePhoto.jpg"
        )
        self.assertEqual(
            get_default_profile_photo("targeted_resume"), "ProfilePhoto_light.jpg"
        )
        self.assertEqual(
            get_default_profile_photo("generalist_online_resume"),
            "ProfilePhoto_light.jpg",
        )


class TestPromptGenerators(unittest.TestCase):
    """Test cases for Coder and Reasoner prompt construction."""

    def test_coder_prompt_defaults(self):
        """Verify coder prompt incorporates default profile photo and strategy."""
        prompt = get_coder_prompt(
            filtered_content="Candidate Content",
            document_type="resume",
            strategy="targeted_resume",
        )
        expected_photo_line = (
            "Profile Photo Asset (use ONLY when the active strategy requires a photo): "
            "ProfilePhoto_light.jpg"
        )
        self.assertIn(expected_photo_line, prompt)
        self.assertIn("Strategy Rules for Targeted Resumes (ATS/Online):", prompt)
        self.assertIn("Candidate Content", prompt)
        self.assertIn("LaTeX resume", prompt)

    def test_coder_prompt_custom_photo(self):
        """Verify coder prompt uses explicitly provided photo asset."""
        prompt = get_coder_prompt(
            filtered_content="Content",
            document_type="resume",
            strategy="targeted_resume",
            profile_photo_filename="ProfilePhoto.jpg",
        )
        expected_photo_line = (
            "Profile Photo Asset (use ONLY when the active strategy requires a photo): "
            "ProfilePhoto.jpg"
        )
        self.assertIn(expected_photo_line, prompt)

    def test_reasoner_prompt_cardinality(self):
        """Verify reasoner prompt contains blueprint directives including cardinality."""
        prompt = get_reasoner_prompt(
            job_description="Senior Linux Engineer",
            professional_data={"name": "Test User"},
            strategy="targeted_resume",
        )
        self.assertIn("Senior Linux Engineer", prompt)
        self.assertIn(
            "STRICTLY obey any `[TARGET MATCH]` cardinality caps and total entry limits",
            prompt,
        )
        self.assertIn("[TARGET MATCH]", prompt)
        self.assertIn("[SECONDARY ENTRY]", prompt)


if __name__ == "__main__":
    unittest.main()
