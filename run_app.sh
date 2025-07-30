IMAGE_NAME="flask-gunicorn"

# Check if the image exists
if docker image inspect "$IMAGE_NAME" > /dev/null 2>&1; then
    echo "✅ Docker image '$IMAGE_NAME' already exists. Skipping build."
else
    echo "🔨 Building Docker image '$IMAGE_NAME'..."
    docker build -t "$IMAGE_NAME" .
    
    # Check build result
    if [ $? -eq 0 ]; then
        echo "✅ Build completed successfully."
    else
        echo "❌ Build failed."
        exit 1
    fi
fi
# Run the containers
docker run -d --rm -p 8000:8000 -v "$PWD/XSIAM_SPL_Converter":/app flask-gunicorn
docker run -d --rm -p 8001:8000 -v "$PWD/XSIAM_DM_Generator":/app flask-gunicorn
docker run -d --rm -p 8002:8000 -v "$PWD/XSIAM_Ingestion_Document":/app flask-gunicorn
docker container ps