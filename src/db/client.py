from pymongo import MongoClient
from src.config import Config

class DatabaseClient:
    def __init__(self):
        # We only connect to the client when needed, or keep a persistent connection
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.DB_NAME]
    
    def get_professional_data(self, professional_id=None):
        """
        Skeleton for fetching professional data.
        In the future, this will fetch directly from self.db.professionals.find_one({...})
        using the schema defined in ai_context.md.
        """
        print(f"Fetching data for professional from MongoDB (skeleton)...")
        return {
            "name": "Jane Doe",
            "skills": [
                {"name": {"en": "C++"}, "category": "hard_skill"},
                {"name": {"en": "Machine Learning"}, "category": "hard_skill"}
            ],
            "experiences": [
                {
                    "title": {"en": "Software Engineer"},
                    "description": {"en": ["Developed C++ ML models", "Optimized PyTorch pipelines"]}
                }
            ]
        }
