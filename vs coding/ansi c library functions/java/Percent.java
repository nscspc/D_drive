import java.util.Scanner;
class Percent{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        
        System.out.println("how many subjects marks you want to enter : ");
        int n=s.nextInt();
        int i;
        float marks;
        float total_marks=0;
        for(i=1;i<=n;i++)
        {
            System.out.println("enter marks : ");
            marks=s.nextFloat();
            total_marks+=marks;
        }
        System.out.println("Total marks : "+total_marks+"\nPercentage = "+total_marks/n);

    }
}