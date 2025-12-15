FROM python:3.13-slim

WORKDIR /app
ENV PYTHONPATH=/app/src

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./src ./src
COPY alembic.ini /app/alembic.ini

EXPOSE 9000

CMD ["python", "-m", "src.main"]