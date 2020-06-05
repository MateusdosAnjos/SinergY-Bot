class ADISpotting:

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user] = 0

   def add_points(self, user, points):
        self.users[user] = self.users[user] + points