import json

# get info and update settings file
class Settings:
    def __init__(self):
        self.setting = self.data_from_file()

    def data_from_file(self):
        file = open('settings.json')
        found_json =  json.load(file)
        return found_json


    def get_setting(self):
        return self.setting

    def get_curr_save_version(self):
        print(self.setting)
        return self.setting["current_backup_version"]

    # have 10 versions of backups for final JSON file
    def get_new_backup_version(self):
        new_possible = self.get_curr_save_version()
        if new_possible > 10:
            return 0
        else:
            new_possible += 1
            return new_possible

    # update current_back_up_version in json file
    def set_new_backup_version(self):
        new_backup_version = self.get_new_backup_version()
        self.setting["current_backup_version"] = new_backup_version

        self.file.write(json.dumps(self.setting))
        self.file.close()



# Some testing for this class
setting_tester = Settings()
z = setting_tester.get_setting()
print(z)

f = open('settings.json')
data = json.load(f)
print(data)