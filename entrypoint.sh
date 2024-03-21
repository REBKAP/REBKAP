#!/bin/bash
# entrypoint.sh

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Start your application
exec gunicorn --bind 0.0.0.0:${PORT:-5000} "app:app"
