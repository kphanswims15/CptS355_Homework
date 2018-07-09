package BallGame;

import java.awt.Color;

public class ShrinkBall extends Ball {
	
	int shrinkRate;
	int radiusConst;
	int scoreMult = 1;
	
	/* Constructor */
	public ShrinkBall(int radius, int initXpos, int initYpos, int speedX, int speedY, int maxBallSpeed, Color color,
			Player player, GameWindow gameW, int shrinkRate) {
		super(radius, initXpos, initYpos, speedX, speedY, maxBallSpeed, color, player, gameW);
		this.shrinkRate = shrinkRate;
		radiusConst = radius;
	}
	
	public boolean userHit (int maus_x, int maus_y)
	{
		
		double x = maus_x - pos_x;
		double y = maus_y - pos_y;

		double distance = Math.sqrt ((x*x) + (y*y));
		
		if (Double.compare(distance-this.radius , player.scoreConstant + Math.abs(x_speed)) <= 0)  {
			player.addScore (scoreMult * (int)(player.scoreConstant * Math.abs(x_speed) + player.scoreConstant));
			radius = (int)((1 - shrinkRate/100.0) * radius);
			if (radius < 0.3 * radiusConst)
			{
				radius = radiusConst;
				scoreMult = 1;
			}
			
			scoreMult *= 2;
			
			if (player.getScore() >= player.getScore2EarnLife())
			{
				player.addLives();
				player.updateScore2EarnLife();
			}
			
			// changes the speed and direction once the ball is hit
			x_speed = (rand.nextInt(maxspeed + 1 + maxspeed) - maxspeed);
			y_speed = (rand.nextInt(maxspeed + 1 + maxspeed) - maxspeed);
			
			return true;
		}
		else return false;
	}
}
