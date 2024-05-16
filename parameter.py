#input params

#Blackout Transformation
class Dummy(object):
  def __init__(self):
    self.seeds = 10000
    self.threshold = 0.5
    self.target_model = 0
    self.weight_diff = 1
    self.weight_nc = 0.1
    self.transformation = 'blackout'
    self.start_point = (0,0)
    self.grad_iterations = 50
    self.step = 1
    self.occlusion_size = (5,5)
args = Dummy()

#Light Transformation
class obj(object):
  def __init__(self):
    self.seeds = 10000
    self.threshold = 0.5
    self.target_model = 0
    self.weight_diff = 1
    self.weight_nc = 0.5
    self.transformation = 'light'
    self.start_point = (0,0)
    self.grad_iterations = 120
    self.step = 500
    self.occlusion_size = (10,10)
args = obj()

#Occulasion

#input params
class Dummy(object):
  def __init__(self):
    self.seeds = 10000
    self.threshold = 0.5
    self.target_model = 0
    self.weight_diff = 1
    self.weight_nc = 0.1
    self.transformation = 'occl'
    self.start_point = (0,0)
    self.grad_iterations = 500
    self.step = 3
    self.occlusion_size = (10, 10)
args = Dummy()