using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;

namespace MSTestFramework
{
    [TestClass]
    public class Tests
    {
        int actual = 0;

        // Called once before all tests
        [ClassInitialize]
        public static void ClassInitialize(TestContext context)
        {
            if (context != null)
            {
                Debug.WriteLine($"ClassInitialize: Test Name = {context.TestName}");
            }
        }

        // Called once after all tests
        [ClassCleanup]
        public static void ClassCleanup()
        {
            Debug.WriteLine("ClassCleanup");
        }


        [TestMethod]
        public void TestAddTwoNumbers1()
        {
            actual = CodeLibrary.Math.AddTwoNumbers(6, 7);

            // Check
            Assert.AreEqual( 13, actual);
        }

        [TestMethod]
        public void TestAddTwoNumbers2()
        {
            actual = CodeLibrary.Math.AddTwoNumbers(11, 12);

            // Check
            Assert.AreEqual( 23, actual);
        }

        [TestMethod]
        public void TestSubtractTwoNumbers1()
        {
            actual = CodeLibrary.Math.SubtractTwoNumbers(99, 22);

            // Check
            Assert.AreEqual( 77, actual);
        }

        // Parameterised test
        [DataRow(99, 5, 495)]
        [DataRow(17, 49, 833)]
        [DataTestMethod]
        public void TestMultiplyTwoNumbers(int number1, int number2, int expectedResult)
        {
            actual = CodeLibrary.Math.MultiplyTwoNumbers(number1, number2);

            // Check
            Assert.AreEqual( expectedResult, actual);
        }

        [TestMethod]
        public void TestJson1()
        {
            string jsonSimpleString = @"{""Name"":""Rick"",""Company"":""West Wind"",""Entered"":""2012-03-16T00:03:33.245-10:00""}";

            // Check
            Assert.AreEqual("West Wind", CodeLibrary.JsonHelper.GetCompany(jsonSimpleString));
        }
    }
}
