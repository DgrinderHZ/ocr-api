
export ENV_VAR := WIN

run:
	uvicorn ocr_api:app --reload

find:
	find -iname $(target)

logs:
	heroku logs -a ocr-fastapi-v1 --tail

update:
	heroku run apt-get update -a ocr-fastapi-v1 
	heroku run apt-get install ffmpeg libsm6 libxext6 -y -a ocr-fastapi-v1
	heroku run apt-get install -y python3-opencv -a ocr-fastapi-v1
	heroku run pip install opencv-python -a ocr-fastapi-v1


update2:
	heroku run apt-get install ffmpeg libsm6 libxext6 -y -a ocr-fastapi-v1