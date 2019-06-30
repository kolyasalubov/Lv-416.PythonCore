class Ball(object):
    def __init__(self, ball_type = None):
      if ball_type == None:
        self.ball_type = "regular"
      else:
        self.ball_type = ball_type