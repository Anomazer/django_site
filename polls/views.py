from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "<img src='https://images.techinsider.ru/upload/img_cache/bab/bab3324f6b0470e5156a1ebd5e48ce14_ce_1920x1280x0x0_cropped_666x444.jpg'>"
        "<style>img{width:1000px}")

def detail(request, question_id):
    return HttpResponse("You are seeing a question now %s." % question_id)

def results(request, question_id):
    responce = "You are seiing a question results now %s. "
    return HttpResponse(responce % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question now %s." % question_id)