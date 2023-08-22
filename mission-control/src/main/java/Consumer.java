import com.greeting.Greet;
import com.rabbitmq.client.Channel;

import java.io.IOException;
import java.util.concurrent.TimeoutException;


public class Consumer {
    public Channel channel;

    public Consumer(Channel c) {
        this.channel = c;
    }

    public void consume() throws IOException, TimeoutException {
        channel.basicConsume("Test-Queue", true, (consumerTag, message) -> {

            String type = message.getProperties().getType();

            System.out.println(type);

            switch (type) {
                case "greeting":
                    new GreetHandler(Greet.newBuilder().mergeFrom(message.getBody()).build());
                    break;
                case "person":
                    break;
            }

        }, consumerTag -> {
        });
    }


}

