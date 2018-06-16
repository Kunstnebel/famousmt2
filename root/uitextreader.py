class TextReader():

	def __init__(self, bAutoEnter = TRUE):
		self.is_auto_enter = bAutoEnter
		self.Clear()

	def __del__(self):
		pass

	# reset
	def Clear(self):
		self.text = ""
		self.keyWords = {}

	# add another keyword with value
	def AddKeyWord(self, keyWord, value):
		self.keyWords[keyWord] = str(value)

	# load any text file
	def LoadFile(self, fileName):

		self.text = ""

		lines = pack_open(fileName, "r").readlines()

		do_read_line = TRUE
		in_argument = {"bool":TRUE,"elseif":FALSE,"next":None,"last":None}
		last_argument = in_argument

		text = ""
		for line in lines:
			current = self.__ConvertText(line)

			# if clauses
			if current.startswith("[IF:") or current.startswith("[ELSEIF:"):
				current.replace(" ", "") # no spaces allowed

				startText = "[IF:"
				if not current.startswith(startText) and current.startswith("[ELSEIF:"):
					startText = "[ELSEIF:"

				operatorInfo = self.__FindOperator(current)

				# get argument 1
				arg1 = current[len(startText):operatorInfo["pos"]]

				# get argument 2
				arg2 = None
				if operatorInfo:
					current = current[operatorInfo["pos"]+operatorInfo["len"]:]
					endPos = current.rfind("]")
					if endPos == -1:
						import dbg
						dbg.TraceError("cannot get text by file %s [no end of IF line \"%s\"]" % (fileName, line.replace("\n", "")))
						return FALSE
					arg2 = current[:endPos]

				# compute by operator
				if operatorInfo:
					result = self.__ComputeOperator(arg1, arg2, operatorInfo["operator"])
				else:
					result = self.__ComputeOperator(arg1, arg2, "")

				# add into argument list
				if startText == "[IF:":
					last_argument["next"] = {"bool":result,"if_res":result,"elseif":FALSE,"next":None,"last":None}
					last_argument["next"]["last"] = last_argument
					last_argument = last_argument["next"]
				elif startText == "[ELSEIF:":
					if last_argument["bool"] == TRUE:
						result = FALSE
					last_argument["bool"] = result
					last_argument["elseif"] = TRUE

				# check read line bool
				if do_read_line == TRUE and result == FALSE:
					do_read_line = FALSE
				elif do_read_line == FALSE and result == TRUE:
					# refresh read_line
					do_read_line = TRUE
					arg = in_argument
					while do_read_line == TRUE:
						if arg["bool"] == FALSE:
							do_read_line = FALSE
						elif arg["next"] == None:
							break
						else:
							arg = arg["next"]

				if startText == "[ELSEIF:":
					if result == TRUE:
						last_argument["if_res"] = TRUE

			# else clause
			elif current.startswith("[ELSE]"):
				if last_argument["elseif"] == TRUE:
					last_argument["bool"] = last_argument["if_res"] == FALSE
				else:
					last_argument["bool"] = last_argument["bool"] == FALSE
				last_argument["elseif"] = FALSE

				# check read line bool
				if do_read_line == TRUE and last_argument["bool"] == FALSE:
					do_read_line = FALSE
				elif do_read_line == FALSE and last_argument["bool"] == TRUE:
					# refresh read_line
					do_read_line = TRUE
					arg = in_argument
					while do_read_line == TRUE:
						if arg["bool"] == FALSE:
							do_read_line = FALSE
						elif arg["next"] == None:
							break
						else:
							arg = arg["next"]

			# endif clause
			elif current.startswith("[ENDIF]"):
				if last_argument["last"] == None:
					import dbg
					dbg.TraceError("cannot get text by file %s [unallowed \"[ENDIF]\"]" % (fileName))
					return FALSE
				last_argument = last_argument["last"]

				# refresh read_line
				do_read_line = TRUE
				arg = in_argument
				while do_read_line == TRUE:
					if arg["bool"] == FALSE:
						do_read_line = FALSE
					elif arg["next"] == None:
						break
					else:
						arg = arg["next"]

			# no clause
			else:
				if do_read_line == TRUE:
					if self.is_auto_enter == TRUE:
						text += current.replace("\n", "[ENTER]")
					else:
						text += current.replace("\n", "")

		self.text = text
		return TRUE

	def GetText(self):
		return self.text

	# convert text by keywords
	def __ConvertText(self, text):
		for keyWord in self.keyWords:
			text = text.replace(keyWord, self.keyWords[keyWord])

		return text

	# find any operator for if/elseif clauses
	def __FindOperator(self, text):
		for pos in xrange(len(text)):
			c = text[pos:pos+1]
			if c == '>' or c == '<' or c == '=':
				return {"pos":pos, "len":1, "operator":c}
			elif text[pos:pos+2] == '!=' or text[pos:pos+2] == '<>':
				return {"pos":pos, "len":2, "operator":text[pos:pos+2]}

		return None

	# compute the operator with the arguments
	def __ComputeOperator(self, arg1, arg2, operator):
		if operator == '>':
			return int(arg1) > int(arg2)
		elif operator == '<':
			return int(arg1) < int(arg2)
		elif operator == '=':
			return str(arg1) == str(arg2)
		elif operator == '!=' or operator == '<>':
			return str(arg1) != str(arg2)
		elif arg1.lower() == "true":
			return TRUE
		elif arg1.lower() == "false":
			return FALSE
		else:
			return int(arg1)
