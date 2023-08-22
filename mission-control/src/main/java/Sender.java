import com.greeting.Greet;
import com.rabbitmq.client.AMQP.BasicProperties;

import generated.Location;
import generated.VehicleAttitude;
import generated.VehicleStatus;
import generated.VehicleVelocity;

import com.rabbitmq.client.Channel;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Random;
import java.util.concurrent.TimeoutException;
import java.util.zip.DeflaterOutputStream;

public class Sender {
    public Channel channel;

    public Sender(Channel c) {
        this.channel = c;
    }

    public void send() throws IOException, TimeoutException {
        double start1 = -43;
        double end1 = -45;
        double random1 = new Random().nextDouble();
        double result1 = start1 + (random1 * (end1 - start1));

        double start2 = 76;
        double end2 = 78;
        double random2 = new Random().nextDouble();
        double result2 = start2 + (random2 * (end2 - start2));

        // Converts to VehicleStatus protobuf message
        
        Location locationMessage = Location.newBuilder().
                setLat(result1).
                setLong(result2).
                setAlt((float) 35.3).
                build();

        start1 = 10;
        end1 = 15;
        random1 = new Random().nextDouble();
        result1 = start1 + (random1 * (end1 - start1));

        start2 = 0;
        end2 = 1;
        random2 = new Random().nextDouble();
        result2 = start2 + (random2 * (end2 - start2));

        VehicleAttitude attitudeMessage = VehicleAttitude.newBuilder().
            setPitch(result1).
            setYaw(result2).
            setRoll(12).
            build();
        
        start1 = 10;
        end1 = 15;
        random1 = new Random().nextDouble();
        result1 = start1 + (random1 * (end1 - start1));

        start2 = 3;
        end2 = 6;
        random2 = new Random().nextDouble();
        result2 = start2 + (random2 * (end2 - start2));

        VehicleVelocity velocityMessage = VehicleVelocity.newBuilder().
            setX((float) result1).
            setY((float)result2).
            setZ(0).
            build();

        VehicleStatus vehicleStatus = VehicleStatus.newBuilder().
            setLocation(locationMessage).
            setVelocityXYZ(velocityMessage).
            setAttitude(attitudeMessage).
            setStatus("Executing").
            build();

        BasicProperties props = new BasicProperties();
        props = props.builder().type("status").build();

        ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
        DeflaterOutputStream outputStream = new DeflaterOutputStream(byteStream);
        try {
            outputStream.write(vehicleStatus.toByteArray(), 0, vehicleStatus.toByteArray().length);
            outputStream.finish();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        channel.basicPublish("ui-exchange", "status", props, byteStream.toByteArray());
        System.out.println("Message sent");
    }
}
