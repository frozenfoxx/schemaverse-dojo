""" Interactive Prompt """

if __package__:
    from .kumite import Kumite
    from .options import Options
    from .players import Players
else:
    from kumite import Kumite
    from options import Options
    from players import Players
import sys
from cmd import Cmd

class Prompt(Cmd, object):
    """ Handle user input """

    def __init__(self):
        super(Prompt, self).__init__()

        self.options = Options().load_options()
        self.players = Players(self.options["playersconf"], self.options['environment']).load_players()
        self.matches = []

    def do_create(self, args):
        """ Structural guide for creation """

        print("[+] Recognized objects in the dojo to create:")
        print(" match")

    def do_create_match(self, args):
        """ Creates a match """

        print("[+] Creating a kumite...")
        kumite = Kumite(self.players, self.options['gameport'])
        kumite.load_container()
        kumite.load_players()
        self.matches.append(kumite)

        print("[+] Kumite created, port: " + str(kumite.port))

    def do_players(self, args):
        """ Show all players """

        print("[+] Player | Password")
        print("[+] -----------------")
        for i in self.players:
            print("[+] " + str(i) + " | " + str(self.players[i]))

    def do_status(self, args):
        """ Status of the training """

        print("[+] Status not yet implemented")

    def do_quit(self, args):
        """ Quit the program """

        print("[+] Shutting down")
        for i in self.matches:
            i.shutdown()

        raise SystemExit
