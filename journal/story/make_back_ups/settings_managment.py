import json, os


# get info and update settings file
class Settings:
    def __init__(self):
        self.file = 'settings.json'
        self.setting = self.data_from_file()
        self.file_path_setting = self.get_file_path()
        #self.file_path_setting = "test"

    # get filepath for the setting file
    def get_file_path(self):
        curr_dir = os.path.dirname(__file__)
        return os.path.join(curr_dir, self.file)


    # get all data from file
    def data_from_file(self):
        file = open(self.get_file_path())
        found_json =  json.load(file)
        return found_json

    def get_file_path_setting(self):
        return self.file_path_setting


    def get_setting(self):
        return self.setting

    def get_curr_save_version(self):
        print(self.setting)
        return self.setting["current_backup_version"]

    # have 10 versions of backups for final JSON file
    def get_new_backup_version(self):
        new_possible = self.get_curr_save_version()
        if new_possible >= 10:
            return 0
        else:
            new_possible += 1
            return new_possible



    # update current_back_up_version in json file
    def set_new_backup_version(self):
        new_backup_version = self.get_new_backup_version()
        self.setting["current_backup_version"] = new_backup_version
        json_object = json.dumps(self.setting, indent=4)
        with open(self.file_path_setting, "w") as outfile:
             outfile.write(json_object)
        outfile.close()

    # get current back up version and update afterwards
    # used when backing up everything
    def get_current_and_update(self):
        current = self.get_current_and_update()
        self.set_new_backup_version()
        return current


# Some testing for this class
#setting_tester = Settings()
#z = setting_tester.set_new_backup_version()
#print(z)

