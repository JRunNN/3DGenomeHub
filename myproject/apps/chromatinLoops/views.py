from django.shortcuts import render
from .serializers import ChromLoopsSerializer, CellTypeSummarySerializer, FileSerializer
from elasticsearch_dsl import Q, Search
from elasticsearch import Elasticsearch
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .documents import  CellTypeSummaryDocument, FileDocument, ChromLoopsDocument
from .models import ChromLoops, File, CellTypeSummary
import json
from django.http import JsonResponse
from .pagination import MyPageNumberPagination
from django.db.models import Q as DjangoQ
from django.db.models import Case, When, Value, Min, Max, F

class ChromatinInteractionsListView(generics.ListAPIView):
    # search_document = ChromLoopsDocument
    pagination_class = MyPageNumberPagination
    serializer_class = ChromLoopsSerializer

    def get_queryset(self):
        print('enter ChromatinInteractionsListView')
        page = self.request.query_params.get('page', 1)
        pagesize = self.request.query_params.get('pagesize', 10)
        cell_id_param = self.request.query_params.getlist('cellId', '')

        # start = (int(page)-1)*int(pagesize)
        # end = start + int(pagesize)

        if (len(cell_id_param) == 1):
            cell_id_param = cell_id_param[0]
            cell_type_summary = CellTypeSummary.objects.get(cell_id=str(cell_id_param))
            related_files = File.objects.filter(cell_type_summary=cell_type_summary)
        else:
            # Get related file_ids from SQL database
            cell_type_summary = CellTypeSummary.objects.filter(cell_id__in=cell_id_param)
            cell_type_ids = cell_type_summary.values_list('cell_id', flat=True)
            related_files = File.objects.filter(cell_type_summary__in = cell_type_ids)
        
        file_ids = related_files.values_list('data_id', flat=True)
        records = ChromLoops.objects.filter(file_id__in=file_ids)

        # Retrieve 'chrom', 'start', and 'end' from request parameters
        chrom = self.request.query_params.get('chrom', None)
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)

        # Convert 'start' and 'end' to integers if they are not None
        if start is not None and end is not None:
            start = int(start)
            end = int(end)
            # Filter records based on the conditions
            records = records.filter(DjangoQ(chrom1=chrom) & DjangoQ(chrom2=chrom))
            # records = records.annotate(
            #     start_cond=Case(
            #         When(start1__gt=F('start2'), then=F('start1')),
            #         default=F('start2'),
            #         output_field=models.IntegerField(),
            #     ),
            #     end_cond=Case(
            #         When(start1__gt=F('start2'), then=F('end2')),
            #         default=F('end1'),
            #         output_field=models.IntegerField(),
            #     ),
            # )
            records = records.filter(DjangoQ(start1__gt=start) & DjangoQ(end2__lt=end))

        gene_name = self.request.query_params.get('geneName', None)
        if gene_name is not None:
            # Filter records based on the `geneName`
            records = records.filter(DjangoQ(anchor1__icontains=gene_name) | DjangoQ(anchor2__icontains=gene_name))
        
        return records



class CellListTypeSummaryListView(APIView):
    search_document = CellTypeSummaryDocument
    print('enter CellListTypeSummaryListView')

    def get(self, request, format=None):
        diseaseStatus_param = request.query_params.getlist('diseaseStatus', '')
        # print('diseaseStatus_param',diseaseStatus_param)
        bodySite_param = request.query_params.getlist('bodySites', '')
        assays_param = request.query_params.getlist('assays', '')
        # assays_param = request.query_params.get('assays_param', '').split(',')
        cellId_param = request.query_params.get('cellId', '')
        page = request.query_params.get('page', '1')
        pagesize = request.query_params.get('pagesize', '10')
        includeInitialData = request.query_params.get('includeInitialData', 'false')
        start = (int(page)-1)*int(pagesize)
        end = start + int(pagesize)

        # Initialize the query
        # Initialize a 'match_all' query
        search_query = Q("match_all")
        if diseaseStatus_param:
            search_query &= Q('bool',
            should=[Q('match_phrase', disease_status=value) for value in diseaseStatus_param],
            minimum_should_match=1)
        if bodySite_param:
            search_query &= Q('bool',
            should=[Q('match_phrase', body_site=value) for value in bodySite_param],
            minimum_should_match=1)
        if assays_param:
            assays_param_string = ','.join(assays_param)
            for assay in assays_param:
                search_query &= Q('nested', path='assays', query=Q('match_phrase', assays__name=assay))
        print('search_query', search_query)
        if cellId_param:
            search_query &= Q('wildcard', cell_id=f'*{cellId_param}*')
            #search_query =  Q('term', cell_id=cellId_param)

        search = self.search_document.search().query(search_query)[start:end]
        response = search.execute()
        serializer = CellTypeSummarySerializer(search.to_queryset(), many=True)
        print('search_query',search_query, start, end)
        print('serializer.data', serializer.data)
        # print(response)
        if includeInitialData:
            initial_data_search = self.search_document.search()
            total_counts = initial_data_search.count()
            initial_data_search_out = initial_data_search[0:total_counts]
            initial_data_response = initial_data_search_out.execute()
            initial_data_serializer = CellTypeSummarySerializer(initial_data_search_out.to_queryset(), many=True)
            # print('includeInitialData:',initial_data_serializer.data)
            return Response({
                "initial_data": initial_data_serializer.data, 
                'data': serializer.data,
                'itemCount': response.hits.total.value,
                'from': start + 1,
                'to': end
            })
        else:
            print(serializer.data)
            return Response({
                'data': serializer.data,
                'itemCount': response.hits.total.value,
                'from': start + 1,
                'to': end
            })


class FilesListView(APIView):
    search_document = FileDocument
    print('enter FilesListView')

    def get(self, request, format=None):
        # diseaseStatus_param = request.query_params.getlist('diseaseStatus', '')
        # bodySites_param = request.query_params.getlist('bodySites', '')
        # assays_param = request.query_params.getlist('assay', '')
        # cellId_param = request.query_params.get('cellId', '')
        # format_param = request.query_params.getlist('format', '')
        page = request.query_params.get('page', '1')
        pagesize = request.query_params.get('pagesize', '10')
        includeInitialData = request.query_params.get('includeInitialData', 'false')
        start = (int(page)-1)*int(pagesize)
        end = start + int(pagesize)
        search_term = request.query_params.get('searchTerm', None)
        # search_query = Q("match_all")
        # Initialize the query
        # Initialize a 'match_all' query
        # Initialize the query with 'match_all' or 'multi_match' depending on the search term
        if search_term:
            # Use the 'multi_match' query to search across all fields in the document
            top_level_query = Q('multi_match', query=search_term, fields=[
                'data_id',
                'format',
                'assay',
                # Add any other top-level fields you want to search here
            ])

            # Construct a nested query for the nested 'cell_type_summary' fields
            nested_query = Q('nested', path='cell_type_summary', query=Q('multi_match', query=search_term, fields=[
            'cell_type_summary.cell_id',
            'cell_type_summary.cell_type',
            'cell_type_summary.disease_status',
            'cell_type_summary.body_site',
            'cell_type_summary.factor',
                # Add any other nested fields you want to search here
            ], type="best_fields"))

            # Combine the top-level and nested queries
            search_query = top_level_query | nested_query
            # search_query &= Q('multi_match', query=search_term, fields=['cell_type_summary__cell_id', 'format', 'assay'])  # Specify the fields to search over
        else:
             search_query = Q("match_all")

        # ... [the rest of your filtering logic] ...


        # search_query = Q("match_all")
        # print('1111111111111')    
        # # if diseaseStatus_param:
        # #     search_query &= Q('bool',
        # #     should=[Q('match_phrase', diseaseStatus=value) for value in diseaseStatus_param],
        # #     minimum_should_match=1)
        # # if bodySites_param:
        # #     search_query &= Q('bool',
        # #     should=[Q('match_phrase', bodySites=value) for value in bodySites_param],
        # #     minimum_should_match=1)
        # if assays_param:
        #     search_query &= Q('bool',
        #     should=[Q('match_phrase', assay=value) for value in assays_param],
        #     minimum_should_match=1)
        # if format_param:
        #     search_query &= Q('bool',
        #     should=[Q('match_phrase', format=value) for value in format_param],
        #     minimum_should_match=1)
        # if diseaseStatus_param:
        #     # diseaseStatus_param_string = ','.join(diseaseStatus_param)
        #     for diseaseStatus in diseaseStatus_param:
        #         search_query &= Q('nested', path='celltypesummary', query=Q('match_phrase', celltypesummary__diseaseStatus=diseaseStatus))
        # # # if diseaseStatus_param:
        #     diseaseStatus_param_string = ','.join(diseaseStatus_param)
        #     for diseaseStatus in assays_param:
        #         search_query &= Q('nested', path='celltypesummary', query=Q('match_phrase', celltypesummary__diseaseStatus=diseaseStatus))
        # if cellId_param:
        #     search_query &= Q('wildcard', cellId=f'*{cellId_param}*')

        # print('search query: ',str(search_query))
        search = self.search_document.search().query(search_query)[start:end]
        # for hit in search:
        #     print(hit.format)
        response = search.execute()
        serializer = FileSerializer(search.to_queryset(), many=True)
        # print('search_query', search_query)
        # print('serializer.data',serializer.data)
        # print('response', response)
        # print(response)
        if includeInitialData:
            initial_data_search = self.search_document.search()
            total_counts = initial_data_search.count()
            initial_data_search_out = initial_data_search[0:total_counts]
            initial_data_response = initial_data_search_out.execute()
            initial_data_serializer = FileSerializer(initial_data_search_out.to_queryset(), many=True)
            # print('includeInitialData:',initial_data_serializer.data)
            return Response({
                "initial_data": initial_data_serializer.data, 
                'data': serializer.data,
                'itemCount': response.hits.total.value,
                'from': start + 1,
                'to': end
            })
        else:
            # print(serializer.data)
            return Response({
                'data': serializer.data,
                'itemCount': response.hits.total.value,
                'from': start + 1,
                'to': end
            })


class BrowerFilesView(APIView):
    search_document = FileDocument
    print('enter BrowerFilesView')

    def get(self, request, format=None):
        cellId_param = request.query_params.get('cellId', '')
        # print(cellId_param)
        # Initialize the query
        # Initialize a 'match_all' query
        # search_query = Q("match_all")

        #if cellId_param:
        #     # Use 'term' query for exact match
        #     search_query =  Q('term', cellId=cellId_param)
        search_query = Q("nested", path="cell_type_summary", query=Q("match", cell_type_summary__cell_id=str(cellId_param)))       
        search = self.search_document.search().query(search_query)

        response = search.execute()
        serializer = FileSerializer(search.to_queryset(), many=True)       
         # print('search_query', search_query)
        # print('serializer.data',serializer.data)
        return Response({
            'data1': serializer.data,
            'cellId_param': cellId_param
        })