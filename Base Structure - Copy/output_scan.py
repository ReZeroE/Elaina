import os
import sys
import re


class OutputScan:
    def scan_output(self, message): # returns True if nothing bad found. False otherwise

        if message.find("@") != -1:
            return "sign unavailable"

        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Storage'
        with open(os.path.join(dir_path, "Banned-Words.txt"), "r") as file:
            bad_words = file.read().replace(" ", "").split(",")
            messageArr = re.sub('\W+',' ', message.lower()).split(" ") # user input

            print(f"Output Scan Array: {messageArr}")

            if any(badWord in messageArr for badWord in bad_words):
                file.close()
                return ('B') # bad
            else:
                file.close()
                return ('G') # good
                