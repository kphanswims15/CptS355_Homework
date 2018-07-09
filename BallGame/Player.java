package BallGame;
public class Player
{
	
	private int score;			   //player score
	private int numLives; // player lives 
	private int score2EarnLifeConstant; // score to get lives constant
	private int score2EarnLife; // score to get lives 
	private boolean gameover=false;	
	// keeps track of number of times each ball is hit
	private int numberOfTimesHitBasic;
	private int numberOfTimesHitBounceBall;
	private int numberOfTimesHitShrinkBall;
	private int totalClicks; // keep tracks of total number of hits
	public int scoreConstant = 10; //This constant value is used in score calculation. You don't need to change this. 	

	
	public Player(int num_lives, int score_2Earn_Life)
	{
		score = 0; //initialize the score to 0
		numLives = num_lives; // get value from the json file somehow
		score2EarnLifeConstant = score_2Earn_Life; // get value from json file somehow
		score2EarnLife = score_2Earn_Life;
	}

	/* get player score*/
	public int getScore ()
	{
		return score;
	}
	
	/* get number of lives */
	public int getNumLives ()
	{
		return numLives;
	}
	
	/* get number to score to earn lives */
	public int getScore2EarnLife ()
	{
		return score2EarnLife;
	}
	
	/* gets number of hits for each ball */
	public int getNumberOfTimesHitBasic ()
	{
		return numberOfTimesHitBasic;
	}
	
	public int getNumberOfTimesHitBounceBall ()
	{
		return numberOfTimesHitBounceBall;
	}
	
	public int getNumberOfTimesHitShrinkBall ()
	{
		return numberOfTimesHitShrinkBall;
	}
	
	/* get the number of total clicks */
	public int getTotalClicks ()
	{
		return totalClicks;
	}
	
	/*check if the game is over*/
	public boolean isGameOver ()
	{
		return gameover;
	}

	/*update player score*/
	public void addScore (int plus)
	{
		score += plus;
	}

	/*update "game over" status*/
	public void gameIsOver ()
	{
		gameover = true;
	}
	
	/* decrements number of lives */
	public void decrementLives ()
	{
		numLives--;
	}
	
	/* add lives after the score 2 earn life is met */
	public void addLives()
	{
		numLives++;
	}
	
	/* updates the score to earn life after a life is earned */
	public void updateScore2EarnLife ()
	{
		score2EarnLife = score2EarnLife + score2EarnLifeConstant;
	}
	
	/* updates the number of times hit for the basic ball */
	public void updateNumberOfTimesHitBasic ()
	{
		numberOfTimesHitBasic++;
	}
	
	/* updates the number of times hit for bounce ball */
	public void updateNumberOfTimesHitBounceBall ()
	{
		numberOfTimesHitBounceBall++;
	}
	
	/* updates the number of times hit for bounce ball */
	public void updateNumberOfTimesHitShrinkBall ()
	{
		numberOfTimesHitShrinkBall++;
	}
	
	/* updates the total number of clicks */
	public void updateTotalClicks ()
	{
		totalClicks++;
	}
	
	/* calculates percent of success hits */
	public double calculatePercentSuccessHits ()
	{
		return ((numberOfTimesHitBasic + numberOfTimesHitBounceBall + numberOfTimesHitShrinkBall) / (double)totalClicks) * 100; 
	}
	
	public String mostHitBall ()
	{
		int mostBallHit = Math.max(numberOfTimesHitBasic, Math.max(numberOfTimesHitBounceBall, numberOfTimesHitShrinkBall));
		if (mostBallHit == numberOfTimesHitBasic)
		{
			return "Basic Ball";
		}
		else if (mostBallHit == numberOfTimesHitBounceBall)
		{
			return "Bounce Ball";
		}
		else
		{
			return "Shrink Ball";
		}
	}
}