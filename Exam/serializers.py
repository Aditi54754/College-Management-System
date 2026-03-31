from rest_framework import serializers
from Exam.models import Exam,Result

class ExamSerializer(serializers.ModelSerializer):
    class Meta :
        model = Exam
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta :
        model = Result
        fields = '__all__'
