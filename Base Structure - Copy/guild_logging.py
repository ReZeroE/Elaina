import os
import sys

class BotLog:
    def __init__(self):
        pass

    def log_guild_info(self, guild_id, guild_name) -> bool:
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Storage'
        log_file = open(os.path.join(dir_path, "Elaina-Log.txt"), "a+", encoding="utf-8")
        log_file.seek(0)

        guild_id = str(guild_id)
        guild_count = 1
        while True:
            lines = log_file.readlines()

            if len(lines) == 0:
                print(f'Guild ID {guild_id} has not been found in my log. New Guild info will be appended.')
                log_file.write(f'Guild ID: {guild_id}\n')
                log_file.write(f'Guild Name: {guild_name}\n')
                log_file.write(f'Guild Count: 1\n\n')
                break

            for counter, line in enumerate(lines):
                if line.find('Guild ID') != -1:
                    guild_count += 1

                if line.find(guild_id) != -1:
                    print('found')
                    break
                elif counter + 1 == len(lines):
                    print(f'Guild ID {guild_id} has not been found in my log. New Guild info will be appended.')
                    log_file.write(f'Guild ID: {guild_id}\n')
                    log_file.write(f'Guild Name: {guild_name}\n')
                    log_file.write(f'Guild Count: {guild_count}\n\n')
                    break
            break

        log_file.close()
        return True



        