class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        pass

    @staticmethod
    def find_id_in_list_with_objects_and_return_object(my_list_of_objects, id_):
        return [index for index, obj in enumerate(my_list_of_objects) if obj.id == id_][0]

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
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.categories, category_id)
        self.categories[obj_index].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        obj_index = self.find_id_in_list_with_objects_and_return_object(self.topics, topic_id)
        self.topics[obj_index].name = new_topic
        self.topics[obj_index].storage_folder = new_storage_folder


    def edit_document(self, document_id: int, new_file_name: str):
        pass

    def delete_category(self, category_id):
        pass

    def delete_topic(self, topic_id):
        pass

    def delete_document(self, document_id):
        pass

    def get_document(self, document_id):
        pass
