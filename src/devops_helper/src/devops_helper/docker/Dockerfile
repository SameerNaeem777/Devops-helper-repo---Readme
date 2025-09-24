FROM python:3.11-slim
WORKDIR /app


# copy only what's needed
COPY pyproject.toml requirements.txt ./
COPY src/ ./src/


RUN pip install --upgrade pip && pip install -r requirements.txt && rm -rf /root/.cache/pip


ENTRYPOINT ["python", "-m", "src.devops_helper.cli"]
