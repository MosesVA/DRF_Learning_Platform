from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, ContentSection
from sections.serializers.content_section_serializers import ContentSectionSectionSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    content_section_title = SerializerMethodField()

    def get_content_section_title(self, section):
        return ContentSectionSectionSerializer(ContentSection.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'content_section_title')
