FROM python:3.9-slim-buster

ADD frasiervision.py .
ADD script_scraper.py .
ADD script_loader.py .
ADD script_chat.py .

COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "./frasiervision.py"]