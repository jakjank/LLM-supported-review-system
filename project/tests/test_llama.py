from src.project.llama_sample import post_question


def test_answer():
    assert (post_question("hi!") != "")
