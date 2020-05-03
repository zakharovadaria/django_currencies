FROM python:3
RUN mkdir /build
WORKDIR /build
EXPOSE 8000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD honcho start
