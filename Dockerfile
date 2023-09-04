FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
COPY pyproject.toml \
     Makefile \
    /code/

# install poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.6.1

ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN make deps-prod

COPY . /code/
COPY ./entrypoint.sh /entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
