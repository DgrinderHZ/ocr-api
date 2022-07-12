
export ENV_VAR := WIN
run:
	uvicorn ocr_api:app --reload