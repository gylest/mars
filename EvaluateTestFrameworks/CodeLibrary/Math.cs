namespace CodeLibrary;

public static class Math
{
    public static int AddTwoNumbers(int a, int b)
    {
        return a + b;
    }

    public static int SubtractTwoNumbers(int a, int b)
    {
        return a - b;
    }

    public static int MultiplyTwoNumbers(int a, int b)
    {
        // Add a condition that should not be hit, to highlight for code coverage
        if (a < (-10000))
        {
            b = -100;
        }

        return a * b;
    }
}
