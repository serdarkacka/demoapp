def concat(array, start, end):
	if array is None:
		return ''
	n = len(array)

	if start > end or start < 0 or end >= n or n == 0:
		return ''

	res = ''

	i = start
	while i <= end:
		res = res + str(array[i])
		i = i + 1

	return res