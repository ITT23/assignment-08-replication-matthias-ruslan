import os
import subprocess
from Config import Config


def get_files():
    applications = []

    with open(Config.APPLICATIONS_PATH) as f:
        while line := f.readline():
            split_line = (line.split(" ", 1))
            applications.append({'gestureName': split_line[0].rstrip(),
                                 'path': os.path.normpath(
                                     (split_line[1].rstrip()))})

    return applications


class ApplicationLauncher:

    def __init__(self):
        self.applicationPaths = get_files()

    def init_application(self, gesture):
        for i in range(0, len(self.applicationPaths)):
            if gesture == self.applicationPaths[i]["gestureName"]:
                try:
                    subprocess.Popen([self.applicationPaths[i]["path"]])
                except Exception as e:
                    print(Config.WRONG_APPLICATION_PATH_EXCEPTION)

                return True

        return False
