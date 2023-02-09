import java.io.IOException;
import java.util.Timer;
import java.util.TimerTask;
import java.util.Random;

public class createdata {

    public static int record = 0;
    public static void main(String[] args) throws IOException {
        Recorder creationtool = new Recorder("openai");
        creationtool.clearFile();

        Timer timer = new Timer();
        
         

        
        TimerTask T = new TimerTask() {

            Random number = new Random();

            @Override
            public void run() {
                record ++ ;
                String string = ""+record+ ","+number.nextInt(100);

        
                try {
                    creationtool.saveValue(string);
                } 
                
                
                
                catch (IOException e) {
                    e.printStackTrace();
                }
            };
                
        };
        
        

        timer.scheduleAtFixedRate(T, 1000, 1000);

    }

    public static void stop(){
        System.exit(0);

    }
}
