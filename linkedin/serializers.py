from rest_framework import serializers
from linkedin.models import Search, JobPost, Company, Tracking


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        exclude = ("user",)


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        exclude = ("user",)


