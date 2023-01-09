from django.shortcuts import render
from .models import Entry
from django.contrib.auth.decorators import login_required
import json
import os


@login_required
def home(request):
    entries = Entry.objects.all().order_by("-id")

    # check is anything will be needed to be added to db or want to back up data
    if request.method == "POST":
        data = request.POST
        if data.get('back_up') == "":
            all_data_dic = full_back_up(entries)
            make_new_json_backup("2023_all.json", all_data_dic)
    return render(request, 'dashboard.html', {'entries': entries})


# make JSON file with all db for back up purposes, automatic if run on desktop only
# use pk for incremental back up
# used in full monthly backups
def full_back_up(entries):
    all_dic_enry= {}
    for story in entries:
        json_story = entry_to_dic(story)
        all_dic_enry.update(json_story)
    return all_dic_enry


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


# create new json file from input dictionary
# used creating monthly backups
def make_new_json_backup(file_name, input_dic):
    json_converted = json.dumps(input_dic)
    curr_dir = os.path.dirname(__file__)
    full_path = os.path.join(curr_dir, 'stories/', file_name)
    print(full_path)
    with open(full_path, 'w') as f:
        f.write(json_converted)
        print("The json file " + file_name + " is created")

