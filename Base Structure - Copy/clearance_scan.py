import sys
import os

class ClearanceScan:
    '''
    Class responsible for determining the user's clearance level
    All clearance data is stored in either C1-Clearance-List.txt or C2-Clearance-List.txt
    '''

    def clearanceScan(self, userID):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Storage'
        C1 = open(os.path.join(dir_path, "C1-Clearance-List.txt"), "r", encoding="utf-8")
        
        for line in C1:
            if userID == int(line.strip()):
                C1.close()
                return 'C1'

        C2 = open(os.path.join(dir_path, "C2-Clearance-List.txt"), "r", encoding="utf-8")
        for line in C2:
            if userID == int(line.strip()):
                C2.close()
                return 'C2'

        return 'None'