import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your weight in kilograms: ");
        double weight = input.nextDouble();
        
        System.out.print("Enter your height in meters (e.g., 1.75): ");
        double height = input.nextDouble();
        
        // Formula: weight / (height * height)
        double bmi = weight / (height * height);
        
        System.out.println("--------------------------------");
        System.out.printf("Your exact BMI score is: %.1f\n", bmi);
        
        // Using basic if-else logic to give meaning to the math result
        if (bmi < 18.5) {
            System.out.println("Weight Status: Underweight");
        } else if (bmi >= 18.5 && bmi < 25.0) {
            System.out.println("Weight Status: Healthy Weight");
        } else {
            System.out.println("Weight Status: Overweight");
        }
        
        input.close();
    }
}

