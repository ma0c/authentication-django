#! -*- encoding: UTF-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib import messages

from . import conf


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """
    Generic Mixin to make an user to be authenticated before see system information
    """
    login_url = "log_in"


class SuperAdminRequiredMixin(AccessMixin):
    """
    Generic mixin to ensure user logged is super_user
    CBV mixin which verifies that the current user is authenticated.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            if request.user.is_staff:
                return super(SuperAdminRequiredMixin, self).dispatch(request, *args, **kwargs)
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    conf.LACK_OF_PERMISSION
                )
                return self.handle_no_permission()
