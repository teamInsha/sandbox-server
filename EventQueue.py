from queue import Queue

class EventQueue:
	def __init__(self):
		self._queue = Queue()

	def enqueue(self, event):
		print("Event is enqueued.")
		self._queue.put(event)

	def dequeue(self):
		print("Event is dequeued.")
		return self._queue.get(block=True, timeout=None)
	
	def size(self):
		return self._queue.qsize()

	def task_done(self):
		self._queue.task_done()
		
