#!/bin/bash

# SAIL Laboratory Safety Documentation - Local Testing Script
# This script runs Jekyll locally for testing before deployment

echo "Starting Jekyll local server..."
echo "================================"
echo ""

# Check if bundle is installed
if ! command -v bundle &> /dev/null; then
    echo "Error: Bundler is not installed."
    echo "Please install it with: gem install bundler"
    exit 1
fi

# Install dependencies if needed
if [ ! -f "Gemfile.lock" ]; then
    echo "Installing dependencies..."
    bundle install
    echo ""
fi

# Serve the site locally
echo "Starting server at http://localhost:4000"
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload
