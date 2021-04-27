class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += str(doc)
        return result

    @staticmethod
    def find_id_in_list_with_objects_and_return_object(my_list_of_objects, id_):
        return [index for index, obj in enumerate(my_list_of_objects) if obj.id == id_][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.categories, category_id)
        self.categories[obj_index].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.topics, topic_id)
        self.topics[obj_index].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.documents, document_id)
        self.documents[obj_index].file_name = new_file_name

    def delete_category(self, category_id):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.categories, category_id)
        self.categories.pop(obj_index)

    def delete_topic(self, topic_id):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.topics, topic_id)
        self.topics.pop(obj_index)

    def delete_document(self, document_id):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.documents, document_id)
        self.documents.pop(obj_index)

    def get_document(self, document_id):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.documents, document_id)
        return self.documents[obj_index]
