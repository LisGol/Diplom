from django.shortcuts import render
from page.standings.models import PersonalStanding, TeamStanding


def personal_standing(request):
    personal_standing = PersonalStanding.objects.order_by("-point").all()
    return render(request,
                  'diplom/standings/personal_standinds.html',
                  {'personal_standing': personal_standing,
                    })


def team_standing(request):
    team_standing = TeamStanding.objects.order_by("-score").all()
    return render(request,
                  'diplom/standings/team_standings.html',
                  {'team_standing': team_standing,
                    })

