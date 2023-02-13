FROM python:3.7-slim
WORKDIR /app
COPY ./qortex_music .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir 
CMD ["gunicorn", "qortex_music.wsgi:application", "--bind", "0:8000" ]