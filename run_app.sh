docker run -d --rm -p 8000:8000 -v "$PWD/XSIAM_SPL_Converter":/app flask-gunicorn
docker run -d --rm -p 8001:8000 -v "$PWD/XSIAM_DM_Generator":/app flask-gunicorn
docker run -d --rm -p 8002:8000 -v "$PWD/XSIAM_Ingestion_Document":/app flask-gunicorn