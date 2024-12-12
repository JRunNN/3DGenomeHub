from django.shortcuts import render
from .serializers import ChromLoopsCancerSerializer, NonCodingElementSVSerializer, NonCodingElementSNVSerializer
from rest_framework import generics
from .pagination import MyPageNumberPagination
from .models import ChromLoopsCancer, NonCodingElementSNV, NonCodingElementSV
from django.db.models import Q as DjangoQ

# Create your views here.
class ChromLoopsCancerListView(generics.ListAPIView):
    # search_document = ChromLoopsDocument
    pagination_class = MyPageNumberPagination
    serializer_class = ChromLoopsCancerSerializer

    def get_queryset(self):
        print('enter ChromLoopsCancerListView')
        page = self.request.query_params.get('page', 1)
        pagesize = self.request.query_params.get('pagesize', 10)
        cancer_id_param = self.request.query_params.get('cancerId', '')

        records = ChromLoopsCancer.objects.filter(body_site = cancer_id_param)

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
            records = records.filter(DjangoQ(anchor1_genes__icontains=gene_name) | DjangoQ(anchor2_genes__icontains=gene_name))
        
        return records



class NonCodingElementSNVListView(generics.ListAPIView):
     # search_document = ChromLoopsDocument
    pagination_class = MyPageNumberPagination
    serializer_class = NonCodingElementSNVSerializer

    def get_queryset(self):
        print('enter ChromLoopsCancerListView')
        page = self.request.query_params.get('page', 1)
        pagesize = self.request.query_params.get('pagesize', 10)
        cancer_id_param = self.request.query_params.get('cancerId', '')

        records = NonCodingElementSNV.objects.all()

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
            records = records.filter(DjangoQ(anchor1_genes__icontains=gene_name) | DjangoQ(anchor2_genes__icontains=gene_name))
        
        return records


class NonCodingElementSVListView(generics.ListAPIView):
         # search_document = ChromLoopsDocument
    pagination_class = MyPageNumberPagination
    serializer_class = NonCodingElementSVSerializer

    def get_queryset(self):
        print('enter NonCodingElementSVListView')
        page = self.request.query_params.get('page', 1)
        pagesize = self.request.query_params.get('pagesize', 10)
        cancer_id_param = self.request.query_params.get('cancerId', '')

        records = NonCodingElementSV.objects.all()

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
            records = records.filter(DjangoQ(anchor1_genes__icontains=gene_name) | DjangoQ(anchor2_genes__icontains=gene_name))
        
        return records