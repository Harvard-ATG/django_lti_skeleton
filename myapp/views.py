from django.http import HttpResponse
from django_app_lti.views import LTILaunchView

class MyLTILaunchView(LTILaunchView):
    def hook_before_post(self, request):
        super(MyLTILaunchView, self).hook_before_post(request)
        print "before post"

    def hook_process_post(self, request):
        super(MyLTILaunchView, self).hook_process_post(request)
        print "process post"

    def hook_after_post(self, request):
        super(MyLTILaunchView, self).hook_after_post(request)
        print "after post"

    def hook_get_redirect(self):
        print "get redirect"
        return super(MyLTILaunchView, self).hook_get_redirect()

def index(request, course_id=None):
    content = 'Welcome to my app. Course ID: %s User: %s' % (course_id, request.user.email)
    return HttpResponse(content)

def hello_world(request):
    return HttpResponse("Hello, World!")
