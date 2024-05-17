from llama_sample import post_question


def check_file(filename, ansname=None):
	"""
	function uses ollama llama2 model to check if in given
	diff from pull request should some variable names be changed
	it also checks for unnecessary fragments of code
	:param filename: name of file with diff from pull request
	:return: answer from ollama how (and if) to change pull request is
	saved in a file
	"""
	with open(filename, "r") as data:
		variables = post_question("Return all variable names from this diff"
								  "from pull-request" + data.read())
		variables_to_change = post_question(f"Check if all variable names ({variables}) "
											f"are correct and"
							" will not create problems later. "
							"\nIs there something that should be changed?")

		unnecessary_code = post_question("Check if in that diff"
								"are some unnecessary fragments"
								"of code that should be replaced or can"
								"be just removed")
		if ansname is None:
			return("Zmienne:\n"+ str(variables) + "\n\n Komentarz:" +
				variables_to_change +"\n\n\n\n" + unnecessary_code)
		else:
			with open(ansname, "w") as ans:
				ans.write(variables_to_change +"\n\n\n\n" + unnecessary_code)

import click
@click.command()
@click.option('--input', default="diff.txt", help='Name of the file with ollama input')
@click.option('--output', default="comment.txt", help='Name of the file for ollama output')
def main(input, output):
    check_file(input, output)


if __name__ == "__main__":
	main()
