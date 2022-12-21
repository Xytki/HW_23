FROM python:3.9

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]

