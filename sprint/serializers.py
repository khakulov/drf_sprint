from rest_framework import serializers


class ProgrammerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    from_pdx = serializers.BooleanField(default=False)
    eats_meat = serializers.BooleanField(default=True)
    email = serializers.EmailField()
