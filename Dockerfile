FROM python:3.12-alpine
WORKDIR /stage
COPY . .
RUN pip install . && \
    pip cache purge && \
    rm -rf /stage && \
    rm -rf /root/.cache
ENTRYPOINT [ "altercase" ]
