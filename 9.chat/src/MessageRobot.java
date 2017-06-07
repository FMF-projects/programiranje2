import java.util.Timer;
import java.util.TimerTask;

public class MessageRobot extends TimerTask {
	private ChatFrame chat;
	private Timer timer;
	
	
	public MessageRobot(ChatFrame chat) {
		this.chat = chat;
	}
	

	/**
	 * Activate the robot!
	 */
	public void activate() {
		Timer timer = new Timer();
		timer.scheduleAtFixedRate(this, 5000, 1000);
	}
	
	public void deactivate(){
		timer.cancel();
	}
	
	@Override
	public void run() {
		//sporocila s streznika
	}
}
