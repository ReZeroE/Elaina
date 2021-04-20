import re
from clearance_scan import ClearanceScan
clScanPointer = ClearanceScan()

from server_scan import ServerScanner
server_scanner = ServerScanner()

guild_ID = []

class InputScan:
    def __init__(self):
        #layer zero - passive functions / override
        self.override = 'permission override>>'

        # layer one - prefix
        self.prefix = '//'
        self.web = 'https'

        # layer two - specified commands
        self.exitCommand = 'sys.exit(0)'
        self.purge = 'purge'
        self.getPermission = 'get perm'

        # layer two - non specified commands
        self.pickCommand = 'pick'
        self.rateCommand = 'rate'
        self.translation = 'translate'

        self.getAnimeInfo = 'get anime'
        self.getAnimeInfo2 = 'search anime'
        self.getCharacter = 'get character'
        self.getCharacter2 = 'search character'

        self.getAnimeID = 'get anime id'
        self.getCharacterID = 'get character id'

    def scanInput(self, user_input, guildID, userID):
        clearance = clScanPointer.clearanceScan(userID)

        # admin override
        if user_input.find(self.override) != -1:
            
            if clearance == 'C1':
                print('Admin 0 - override')
                clearance = 'C0'
                pass
            else:
                return "Permission Override Denied (C0D)"

        # layer one - prefix =========================================================================================================================================================
        if user_input.find(self.prefix) != -1 and user_input.find(self.web) == -1:



            # Banned Guilds ================================================================================ (Layer One)
            if server_scanner.scan_server(guildID) == -1:
                if clearance == 'C1':
                    pass
                elif user_input.find(self.web) == -1:
                    return 'Error 0 - Banned Guild'


            # Specified commands =========================================================================== (Layer Two)
            if user_input.find(self.exitCommand) != -1:
                if clearance == 'C1':
                    return 'Code A1 - Program Exit'
                else:
                    return "You don't have enough clearance to use this command! (C1D)"

            elif user_input.find(self.purge) != -1:
                if clearance == 'C1' or clearance == 'C2':
                    return 'Code A2 - Purge'
                else:
                    return "You don't have enough clearance to use this command! (C2D)"

            


            # Non-clearance gated =========================================================================== (Layer Two)
            elif user_input.find(self.getAnimeInfo) != -1 or user_input.find(self.getAnimeInfo2) != -1:
                return "Code B1 - Search Anime Info"

            elif user_input.find(self.getCharacter) != -1 or user_input.find(self.getCharacter2) != -1:
                return "Code B2 - Search Character Info"

            elif user_input.find(self.getPermission) != -1:
                return 'Code B3 - Get Permission'

            elif user_input.find(self.pickCommand) != -1:
                return 'Code B4 - Pick Message'

            elif user_input.find(self.rateCommand) != -1:
                return 'Code B5 - Rate Message'

            elif user_input.find(self.translation) != -1:
                return 'Code B6 - Translation'

            return 'Not-Specified-Command'
        return 'None-Command'
