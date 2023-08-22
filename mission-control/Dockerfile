FROM maven:3.6.0-jdk-11-slim AS build
COPY src /home/app/src
COPY pom.xml /home/app
WORKDIR /home/app
RUN mvn -f pom.xml clean package

ENTRYPOINT ["mvn","exec:java"]
