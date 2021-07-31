# Eleos test app

This is the Eleos test app.

These are the steps to run the Flask web service using Python:

1. Verify Python3 is installed on your machine: 
Run `python --version`

2. Verify pip is installed on your machine:
Run `pip --version` 
If it's not installed, use the instructions here: https://pip.pypa.io/en/stable/installation/

3. Create a Python virtual environment to run the application: 
`python -m venv eleos_venv
`
4. Activate the created virtual environment:
`source eleos_venv/bin/activate`

5. Install all the needed requirements for this app:
`pip install -r requirements.txt
`
6. Add the Zoom API token to your path:
`export ZOOM_TOKEN="<token>"
`
7. Run the Eleos test app:
`python src/main.py
`
8. Using the browser go to `http://<your_local_ip>/index`
Enjoy!

------------

These are the steps to run the Flask web service using Docker

1. Build the docker image:
`docker build -t eleos_test_image .`

2. Add the Zoom API token to your path:
`export ZOOM_TOKEN="<token>"

3. Run the created Docker image using the following command:
`docker run --env ZOOM_TOKEN=$ZOOM_TOKEN -dp 80:80 eleos_test_image`

![alt text](https://raw.githubusercontent.com/pavelzag/Eleos/main/images/screenshot1.png)


