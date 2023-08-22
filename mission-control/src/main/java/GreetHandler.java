import com.greeting.Greet;


public class GreetHandler {
    Greet greeting; 

    public GreetHandler(Greet greeting){
        this.greeting = greeting;
        Handler();
    }

    public void Handler(){
        System.out.printf("Greet Handler \n Username - %s \n Greeting - %s \n", greeting.getUsername(), greeting.getGreeting());
    }
}
