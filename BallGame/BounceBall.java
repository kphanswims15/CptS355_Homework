package BallGame;

import java.awt.Color;

public class BounceBall extends Ball {

	int bounceCount;
	int bounceCountConst;
	public BounceBall(int radius, int initXpos, int initYpos, int speedX, int speedY, int maxBallSpeed, Color color,
			Player player, GameWindow gameW, int bounceCount) {
		super(radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color, player, gameW);
		this.bounceCount = bounceCount;
		bounceCountConst = bounceCount;
	}
	
	protected void resetBallPosition()
	{
		pos_x = first_x;
		pos_y = first_y;
		bounceCount = bounceCountConst;
	}
	
	protected boolean isOut ()
	{
		if ((pos_x < gameW.x_leftout) || (pos_x > gameW.x_rightout) || (pos_y < gameW.y_upout) || (pos_y > gameW.y_downout))
		{
			if (bounceCount == 0) 
			{
				return super.isOut();
			}
			
			bounceCount--;
			
			// makes the ball bounce off the walls
			// ball hits the left or right wall 
			if (pos_x < gameW.x_leftout || pos_x > gameW.x_rightout) 
			{
				// flips the direction of x
				x_speed = x_speed * -1;
			}
			
			// ball hits the top or bottom
			if (pos_y < gameW.y_upout || pos_y > gameW.y_downout)
			{
				// flips the direction of y
				y_speed = y_speed * -1;
			}
			
			return true;
		}
		
		return false;
	}
}
