from .llama_sample import post_question
import json
import click
from .check_json import Answer



variables_schema = { # daje właśnie w takej formie -> działa
	"variables": {
		"type": "array",
		"items": {
			"type": "string",
			"description": "Variable name"
		}
	}
}

answer_schema = {'$defs': 
 	{'Change': 
   		{'properties': 
	  		{'FILE_PATH': 
	  			{'title': 'File Path', 
	   			'type': 'string'}, 
			'LINE_POSITION': 
				{'title': 'Line Position', 
	 			'type': 'integer'}, 
			'COMMENT_BODY': 
				{'title': 'Comment Body', 
	 			'type': 'string'}
			}, 
		'required': 
			['FILE_PATH', 
 			'LINE_POSITION', 
			'COMMENT_BODY'],
		 'title': 'Change',
		 'type': 'object'}
	}, 
	'properties': {
		'changes': {
			'items': {'$ref': '#/$defs/Change'},
			'title': 'Changes', 'type': 'array'
		}
	},
	'required': ['changes'], 
	'title': 'Answer', 
	'type': 'object'
}





nic = {
	"changes":{
		"type": "array",
		"items": 
		{	
			"FILE_PATH": {
				"type": "string",
				"description": "Path to the file"
			},
			"LINE_POSITION": {
				"type": "integer",
				"description": "Line number where the change happens"
			},
			"COMMENT_BODY": {
				"type": "string",
				"description": "New code that should be in this line"
			}
		
		}
	}
}



def check_file(filename, ansname=None, context=None, debug=False):
	"""
	function uses ollama llama3 model to check if in given
	diff from pull request should some variable names be changed
	it also checks for unnecessary fragments of code
	:param filename: name of file with diff from pull request
	:param ansname: name of file where answer should be saved
	:param context: name of file with context of diff
	:return: answer from ollama how (and if) to change pull request is
	:debug: if True, print answer instead of saving it in a "ansname" file
	saved in a file
	"""

	with open(filename, "r") as data:
		with open(context, "r") as context_fd:
			diff = data.read()

			if(len(diff) <= 3): # if diff is empty
				with open(ansname, "w") as ans:
					ans.write("Nie ma zmian w plikach pythonowych")
					return
				
			# if diff is not empty:
			
			context_data = context_fd.read()
			variables = post_question(f"""
							 You are a helpful AI assistant. Given a diff file and context
							 of changes the assistant will return all variable names from
							 the diff file. Output in JSON using the schema 
							 defined here: {variables_schema}.
							 The diff file: {diff}.
							 This is the context of the diff: {context_data}.""")	
			
			variables = variables.strip()
			if debug: print(variables)

			# making json object from string if possible:
			try:
				variables = json.loads(variables)
				variables = variables["variables"]
			except Exception as e:
				# extracting json object from string
				variables = str(variables)
				l = variables.find("{") # finding first occurence of {
				r = variables.rfind("}") # finding last occurence of }
				if l > -1 and r > -1 and l < r:
					print(f"l = {l}, r = {r}")
					variables = variables[l:r+1]
					try:
						variables = json.loads(variables)
						variables = variables["variables"]
					except Exception as e:
						# if json object is still not correct
						print("Error in json format (exception = ", e, "), variables:", variables)


			if debug: print(variables)
			# checking if json format is correct:


			variables_to_change = post_question(f"""
								You are a helpful AI assistant. Given diff file and context
								of changes the assistant will return suggest changes that 
								should be made in order to make sure all variable names 
								are suitable. The changes is a list of dictionaries with
								keys: FILE_PATH, LINE_POSITION, COMMENT_BODY. Output in JSON
								using the schema defined here: {answer_schema}.
								Output example is:""" + """
								{'changes':[
									{
										'FILE_PATH': 'project/src/project/prompt1.py'
										'LINE_POSITION': 51
										'COMMENT_BODY': '	with open(filename, "r") as diff_file:'
									},
									{
										'FILE_PATH': 'project/src/project/prompt1.py'
										'LINE_POSITION': 53
										'COMMENT_BODY': '			diff = diff_file.read()'
									},
									{
										'FILE_PATH': 'project/src/project/prompt1.py'
										'LINE_POSITION': 130
										'COMMENT_BODY': '				with open(ansname, "w") as ans_fd:'
									}
								]}""" + f"""
								The diff file is: {diff}.
								Variables are: {variables}.
								The context of the diff is: {context_data}.
								""")

			variables_to_change = variables_to_change.strip() # str
			print("WARIABLES TO CHANGE:\n", variables_to_change, "\n")

			# checking if json format is correct:
			try:
				variables_to_change = json.loads(variables_to_change)
				Answer.model_validate(variables_to_change)
				with open(ansname, "w") as ans:
						ans.write(str(variables_to_change))
			# except Exception as e:
				# try:
				# 	l = variables_to_change.find("{") # finding first occurence of {
				# 	r = variables_to_change.rfind("}") # finding last occurence of }
				# 	if l != -1 and r != -1:
				# 		variables_to_change = variables_to_change[l:r+1]
				# 		Answer.model_validate(variables_to_change)
				# 		with open(ansname, "w") as ans:
				# 			ans.write(variables_to_change)
			except Exception as e:
				print("Wrong or not existing json format (exception: ", e, ")")
				return

				


@click.command()
@click.option('--input', default="SRS_files/diff.txt", help='Name of the file with ollama input')
@click.option('--output', default="SRS_files/comment.json", help='Name of the file for ollama output')
@click.option('--context', default="SRS_files/context.txt", help='Name of the file with context of diff')
@click.option('--debug', default=False, help='Debug mode')
def main(input, output, context, debug):
    check_file(input, output, context, debug)


if __name__ == "__main__":
	main()
