from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):
    """Allow users to eidt their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own prifile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""


    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update thei own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

    
