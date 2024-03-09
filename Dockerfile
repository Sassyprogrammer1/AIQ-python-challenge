FROM python:latest
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000