#!/bin/bash
set -e

echo "Starting Project Apero Setup in Codespaces..."

# 1. Build and start Docker containers using docker-compose
echo "Building and starting Docker containers..."
docker-compose up --build -d

# 2. Run 'rasa train' inside the Rasa container
echo "Training Rasa model inside the Rasa container..."
docker exec -it rasa_server rasa train

# 3. Restart Docker containers to load the trained model
echo "Restarting Docker containers..."
docker-compose restart

echo "Setup complete! Access the Project Apero web application at http://localhost:8051"
