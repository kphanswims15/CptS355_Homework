/*
Kimi Phan
11466435
MacOs/Unix
*/

package BallGame;
import java.awt.*;
import java.util.*;
import java.applet.*;
import java.awt.event.MouseEvent;
import javax.swing.event.*;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import org.json.simple.JSONArray; 
import org.json.simple.JSONObject; 
import org.json.simple.parser.JSONParser; 
import org.json.simple.parser.ParseException; 

/*<applet code="Main" height=400 width=400></applet>*/


public class Main extends Applet implements Runnable
{

/* Configuration arguments. These should be initialized with the values read from the config.JSON file*/					
    private int numBalls;
/*end of config arguments*/

    private int refreshrate = 15;	           //Refresh rate for the applet screen. Do not change this value. 
	private boolean isStoped = true;		     
    Font f = new Font ("Arial", Font.BOLD, 18);
	
	private Player player;			           //Player instance.
	private Ball redball;                      //Ball instance. You need to replace this with an array of balls.     
	Thread th;						           //The applet thread. 
	  
    Cursor c;				
    private GameWindow gwindow;                 // Defines the borders of the applet screen. A ball is considered "out" when it moves out of these borders.
	private Image dbImage;
	private Graphics dbg;
	
	// ball variables
	ArrayList <Ball> ball_array = new ArrayList <Ball> ();
	
	class HandleMouse extends MouseInputAdapter 
	{

    	public HandleMouse() 
    	{
            addMouseListener(this);
        }
		
    	public void mouseClicked(MouseEvent e) 
    	{
        	if (!isStoped) {
        		for (Ball b: ball_array)
        		{
        			if (b.userHit (e.getX(), e.getY())) {
        				b.ballWasHit ();
        				if (b instanceof BounceBall)
        				{
        					player.updateNumberOfTimesHitBounceBall();
        				}
        				else if (b instanceof ShrinkBall)
        				{
        					player.updateNumberOfTimesHitShrinkBall();
        				}
        				else
        				{
        					player.updateNumberOfTimesHitBasic();
        				}
        			}
        		}
        		player.updateTotalClicks();
			}
			else if (isStoped && e.getClickCount() == 2) {
				isStoped = false;
				init ();
			}
    		
    	}

    	public void mouseReleased(MouseEvent e) 
    	{
           
    	}
        
    	public void RegisterHandler() 
    	{

    	}
    }
	
	HandleMouse hm = new HandleMouse();
	
	//JSON reader; you need to complete this function
	public void JSONReader()
	{
		final String filePath = "/Users/KimberleePhan/Desktop/BallGame_skeleton/config.JSON";
		
		try {
			FileReader reader = new FileReader(filePath);
			
			JSONParser jsonParser = new JSONParser();
			JSONObject jsonObject = (JSONObject) jsonParser.parse(reader);
			
			// Parsing GameWindow
			JSONObject gameWindow = (JSONObject) jsonObject.get("GameWindow");
			String x_Leftout = (String) gameWindow.get("x_leftout");
			int x_leftout = Integer.valueOf(x_Leftout);
			String x_Rightout = (String) gameWindow.get("x_rightout");
			int x_rightout = Integer.valueOf(x_Rightout);
			String y_Upout = (String) gameWindow.get("y_upout");
			int y_upout = Integer.valueOf(y_Upout);
			String y_Downout = (String) gameWindow.get("y_downout");
			int y_downout = Integer.valueOf(y_Downout);
			gwindow = new GameWindow(x_leftout, x_rightout, y_upout, y_downout);
			
			// Parsing Player
			JSONObject player = (JSONObject) jsonObject.get("Player");
			String num_lives = (String) player.get("numLives");
			int numLives = Integer.valueOf(num_lives);
			String score_2Earn_Life = (String) player.get("score2EarnLife");
			int score2EarnLife = Integer.valueOf(score_2Earn_Life);
			this.player = new Player (numLives, score2EarnLife);
			
			// number of balls
			String num_Balls = (String) jsonObject.get("numBalls");
			numBalls = Integer.valueOf(num_Balls);
			
			// Parsing ball
			JSONArray balls = (JSONArray) jsonObject.get("Ball");
			ball_array.clear();
			for (int i = 0; i < balls.size(); i++)
			{
				JSONObject ballObject = (JSONObject) balls.get(i);
				String Id = (String) ballObject.get("id");
				int id = Integer.valueOf(Id);
				String Radius = (String) ballObject.get("radius");
				int radius = Integer.valueOf(Radius);
				String init_Xpos = (String) ballObject.get("initXpos");
				int initXpos = Integer.valueOf(init_Xpos);
				String init_Ypos = (String) ballObject.get("initYpos");
				int initYpos = Integer.valueOf(init_Ypos);
				String speed_X = (String) ballObject.get("speedX");
				int speedX = Integer.valueOf(speed_X);
				String speed_Y = (String) ballObject.get("speedY");
				int speedY = Integer.valueOf(speed_Y);
				String max_ball_speed = (String) ballObject.get("maxBallSpeed");
				int maxBallSpeed = Integer.valueOf(max_ball_speed);
				JSONArray colorArray = (JSONArray) ballObject.get("color");
				String redString = (String) colorArray.get(0);
				String greenString = (String) colorArray.get(1);
				String blueString = (String) colorArray.get(2);
				int red = Integer.valueOf(redString);
				int green = Integer.valueOf(greenString);
				int blue = Integer.valueOf(blueString);
				Color color = new Color(red, green, blue);
				
				if (((String) ballObject.get("type")).equals("bounceball"))
				{
					String bounce_count = (String) ballObject.get("bounceCount");
					int bounceCount = Integer.valueOf(bounce_count);
					ball_array.add(new BounceBall(radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color, this.player, gwindow, bounceCount));
				}
				else if (((String) ballObject.get("type")).equals("shrinkball"))
				{
					String shrink_rate = (String) ballObject.get("shrinkRate");
					int shrinkRate = Integer.valueOf(shrink_rate);
					ball_array.add(new ShrinkBall(radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color, this.player, gwindow, shrinkRate));
				}
				else
				{
					ball_array.add(new Ball(radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color, this.player, gwindow));
				}
			}
		}
		catch (FileNotFoundException e)
		{
			e.printStackTrace();	
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/*initialize the game*/
	public void init ()
	{	
		//reads info from JSON doc
		this.JSONReader();
		c = new Cursor (Cursor.CROSSHAIR_CURSOR);
		this.setCursor (c);	
				
		setBackground (Color.black);
		setFont (f);

		if (getParameter ("refreshrate") != null) {
			refreshrate = Integer.parseInt(getParameter("refreshrate"));
		}
		else refreshrate = 15;
		
		/* The parameters for the GameWindow constructor (x_leftout, x_rightout, y_upout, y_downout) 
		should be initialized with the values read from the config.JSON file*/	
		this.setSize(gwindow.x_rightout, gwindow.y_downout); //set the size of the applet window.
		
		/*The skeleton code creates a single basic ball. Your game should support arbitrary number of balls. 
		* The number of balls and the types of those balls are specified in the config.JSON file.
		* The ball instances will be stores in an Array or Arraylist.  */
		/* The parameters for the Ball constructor (radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color) 
		should be initialized with the values read from the config.JSON file. Note that the "color" need to be initialized using the RGB values provided in the config.JSON file*/
		// redball = new Ball(15, 400, 500, 1, -1, 4, Color.red, player, gwindow)
		
		numBalls = 1;
		
	}
	
	/*start the applet thread and start animating*/
	public void start ()
	{		
		if (th==null){
			th = new Thread (this);
		}
		th.start ();
	}
	
	/*stop the thread*/
	public void stop ()
	{
		th=null;
	}

    
	public void run ()
	{	
		/*Lower this thread's priority so it won't interfere with other processing going on*/
		Thread.currentThread().setPriority(Thread.MIN_PRIORITY);

        /*This is the animation loop. It continues until the user stops or closes the applet*/
		while (true) {
			if (!isStoped) {
				for (Ball b : ball_array)
				{
					b.move();
				}
			}
            /*Display it*/
			repaint();
            
			try {
				
				Thread.sleep (refreshrate);
			}
			catch (InterruptedException ex) {
				
			}			
		}
	}

	
	public void paint (Graphics g)
	{
		/*if the game is still active draw the ball and display the player's score. If the game is active but stopped, ask player to double click to start the game*/ 
		if (!player.isGameOver()) {
			g.setColor (Color.yellow);
			
			g.drawString ("Score: " + player.getScore(), 10, 40);
			g.drawString("Lives: " + player.getNumLives(), 10, 70); // The player lives need to be displayed
			
			for (Ball b : ball_array)
			{
				b.DrawBall(g);
			}
			
			if (isStoped) {
				g.setColor (Color.yellow);
				g.drawString ("Doubleclick on Applet to start Game!", 40, 200);
			}
		}
		/*if the game is over (i.e., the ball is out) display player's score*/
		else {
			g.setColor (Color.yellow);
			g.drawString ("Game over!", 130, 100);
			g.drawString ("You scored " + player.getScore() + " Points!", 90, 140);
			g.drawString("Statistics: ", 400, 160);
			g.drawString("Number of Clicks: " + player.getTotalClicks(), 400, 180); // The number of clicks need to be displayed
			g.drawString("% of Successful Clicks: " + player.calculatePercentSuccessHits() + "%",400,200); // The % of successful clicks need to be displayed
			g.drawString("Ball most hit: " + player.mostHitBall(), 400, 240); // The nball that was hit the most need to be displayed
				
			g.drawString ("Doubleclick on the Applet, to play again!", 20, 220);

			isStoped = true;	
		}
	}

	
	public void update (Graphics g)
	{
		
		if (dbImage == null)
		{
			dbImage = createImage (this.getSize().width, this.getSize().height);
			dbg = dbImage.getGraphics ();
		}

		
		dbg.setColor (getBackground ());
		dbg.fillRect (0, 0, this.getSize().width, this.getSize().height);

		
		dbg.setColor (getForeground());
		paint (dbg);

		
		g.drawImage (dbImage, 0, 0, this);
	}
}


