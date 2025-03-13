from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer, token_filter

from .models import Anime

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

# ----------------- Для русского языка -----------------

russian_stop = token_filter(
    'russian_stop',
    type="stop",
    stopwords="_russian_",
)

russian_keywords = token_filter(
    'russian_keywords',
    type="keyword_marker",
    keywords="пример",
)

russian_stemmer = token_filter(
    'russian_stemmer',
    type="stemmer",
    language="russian",
)

# ----------------------------------


# ----------------- Для английского языка -----------------

english_stop = token_filter(
    'english_stop',
    type="stop",
    stopwords="_english_",
)

english_keywords = token_filter(
    'english_keywords',
    type="keyword_marker",
    keywords="example",
)

english_stemmer = token_filter(
    'english_stemmer',
    type="stemmer",
    language="english",
)

english_possessive_stemmer = token_filter(
    'english_stemmer',
    type="stemmer",
    language="possessive_english",
)

# ----------------------------------


My_analyzer = analyzer(
    'russian',
    tokenizer="standard",
    filter=[
        english_possessive_stemmer,
        "lowercase",
        english_stop,
        english_keywords,
        english_stemmer,
        russian_stop,
        russian_keywords,
        russian_stemmer,
    ],
)


@INDEX.doc_type
class AnimeDocument(Document):

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=My_analyzer,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    additional_name = fields.TextField(
        analyzer=My_analyzer,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    # short_description = fields.TextField(
    #     analyzer=My_analyzer,
    #     fields={
    #         'raw': fields.TextField(analyzer='keyword'),
    #     }
    # )
    #
    # large_description = fields.TextField(
    #     analyzer=My_analyzer,
    #     fields={
    #         'raw': fields.TextField(analyzer='keyword'),
    #     }
    # )

    review = fields.TextField(
        analyzer=My_analyzer,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    description = fields.TextField(
        analyzer=My_analyzer,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    class Meta:
        model = Anime

    class Django:
        model = Anime