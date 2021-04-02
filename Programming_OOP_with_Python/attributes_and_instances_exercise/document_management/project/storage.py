class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.categories.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.categories.append(document)

    def edit_category(self, category_id: int, new_name: str):
        pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        pass

