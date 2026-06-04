import java.util.Scanner;
import java.util.Random; //1.Import the random tool

public class game{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        Random random = new Random();  //2. Create a random object

        //Generate a random no from 0 upto 99 then adds 1 to make it 1 to 100
        
        int secretNumber = random.nextInt(100)+1;
        int userGuess=0; // Variable to store what the user types
        int attempts=0; // Variable to count how many tries it takes

        System.out.print("=== Welcome to the Number Guessing Game! ===\n");
        System.out.print(" I have choosen a secret number between 1 and 100.\n");


        //3. The while loop keeps running asa long as the guess is wrong

        while(userGuess != secretNumber){
            System.out.print("Enter you guess:");
            userGuess=input.nextInt();
            attempts++; //Shortcut to add 1 to the no of attempts

            //4. Give clues to help the user

            if(userGuess > secretNumber){
                System.out.print("Too high! Try a lower number.");
            } else if(userGuess < secretNumber){
                System.out.print("Too low! Try a higher number.");
            } else{
                System.out.print("-----------------------------------------\n");
                System.out.print("Congratulations! You guessed the number!\n");
                System.out.printf("It took you exactly %d attempts.\n", attempts);
            }
        }

        input.close();
    }
}