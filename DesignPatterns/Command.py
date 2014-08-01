'''
This is my implementation of the Command design pattern.
It decouples simple actions into a "Command" class that is
inherited by FireCommand, etc.
 
Written in python for simplicity sake.
 
For more info >> http://gameprogrammingpatterns.com/command.html
'''
 
class Command:
def execute(self, actor):
pass
 
class FireCommand(Command):
def execute(self, actor):
actor.fire()
 
class JumpCommand(Command):
def execute(self, actor):
actor.jump()
 
class YellCommand(Command):
def execute(self, actor):
actor.yell()
 
class GameActor():
def __init__(self, name=None, hp=100):
self.name , self.hp = name , hp
 
def fire(self):
print "Pew pew pew!"
def jump(self):
print "I jumped!"
 
def yell(self):
print "I AM "+str(self.name)+"!"
 
#Setup our command handlers
fire = FireCommand()
jump = JumpCommand()
yell = YellCommand()
 
#Make a game actor object
actor = GameActor("Tom", 200)
 
 
#Fire off some commands to an actor
fire.execute(actor)
jump.execute(actor)
yell.execute(actor)
 
'''
Output:
 
Pew pew pew!
I jumped!
I AM Tom!
 
'''
