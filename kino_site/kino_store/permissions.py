from rest_framework.permissions import BasePermission


class IsProUserOrSimpleMovieOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.status_movie == 'simple':
            return True
        if request.user.status == 'pro':
            return True
        return False