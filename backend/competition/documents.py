# backend/documents.py
from elasticsearch_dsl import Document, Text, Keyword, Date
from .models import Competition


class CompetitionDocument(Document):
    name = Text()
    description = Text()
    types = Keyword()
    levels = Keyword()
    website = Keyword()
    other_info = Text()
    timeline = Date()

    class Index:
        name = 'competitions'

    def save(self, **kwargs):
        self.meta.id = self.instance.id
        super().save(**kwargs)
