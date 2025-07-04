from rest_framework import permissions
import datetime



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user 

class IsUsernameJohn(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.username == 'john':
            return False
        return True

class IsDayBetweenMondayAndFriday(permissions.BasePermission):
    def has_permission(self, request, view):
        now = datetime.datetime.now
        return now.weekday() >= 0 and now.weekday() < 5     

class IsTimeBetween9And18(permissions.BasePermission):
    def has_permission(self, request, view):
        now = datetime.datetime.now()
        return now.hour >= 9 and now.hour < 18

class IsPremiumUserAndPremiumCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return False

class IsYearEven(permissions.BasePermission):
    def has_permission(self, request, view):
        now = datetime.datetime.now()
        if now.year % 2 == 0:
            return True
        return False


class IsUserSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

class OnlyPutAndPatch(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['PUT' , 'PATCH']

           
