"""
MongoDB Database Client Module
"""

from typing import Any

from bson.objectid import ObjectId
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

    def get_professional_data(
        self, professional_id: str | None = None
    ) -> dict[str, Any] | None:
        """
        Fetches professional data from the MongoDB database.
        If professional_id is provided, fetches that specific document.
        Otherwise, fetches the first available professional document.
        """
        print("Fetching data for professional from MongoDB...")
        if professional_id:
            return self.db.professionals.find_one({"_id": ObjectId(professional_id)})
        return self.db.professionals.find_one()

    def save_resume(self, resume_data: dict[str, Any]) -> str:
        """
        Saves a generated resume record to the database.
        Returns the stringified ObjectId of the inserted document.
        """
        result = self.db.resumes.insert_one(resume_data)
        return str(result.inserted_id)

    def save_cover_letter(self, cover_letter_data: dict[str, Any]) -> str:
        """
        Saves a generated cover letter record to the database.
        Returns the stringified ObjectId of the inserted document.
        """
        result = self.db.coverLetters.insert_one(cover_letter_data)
        return str(result.inserted_id)
