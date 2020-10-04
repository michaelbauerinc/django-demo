FROM static_ubuntu
RUN apt-get update
WORKDIR /app
COPY . .
RUN apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev libpng-dev -y
RUN sh ./utils/install-python-pip.sh
RUN python ./utils/create_db.py
RUN sh ./utils/create-admin-user.sh
EXPOSE 8000
# Email Port
EXPOSE 587
CMD ["sh", "start.sh"]