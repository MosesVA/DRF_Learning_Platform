from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, ContentSection
from sections.permissions import IsModerator
from sections.serializers.section_serializers import SectionListSerializer, SectionSerializer
from sections.serializers.content_section_serializers import ContentSectionListSerializer, ContentSectionSerializer
from sections.paginators import SectionPaginator, ContentSectionPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentSectionAPIView(ListAPIView):
    serializer_class = ContentSectionListSerializer
    queryset = ContentSection.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContentSectionPaginator


class ContentSectionCreateAPIView(CreateAPIView):
    serializer_class = ContentSectionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentSectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSectionSerializer
    queryset = ContentSection.objects.all()
    permission_classes = [IsAuthenticated]


class ContentSectionUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSectionSerializer
    queryset = ContentSection.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentSectionDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSectionSerializer
    queryset = ContentSection.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]
