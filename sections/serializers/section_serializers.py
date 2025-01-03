from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serializers.content_serializers import ContentSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    content_section_title = SerializerMethodField()

    def get_content_section_title(self, section):
        return ContentSerializer(Content.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'content_section_title')
