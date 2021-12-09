FROM python

RUN mkdir /home/app

COPY /app /home/app

WORKDIR /home/app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]