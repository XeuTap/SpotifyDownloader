class TimeConverter:
	"""Converts string format hh.mm.ss to integer seconds """
	def __init__(self):
		pass
	def convertosec(self, _time):
		"""Returns time in seconds """
		symbols = ":;.,"
		for sym in symbols:
			raw_ls = _time.split(sym)
			if len(raw_ls) > 1:
				break
		raw = "".join(raw_ls)
		if len(raw)% 2 == 1:
			tempo = int(raw[0]) * 60
			raw = raw[1:len(raw)]
		else: 
			tempo = int(raw[0:2]) * 60
			raw = raw[2:len(raw)]
		while len(raw) > 2:
			tempo += int(raw[0: 2])
			tempo *= 60
			raw = raw[2: len(raw)]
		return tempo + int(raw[0:2])


if __name__ == "__main__":
		tc = TimeConverter()
		print(tc.convertosec("1,4,26")) # result should be 3685
		# 61,25 = 3660 + 25