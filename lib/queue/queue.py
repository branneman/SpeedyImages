# NOT USED, REFACTOR BEFORE USE

# Read more:
#  http://docs.python.org/3.3/reference/datamodel.html#emulating-container-types
#  http://stackoverflow.com/questions/3487434/overriding-append-method-after-inheriting-from-a-python-list
#  http://stackoverflow.com/questions/8180014/how-to-subclass-python-list-without-type-problems

from queue.item import QueueItem

class Queue(list):

    def append(self, item):

        if not isinstance(item, QueueItem):
            raise TypeError('item is not of type %s' % QueueItem)

        super().append(item)
