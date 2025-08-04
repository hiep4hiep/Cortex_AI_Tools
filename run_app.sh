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
docker compose up -d