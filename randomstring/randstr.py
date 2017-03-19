from random import seed, randint, getstate, setstate
from uuid import uuid4

class RandString(object):
	"""
	RandString provides a mechanism to generate psuedo random strings of 
	fixed length.

	The string can either create base62 (A-Z, a-z, 0-9) or disambiguated 
	(base56 - omitting iIlLoO) strings.

	The class uses the random python library, and allows callers to 
	specify a seed value for repeatable string sequences.  If no 
	Initialize is provided, then the initializer is the result of a 
	call to uuid.uuid4().

	"""

	def __init__(self, Size=10, Initializer=None, NoAmbiguousCharacters=True):
		self._size = Size
		self._c = "ABCDEFGHJKMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz0123456789"
		if not NoAmbiguousCharacters:
			self._c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		self._l = len(self._c)
		self._last_state = None
		self._initializer = Initializer
		if not self._initializer:
			self._initializer = uuid4() 

	def base(self):
		"""
		Returns the base (base56 or base62) being used as int
		"""
		return self._l

	def size(self):
		"""
		Returns the size (length) of the strings being generated as int
		"""
		return self._size

	def next(self):
		"""
		Creates the next string in the psuedo-random sequence.

		Stores/replaces the existing state of the random generator as part
		of this process, to ensure that other processing dependent on the 
		existing random sequence seed is not affected by generating the 
		string.  Note that this does not support concurrent threads.

		"""
		last_state = None
		try:

			last_state = getstate()
			if not self._last_state:
				seed(self._initializer)
			else:
				setstate(self._last_state)

			selection = []
			for x in range(0, self._size):
				selection.append(self._c[randint(0, self._l-1)])

			return ''.join(selection)

		finally:
			self._last_state = getstate()
			setstate(last_state)


if __name__ == "__main__":
	from argparse import ArgumentParser
	from math import pow

	p = ArgumentParser(description='Create a random string of specified length')
	p.add_argument("-s", help='Size of the string (default: 10)', type=int, default=10)
	p.add_argument("-a", help='Include ambiguous characters (default: False)', type=bool, default=False)
	p.add_argument("-i", help='Initializer for random sequence (default: None)', type=str, default=None)
	p.add_argument("-n", help='Number of strings to generate (default: 10)', type=int, default=10)

	args = p.parse_args()

	r = RandString(Size=args.s, Initializer=args.i, NoAmbiguousCharacters=(not args.a))
	print "RandString.base():", r.base()
	print "RandString.size():", r.size()
	print "Permutations:", pow(r.base(), r.size())
	for x in range(args.n):
		print r.next()
