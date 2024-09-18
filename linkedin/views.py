from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from linkedin.models import Search, JobPost, Company, Tracking
from linkedin.serializers import SearchSerializer, JobPostSerializer, CompanySerializer, TrackingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class SearchViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset

    def perform_create(self, serializer):
        # Assign the current logged-in user to the search object
        serializer.save(user=self.request.user)


class JobPostViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset

    def get_queryset(self):
        user = self.request.user
        queryset = JobPost.objects.all()

        # Filter job posts based on whether they have been viewed by the user
        viewed = self.request.query_params.get('viewed')

        if viewed == 'true':
            # Return only job posts that have been viewed by the user
            queryset = queryset.filter(id__in=[job.id for job in queryset if job.view_by_user(user)])
        elif viewed == 'false':
            # Return only job posts that have NOT been viewed by the user
            queryset = queryset.exclude(id__in=[job.id for job in queryset if job.view_by_user(user)])

        return queryset


class CompanyViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset


class TrackingViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = TrackingSerializer
    queryset = Tracking.objects.all()
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Tracking.objects.filter(user=self.request.user).all()


