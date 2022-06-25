import fundamental

while True:
	text = input('fundamental (please run your code with RUN("sample.myopl")) => ')
	if text.strip() == "": continue
	result, error = fundamental.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
