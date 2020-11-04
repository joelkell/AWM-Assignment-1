from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.utils.decorators import method_decorator
from django.views import generic

from . import models


@login_required
def update_location(request):
    try:
        user_profile = models.Profile.objects.get(user=request.user)
        if not user_profile:
            raise ValueError("Can't get User details")

        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)

        user_profile.last_location = point
        user_profile.save()

        return JsonResponse({"message": f"set location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@method_decorator(login_required, name='dispatch')
class MapView(generic.TemplateView):
    template_name = "world/index.html"
