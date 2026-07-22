def http_error(status):
	match status:
		case 401 | 403 | 405:
			return "Not allowed"
		case 400:
			return "Bad request"
		case 404:
			return "Not found"
		case 418:
			return "I'm a teaport"
		case _:
			return "Something is wrong with the internet"

# in the last case, the wildcard("the variable name"/ _ ) never fails to match. 
