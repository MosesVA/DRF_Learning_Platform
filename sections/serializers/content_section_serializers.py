from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Section, ContentSection


class ContentSectionSerializer(ModelSerializer):
    class Meta:
        model = ContentSection
        fields = '__all__'


class ContentSectionSectionSerializer(ModelSerializer):
    class Meta:
        model = ContentSection
        fields = ('id', 'title')


class ContentSectionListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = ContentSection
        fields = ('id', 'section', 'title',)
