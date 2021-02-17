from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):
    """Allow users to eidt their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own prifile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
    