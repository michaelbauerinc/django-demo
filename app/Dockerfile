FROM static_ubuntu
RUN apt-get update
WORKDIR /app
COPY . .
RUN sh ./utils/install-python-pip.sh
EXPOSE 8000
CMD ["sh", "start.sh"]