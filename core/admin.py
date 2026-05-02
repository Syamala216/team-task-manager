from django.contrib import admin
from .models import User, Workspace, WorkItem

admin.site.register(User)
admin.site.register(Workspace)
admin.site.register(WorkItem)