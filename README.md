# Flask Application Deployment Guide

This guide provides instructions for deploying a Flask application on a cPanel hosting environment.

## Fields Explanation

When setting up your Flask application on cPanel, you will need to fill in the following fields:

1. **Python Version**:
   - Specify the Python version that your application will use (e.g., `3.9`, `3.10`). Ensure that the selected version is supported by your hosting provider.

2. **Application Root**:
   - This is the directory path where your Flask application files are located on the server. Example: `/home/your_username/my_flask_app`.

3. **Application URL**:
   - The URL where your application will be accessible to users. This could be a domain like `mywebsite.com` or a subdomain such as `app.mywebsite.com`.

4. **Application Startup File**:
   - The name of the file that serves as the entry point for your Flask application. Common examples are `app.py` or `wsgi.py`.

5. **Application Entry Point**:
   - The WSGI callable for your Flask application, which tells the server how to start your app. The format is `startup_file:app_instance`, where:
     - `startup_file` is the name of your application’s startup file (without the `.py` extension).
     - `app_instance` is the Flask instance in your startup file. For example, if your startup file is `app.py` and your Flask instance is named `app`, this would be `app:app`.

6. **Environment Variables**:
   - Any environment-specific settings your application needs, such as:
     - `FLASK_ENV` to set the environment (`development` or `production`).
     - Database connection strings, API keys, etc.

## Example Configuration

- **Python Version**: 3.9+
- **Application Root**: `/home/your_username/my_flask_app`
- **Application URL**: `app.mywebsite.com`
- **Application Startup File**: `app.py`
- **Application Entry Point**: `app:app`

## Deployment Steps

1. Clone this repository to your server:
   ```bash
   git clone https://github.com/esubaalew/flask-cpanel.git
   cd flask-cpanel
