from .llama_sample import post_question
import json
import click
from .check_json import Answer


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
			variables = post_question(f""" Please return all variable names from
							 this diff from pull-request:
							  {diff}.
							This is the context of the diff: {context_data}.
							Please use following json format to return the answer:
								'variables': List[str] # list of all variables
								'comment': str # comment about variables 
								Please do not write anything else
							 that the json object, its really important.
								  """)	
			
			print(variables)

			# making json object from string if possible:
			try:
				variables = json.loads(variables)
				variables = variables["variables"]
			except json.JSONDecodeError or KeyError:
				# extracting json object from string
				l = variables.find("{") # finding first occurence of {
				r = variables.rfind("}") # finding last occurence of }
				if l != -1 and r != -1:
					variables = variables[l:r+1]
					try:
						variables = json.loads(variables)
						variables = variables["variables"]
					except json.JSONDecodeError or KeyError:
						# if json object is still not correct
						print("Error in json format")


			print(variables)	
			# checking if json format is correct:


			variables_to_change = post_question(f"""Check if all variable names from
								{variables} are correct and will not create problems later
								in the code. If not, suggest some new variable names.
								The diff file is: {diff}
								The context of the diff is: {context_data}
								If the variable names are not correct, please provide
								a new diff with correct variable names as well as
								a comment on why the variable names should be changed.
								Use the following json format:

								"FILE_PATH": str # path to the file
 								"LINE_POSITION": int # line number where the variable is
								"COMMENT_BODY": str # change that should be made in the code
								
								Please do not write anything else.
								""")

			print("\n\n\n"+variables_to_change+"\n\n\n")

			# checking if json format is correct:
			try:
				Answer.model_validate(variables_to_change)
				with open(ansname, "w") as ans:
						ans.write(variables_to_change)
			except Exception as e:
				try:
					l = variables_to_change.find("{") # finding first occurence of {
					r = variables_to_change.rfind("}") # finding last occurence of }
					if l != -1 and r != -1:
						variables_to_change = variables_to_change[l:r+1]
						Answer.model_validate(variables_to_change)
						with open(ansname, "w") as ans:
							ans.write(variables_to_change)
				except Exception as e:
					print("Wrong or not existing json format")
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
