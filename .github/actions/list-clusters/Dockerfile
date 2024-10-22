FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY list_clusters.py /list_clusters.py
CMD ["python", "/list_clusters.py"]