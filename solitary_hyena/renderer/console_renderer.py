from . import BaseRenderer
import curses

class ConsoleRenderer(BaseRenderer):

  def __init__(self):
    super(ConsoleRenderer, self).__init__()



  def title(self, entries, id, parser):
    title = super(ConsoleRenderer, self).title(entries, id, parser)

