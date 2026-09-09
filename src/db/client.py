"""
MongoDB Database Client Module
"""

# pyrefly: ignore [missing-import]
from pymongo import MongoClient

from src.config import Config


class DatabaseClient:
    """
    Client for interacting with the MongoDB database containing professional data.
    """

    def __init__(self):
        # We only connect to the client when needed, or keep a persistent connection
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.DB_NAME]

    def get_professional_data(self):
        """
        Skeleton for fetching professional data.
        In the future, this will fetch directly from self.db.professionals.find_one({...})
        using the schema defined in ai_context.md.
        """
        print("Fetching data for professional from MongoDB (skeleton)...")
        return {
            "name": "Jane Doe",
            "skills": [
                {
                    "category": "hard_skill",
                    "subCategory": "Languages",
                    "name": {"en": "C++"},
                    "proficiencyLevel": 5,
                },
                {
                    "category": "hard_skill",
                    "subCategory": "Frameworks",
                    "name": {"en": "Machine Learning"},
                    "proficiencyLevel": 4,
                },
            ],
            "experiences": [
                {
                    "title": {"en": "Software Engineer"},
                    "company": {"en": "Tech Corp"},
                    "location": {"en": "Berlin, Germany"},
                    "timeline": {"startDate": "2020-01", "endDate": None},
                    "description": {
                        "en": ["Developed C++ ML models", "Optimized PyTorch pipelines"]
                    },
                }
            ],
        }
