class A{
    A()
    {//this and super should always be used at the top.
      this(2);//to invoke parmeterized contructor from non-parameterized constructor.
      System.out.println("A non-parameterized");
    }
    A(int x)
    {
      //calling non-parameterized constructor from parameterized constructor using this keyword.
      //this();//this is a refrence keyword which refers to the object of the class.
      System.out.println("A parameterized "+x);
    }
  }
  public class Test{
    public static void main(String[] args) {
      A a=new A();
    }
  }
  //recursion is not possible in constructor.