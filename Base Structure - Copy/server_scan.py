import sys
import os

class ServerScanner:
    '''
    Class responsible for scanning the server ID to determine whether if the server has been banned
    Banned server ID list is stored in ./Storage/Banned-Server
    '''

    def __init__(self):
        self.banned_servers = [674833962572578847]

    def scan_server(self, server_id) -> int:
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Storage'
        server_file = open(os.path.join(dir_path, "Banned-Server.txt"), "r", encoding="utf-8")
        server_file.seek(0)

        for line in server_file:
            if str(server_id) == line.strip():
                server_file.close()
                return -1 # bad
        server_file.close()
        return 0 # good
