class BaseRepository:
    def __init__(self, collection):
        self.collection = collection

    def insert(self, item) -> str:
        return self.collection.insert_one(item).inserted_id

    def insert_all(self, items) -> str:
        return self.collection.insert_many(items)

    def find_all(self):
        results = self.collection.find({})
        return [r for r in results]

    def find_one(self, query={}):
        return self.collection.find_one(query)

    def find(self, query={}):
        results = self.collection.find(query)
        return [r for r in results]

    def update_one(self, query_elements, new_values):
        return self.collection.update_one(query_elements, {'$set': new_values})

    def delete_one(self, query):
        self.collection.delete_one(query)

    def drop(self):
        self.collection.drop()