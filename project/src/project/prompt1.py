from .llama_sample import post_question
import json
import click


def check_file(filename, ansname=None, context=None, debug=False):
	"""
	function uses ollama llama2 model to check if in given
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
			variables = post_question(f""" Please return all variable names from
							 this diff from pull-request:
							  {diff}.
							This is the context of the diff: {context_data}.
							Please use json format to return the answer. All variables 
							 should be saved in the "variables" key. Any extra comment 
							 on variables or other things
							 should be provided using the
							 "comment" key. Please do not write anything else
							 that the json object, its really important.
								  """)	
			
			# making json object from string if possible:
			try:
				variables = json.loads(variables)
				variables = variables["variables"]
			except json.JSONDecodeError or KeyError:
				if debug:
					print("Error in json format")


			variables_to_change = post_question(f"""Check if all variable names from
								{variables} are correct and will not create problems later
								in the code. If not, suggest some new variable names.
								The diff file is: {diff}
								The context of the diff is: {context_data}
								If the variable names are not correct, please provide
								a new diff with correct variable names as well as
								a comment on why the variable names should be changed below.""")

			# unnecessary_code = post_question("Check if in that diff"
			# 					"are some unnecessary fragments"
			# 					"of code that should be replaced or can"
			# 					"be just removed")

			if debug:
				print(variables)
				print("\n\n\n\n")
				print(variables_to_change)
			else:
				with open(ansname, "w") as ans:
						ans.write(variables_to_change)



@click.command()
@click.option('--input', default="SRS_files/diff.txt", help='Name of the file with ollama input')
@click.option('--output', default="SRS_files/comment.txt", help='Name of the file for ollama output')
@click.option('--context', default="SRS_files/context.txt", help='Name of the file with context of diff')
@click.option('--debug', default=False, help='Debug mode')
def main(input, output, context, debug):
    check_file(input, output, context, debug)


if __name__ == "__main__":
	main()
