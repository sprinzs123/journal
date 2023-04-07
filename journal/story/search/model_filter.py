from ..models import Entry


# accepts filter object that dectate how to filter data
# does and filter
class Filter:
    def __init__(self, filter_param):
        self.filter_param = filter_param
        self.data = Entry.objects.all()
        self.filtered_data = self.filter_data()

    def get_data(self):

        return self.filtered_data

    def filter_data(self):
        #self.date_filter()
        #self.tags_filter()
        #self.tags_filter()
        self.title_filter()
        return self.data



    def date_filter(self):
        if self.filter_param["start_date"] != "":
            start_date = self.filter_param["start_date"]
            end_date = self.filter_param["start_date"]

    def tags_filter(self):
        if self.filter_param["tags"] != "":
            self.data.filter(tags__contains=self.filter_param["text"])

    def text_filter(self):
        if self.filter_param["text"] != "":
            self.data =self.data.filter(text__contains=self.filter_param["text"])

    def title_filter(self):
        if self.filter_param["text"] != "":
            self.data.filter(title__contains="rei")