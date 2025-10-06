using Newtonsoft.Json.Linq;
using System;
using System.Diagnostics;

namespace CodeLibrary
{
    public static class JsonHelper
    {
        public static string GetCompany(string jsonString)
        {
            //
            // Dynamic Deserialization - Simple JSON to Values
            //

            dynamic json = JValue.Parse(jsonString);

            // json values
            string name = json.Name;
            string company = json.Company;
            DateTime entered = json.Entered;

            // Show parse result
            Debug.WriteLine($"JSON Parse Results: Name = {name}, Company = {company}, Entered = {entered}");

            // return 
            return company;
        }
    }
}
