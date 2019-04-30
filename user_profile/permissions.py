from rest_framework import permissions 



class IsLoggedInUserOrAdmin(permissions.BasePermission): # Providing logged in user to ONLY view his own profile.

	def has_object_permission(self, request, view, obj):
		return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission): # If the logged in user is admin then permissions for him. 

	def has_permission(self, request, view):
		return request.user and request.user.is_staff

	def has_object_permission(self, request, view, obj):
		return request.user and request.user.is_staff
