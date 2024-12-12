from chromatinLoops.serializers import ChromLoopsSerializer
from rest_framework.response import Response
from chromatinLoops.models import ChromLoops, File, CellTypeSummary
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.http import HttpResponse
from rest_framework.response import Response
import csv
from rest_framework.views import APIView

class ChromatinInteractionsExportView(APIView):
    serializer_class = ChromLoopsSerializer

    def get_queryset(self):
        print('enter ChromatinInteractionsExportView')
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

        return records

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        
        queryset = self.get_queryset()
        serializer = ChromLoopsSerializer(queryset, many=True)
        # header = ChromLoopsSerializer.Meta.fields
        header = [
            'chrom1',
            'start1',
            'end1',
            'chrom2',
            'start2',
            'end2',
            'counts',
            'anchor1',
            'anchor2',
            'file_id',
            'id'
        ]
        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)
        
        return response