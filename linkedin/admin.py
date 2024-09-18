from django.contrib import admin
from linkedin.models import Search, Tracking, JobPost, Company


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "keyword", "created_at", "updated_at")


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ("id", "job_post", "user", "created_at")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","raison_social")