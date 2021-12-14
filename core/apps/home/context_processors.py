from .models import Session,Period
def sessions_processor(request):
    sessions = Session.objects.all()
    periods = Periods.objects.all()            
    return {'sessions': sessions,'periods': periods}