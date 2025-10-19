namespace XUnitFramework;

public class Tests
{
    int result = 0;

    public Tests()
    {
    }

    [Fact]
    public void TestAddTwoNumbers1()
    {
        result = CodeLibrary.Math.AddTwoNumbers(6, 7);

        // Check
        Assert.Equal(13, result);
    }

    [Fact]
    public void TestAddTwoNumbers2()
    {
        result = CodeLibrary.Math.AddTwoNumbers(11, 12);

        // Check
        Assert.Equal(23, result);
    }

    [Fact]
    public void TestSubtractTwoNumbers1()
    {
        result = CodeLibrary.Math.SubtractTwoNumbers(99, 22);

        // Check
        Assert.Equal(77, result);
    }

    // Parameterised test
    [Theory]
    [InlineData(99, 22, 2178)]
    [InlineData(10, 100, 1000)]
    public void TestMultiplyTwoNumbers(int number1, int number2, int expectedResult)
    {
        result = CodeLibrary.Math.MultiplyTwoNumbers(number1, number2);

        // Check
        Assert.Equal(expectedResult, result);
    }

    [Fact]
    public void TestJson1()
    {
        string jsonSimpleString = @"{""Name"":""Rick"",""Company"":""West Wind"",""Entered"":""2012-03-16T00:03:33.245-10:00""}";

        // Check
        Assert.Equal("West Wind", CodeLibrary.JsonHelper.GetCompany(jsonSimpleString));
    }

    [Fact]
    public void TestSelenium1()
    {
        // This is new style using statement from C# 8. Dispose method is called automatically at end
        using IWebDriver driver = new OpenQA.Selenium.Chrome.ChromeDriver();

        Uri uri = new Uri("http://www.python.org");
        driver.Navigate().GoToUrl(uri);

        Assert.Contains("Python", driver.Title, StringComparison.CurrentCulture);

        var elem = driver.FindElement(By.Name("q"));
        elem.SendKeys("pycon");
        elem.SendKeys(Keys.Return);

        Assert.NotEqual("No results found.", driver.PageSource);
    }
}
