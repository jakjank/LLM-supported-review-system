from src.project.check_json import Answer
import json

def test_check_json():
	v1 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes"}'
	v2 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODYYYY" : "proposed changes"}'
	
	v3 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes", "COMMENT_BODY_2":"changes2"}'

	check_v2 = True
	check_v3 = True
	Answer.model_validate(json.loads(v1))
	print("v1 is valid")
	try:
		Answer.model_validate(v2)
	except:
		check_v2 = False
	try:
		Answer.model_validate(v3)
	except:
		check_v3 = False
	if check_v2 == True or check_v3 == True: # both of them should fail
		assert(False)