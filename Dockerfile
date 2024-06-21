FROM rezah65/djbase:5.0.6

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR /src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/development.txt

RUN mkdir -p /vol/web/media && \
    chmod -R +x /scripts && \
    adduser --disabled-password --no-create-home librishop && \
    chown -R librishop:librishop /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER librishop

CMD ["run.sh"]