from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

client=MongoClient(os.getenv('MONGODB_URI'))

db=client['cmb']
meals=db['meals']
messages=db['messages']
users=db['users']

class User:
    def __init__(self,number):
        self.number=number
    
    def create_user(self,goals,name,email):
        data={
            "name":name,
            "email":email,
            "pnumber":self.number,
            "goals":goals
        }
        users.insert_one(data)
    
    def add_meal(self, meal_name, calories, fat, protein, carbs, meal_type=None):
        meal_data = {
            "pnumber": self.number,
            "meal_name": meal_name,
            "calories": calories,
            "fat": fat,
            "protein": protein,
            "carbs": carbs,
            "meal_type": meal_type,
            "logged_at": datetime.now()
        }
        return meals.insert_one(meal_data)
    
    def edit_meal(self, meal_id, meal_name=None, calories=None, fat=None, protein=None, carbs=None, ingredients=None, meal_type=None):
        update_data = {}
        if meal_name is not None:
            update_data["meal_name"] = meal_name
        if calories is not None:
            update_data["calories"] = calories
        if fat is not None:
            update_data["fat"] = fat
        if protein is not None:
            update_data["protein"] = protein
        if carbs is not None:
            update_data["carbs"] = carbs
        if meal_type is not None:
            update_data["meal_type"] = meal_type
        
        return meals.update_one({"_id": meal_id}, {"$set": update_data})
    
    def log_message(self, content, from_number, sent_at=None):
        message_data = {
            "content": content,
            "from": from_number,
            "sent_at": sent_at
        }
        return messages.insert_one(message_data)
    
    def get_last_messages(self, limit=5):
        return list(messages.find().sort("sent_at", -1).limit(limit))
    
    def get_user(self):
        return users.find_one({"pnumber": self.number})
    
    def update_user(self, name=None, email=None, goals=None):
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if email is not None:
            update_data["email"] = email
        if goals is not None:
            update_data["goals"] = goals
        
        return users.update_one({"pnumber": self.number}, {"$set": update_data})
    
    def delete_user(self):
        return users.delete_one({"pnumber": self.number})
    
    def get_meals(self):
        return list(meals.find({"pnumber": self.number}))
    
    def delete_meal(self, meal_id):
        return meals.delete_one({"_id": meal_id, "pnumber": self.number})
