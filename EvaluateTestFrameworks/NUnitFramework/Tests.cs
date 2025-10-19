namespace NUnitFramework;

public class Tests
{
    int result     = 0;

    // This is called once for all child test cases
    [OneTimeSetUp]
    public void OneTimeSetup()
    {
    }

    // This is called once after all child test cases run
    [OneTimeTearDown]
    public void OneTimeTearDown()
    {
    }

    //
    // Called before child test case
    //
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void TestAddTwoNumbers1()
    {
        result = CodeLibrary.Math.AddTwoNumbers(6, 7);

        // Check
        Assert.That( result, Is.EqualTo(13)); // NUnit preferred over Assert.AreEqual()
    }

    [Test]
    public void TestAddTwoNumbers2()
    {
        result = CodeLibrary.Math.AddTwoNumbers(11, 12);

        // Check
        Assert.That(result, Is.EqualTo(23));
    }

    [Test]
    public void TestSubtractTwoNumbers1()
    {
        result = CodeLibrary.Math.SubtractTwoNumbers(99, 22);

        // Check
        Assert.That(result, Is.EqualTo(77));
    }

    // Parameterized test
    [TestCase(99, 22,  2178)]
    [TestCase(10, 100, 1000)]
    [TestCase(17, 3,   51)]
    public void TestMultiplyTwoNumbers(int number1, int number2, int expectedResult)
    {
        result = CodeLibrary.Math.MultiplyTwoNumbers(number1, number2);

        // Check
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void TestJson1()
    {
        string jsonSimpleString = @"{""Name"":""Rick"",""Company"":""West Wind"",""Entered"":""2012-03-16T00:03:33.245-10:00""}";

        // Check
        Assert.That(CodeLibrary.JsonHelper.GetCompany(jsonSimpleString), Is.EqualTo("West Wind"));
    }
}
