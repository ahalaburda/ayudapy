from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer, ModelSerializer

from .models import HelpRequest


class HelpRequestSerializer(GeoModelSerializer):
    class Meta:
        model = HelpRequest
        fields = ['id', 'title', 'message', 'name', 'phone', 'address', 'city', 'location', 'picture', 'active', 'added']
        geo_field = 'location'


class HelpRequestGeoJSONSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HelpRequest
        fields = ['pk', 'title', 'message', 'name']
        geo_field = 'location'

class HelpRequestSearchSerializer(ModelSerializer):
	class Meta:
		model = HelpRequest
		fields = ['id', 'title', 'message', 'name', 'phone', 'address', 'city', 'location', 'picture', 'active', 'added']