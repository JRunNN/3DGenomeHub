from .models import ChromLoopsCancer, NonCodingElementSV, NonCodingElementSNV
from rest_framework import serializers

# ChromLoopsCancer serializer
class ChromLoopsCancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChromLoopsCancer
        fields = '__all__'

# NonCodingElementSV serializer
class NonCodingElementSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonCodingElementSV
        fields = '__all__'

# NonCodingElementSV serializer
class NonCodingElementSNVSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonCodingElementSNV
        fields = '__all__'