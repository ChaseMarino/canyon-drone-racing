# run 
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management\
mvn clean package (mvn clean install: first time or changes to pom dependencies)\
mvn exec:java

view ui at localhost:15672 (guest/guest) or look at logs to verify success 

# Regenerate Protobuf Files
protoc --java_out=src/main/java/ src/main/java/proto/greeting.proto