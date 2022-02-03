from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from page.standings.models import Personal_standing


def personal_standing(request, point_id=None, order_by=None):
    personal_standing = Personal_standing.objects.order_by("-point").all()
    return render(request,
                  'diplom/standings/personal_standinds.html',
                  {'personal_standing': personal_standing,
                    })


def team_standing(request):
    team_standing = Personal_standing.objects.all()
    return render(request,
                  'diplom/standings/team_standings.html',
                  {'team_standing': team_standing,
                    })

