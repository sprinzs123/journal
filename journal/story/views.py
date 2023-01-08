from django.shortcuts import render
from .models import Entry
from django.contrib.auth.decorators import login_required
import json


@login_required
def home(request):
    entries = Entry.objects.all().order_by("-id")

    # check is anything will be needed to be added to db or want to back up data
    if request.method == "POST":
        data = request.POST
        if data.get('back_up') == "":
            full_back_up(entries)
    return render(request, 'dashboard.html', {'entries': entries})


# make JSON file with all db for back up purposes, automatic if run on desktop only
# use pk for incremental back up
# used in full monthly backups
def full_back_up(entries):
    db_to_json = {}
    for story in entries:
        json_story = entry_to_dic(story)
        db_to_json.update(json_story)
    return db_to_json


# return what data is missing from back up file
# return all missing data
# get last pk that been recorded in JSON and compare that to db
def get_missing_json(entries, json_file):
    last_db_pk = entries[-1].pk
    last_json_pk = get_last_json_pk(json_file)
    missing = {}
    if last_json_pk != last_db_pk:
        for missing_pk in range(last_json_pk, last_db_pk + 1):
            curr_object = entries[missing_pk]
            dic_object = entry_to_dic(curr_object)
            missing.update(dic_object)
    return missing


# convert one entry to dictionary
def entry_to_dic(one_entry):
    one_entry_dic ={
        one_entry.pk: {
            "title": one_entry.title,
            "date_start": one_entry.date_start.strftime('%m/%d/%Y'),
            "date_end": one_entry.date_end.strftime('%m/%d/%Y'),
            "day_of_week_start": one_entry.day_of_week_start,
            "day_of_week_end": one_entry.day_of_week_end,
            "text": one_entry.text,
            "tags": one_entry.tags
        }
    }
    return one_entry_dic



# get last entry in json back up file
def get_last_json_pk(file_name):
    f = open("stories/" + file_name)
    data = json.load(f)
    last_pk = 0
    for pk in data:
        last_pk = pk
    f.close()
    return last_pk


