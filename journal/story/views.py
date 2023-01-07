from django.shortcuts import render
from .models import Entry
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    entries = Entry.objects.all().order_by("-id")

    # check is anything will be needed to be added to db or want to back up data
    if request.method == "POST":
        data = request.POST
        print(data)
        if data.get('back_up') == "":
            print("IF WORKING")

            make_back_up(entries)
    return render(request, 'dashboard.html', {'entries': entries})


# make JSON file with all db for back up purposes, automatic if run on desktop only
# use pk for incremental back up
# full monthly back ps
def make_back_up(entries):
    db_to_json = {}
    print(entries)
    for story in entries:

        print(story.pk)
