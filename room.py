


class Player():
    
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        

class Room():
    def __init__(self, id):
        self.id = id
        self.players = []
        self.bullets_pos = {}
    
    def update_player_pos(self, other : Player):
        for player in self.players:
            if player.id == other.id:
                player.pos = other.pos
                break
    
    def update_bullet_pos(self,bullet_id, pos):
        self.bullets_pos[bullet_id] = pos
        
        
        