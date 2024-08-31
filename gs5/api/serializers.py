from rest_framework import serializers
from .models import Student
def stsrt_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name should start with s')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[stsrt_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    def validate_roll(self, roll):
        if roll>=200:
            raise serializers.ValidationError('Seats Full')
        return roll
    
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'kim' and ct.lower() != 'seoul':
            raise serializers.ValidationError('City must be seoul')
        return data
            
    
   