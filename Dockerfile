# FOR UBUNTU SERVER
FROM ubuntu:20.04
RUN DEBIAN_FRONTEND=noninteractive

# Set timezone:
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Install dependencies:
RUN apt-get update && apt-get install -y tzdata

RUN apt-get update && apt-get install -y keyboard-configuration

RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get install python3.10 -y
RUN sudo apt-get install python3-pip -y

# Sets the working directory in the container  
COPY . /app

# WORKDIR /app
WORKDIR /app

# Copies the dependency files to the working directory
# COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copies everything to the working directory
# COPY . /app
# Command to run on container start    
ENTRYPOINT ["python3"]
CMD ["app.py"]
