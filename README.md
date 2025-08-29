# AI Image Generator

A simple web application built with Python and Flask that uses the Google Gemini API to generate images from a text prompt. This project was created as part of the "From Setup to App" tutorial.

## How It Works

This application consists of a simple frontend (HTML, CSS, JavaScript) and a backend server (Python, Flask). 
The user enters a prompt on the webpage, which is sent to the Flask server. The server then calls the Google Gemini API, receives the generated image data, and sends it back to the webpage to be displayed.

## Prerequisites

* A working WSL (Windows Subsystem for Linux) environment.
* Python 3 and `pip` installed.
* A Google Gemini API Key.

## Setup and Installation Guide

Follow these steps in your Linux terminal to get the application running.

### 1. Set Up Your API Key
This application requires a Google Gemini API key.
1.  Get your key from [Google AI Studio](https://aistudio.google.com/).
2.  Store the key securely as an environment variable. **Replace `YOUR_API_KEY` with your actual key.**
    ```bash
    echo 'export GOOGLE_API_KEY="YOUR_API_KEY"' >> ~/.bashrc && source ~/.bashrc
    ```

### 2. Install Dependencies
Navigate to the project directory and install the required Python libraries:
```bash
# Install Flask for the web server and the Google AI library for the API
pip install Flask google-generativeai

## Github commands for students coming from Youtube

git init
git add .
git commit -m "Initial commit: Create Flask app structure"
git remote add origin https://github.com/YOUR_USERNAME/ai-image-generator.git
git branch -M main
git push -u origin main

