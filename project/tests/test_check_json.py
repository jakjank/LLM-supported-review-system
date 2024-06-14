from src.project.check_json import Answer, Change
import json

def test_check_json():


	# checking Change
	c1 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes"}'
	c2 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODYYYY" : "proposed changes"}'
	
	c3 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes", "COMMENT_BODY_2":"changes2"}'

	check_c2 = True
	check_c3 = True
	Change.model_validate(json.loads(c1))
	print("c1 is valid")
	try:
		Change.model_validate(c2)
	except:
		check_c2 = False
	try:
		Change.model_validate(c3)
	except:
		check_c3 = False
	if check_c2 == True or check_c3 == True: # both of them should fail
		assert(False)


	# checking Answer:
	a1 ={
		 "changes": 
		 [
			{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			},{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			},{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			},{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			},{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			},{
				"FILE_PATH": "aaa.py", 
				"LINE_POSITION" : 1, 
				"COMMENT_BODY" : "proposed changes"
			}
		 ]
		 }
	
	a2 = '{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes"}'
	a3 = { "changes": [{"FILE_PATH": "aaa.py", "LINE_POSITION" : 1, "COMMENT_BODY" : "proposed changes"}]}

	Answer.model_validate(a1) # should be good

	check_a2 = True
	try:
		Answer.model_validate(json.loads(a2))
	except:
		check_a2=False
	assert(check_a2 == False) # a2 should not work
	Answer.model_validate(a3) # also should work