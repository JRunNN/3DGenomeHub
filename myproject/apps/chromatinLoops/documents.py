# documents.py

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl.fields import NestedField

from .models import ChromLoops, CellTypeSummary, Assay, File


# 

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Configure how the index should be refreshed after an update.
@registry.register_document
class ChromLoopsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'chromloops'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = ChromLoops # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'chrom1',
            'start1',
            'end1',
            'chrom2',
            'start2',
            'end2',
            'anchor1',
            'anchor2',
            'file_id',
            'counts'
        ]
        #sticsearch documentation for supported options:
        # https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
        # This per-Document setting overrides settings.ELASTICSEARCH_DSL_AUTO_REFRESH.
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000


@registry.register_document
class CellTypeSummaryDocument(Document):
    assays = fields.NestedField(
                            properties={
                                'name': fields.TextField()
                            })
    
    class Index:
        # Name of the Elasticsearch index
        name = 'celltypesummary'

    class Django:
        model = CellTypeSummary # The model associated with this Document
        related_models = [Assay]
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'cell_id',
            'disease_status',
            'body_site',
            # 'assays'
        ]

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        if isinstance(related_instance, Assay):
            return related_instance.name.all()
        



@registry.register_document
class FileDocument(Document):
    cell_type_summary = fields.NestedField(properties={
        'cell_id': fields.TextField(),
        'cell_type': fields.TextField(),
        'disease_status': fields.TextField(),
        'body_site': fields.TextField(),
        'factor': fields.TextField(),
    })

    def replace_spaces_commas(s):
        s = s.replace(',', ' ')
        s = ' '.join(s.split())
        s = s.replace(' ', '-')
        return s

    def prepare_cell_id(self, instance):
        return replace_spaces_commas(instance.cell_type_summary.cell_id)

    class Index:
        name = 'file'
        # settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    # Assay = fields.NestedField(properties={
    #     'name': fields.TextField()
    # })    

    class Django:
        model = File  # The model associated with this Document
        related_models = [CellTypeSummary]
        fields = [
            'data_id',
            'format',
            'assay',
        ]

    def get_queryset(self):
        """Not mandatory but useful for overriding the default queryset"""
        return super().get_queryset().select_related('cell_type_summary')


    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, CellTypeSummary):
            print('2222222222')
            return related_instance.files.all()

    #   # Define the field's preparation method
    # def prepare_cell_type_summary(self, instance):
    #     # This will prepare the nested 'cell_type_summary' field for indexing
    #     return {
    #         'cell_id': instance.cell_type_summary.cell_id,
    #         'cell_type': instance.cell_type_summary.get_cell_type_display(),
    #         'disease_status': instance.cell_type_summary.get_disease_status_display(),
    #         'body_site': instance.cell_type_summary.get_body_site_display(),
    #         'factor': instance.cell_type_summary.get_factor_display(),
    #     }