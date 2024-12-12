from .models import ChromLoops, CellTypeSummary, File
from rest_framework import serializers

# chromatin interaction serializer
class ChromLoopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChromLoops
        fields = '__all__'

# cellType summary serializer]
class CellTypeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CellTypeSummary
        fields = '__all__'

# cellType summary serializer]
class FileSerializer(serializers.ModelSerializer):
        # Nest the CellTypeSummarySerializer
    cell_type_summary = CellTypeSummarySerializer(read_only=True)
    
    class Meta:
        model = File
        fields = '__all__'