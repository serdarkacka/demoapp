def concat(array, f, t):
	if array is None:
		return ''
	n = len(array)

	if f > t or f < 0 or t >= n or n == 0:
		return ''

	res = ''

	i = f
	while i <= t:
		res = res + str(array[i])
		i = i + 1

	return res