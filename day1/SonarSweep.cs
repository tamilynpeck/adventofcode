using System;
using System.Collections.Generic;

public static class SonarSweep
{
    public static int Score()
    {
        var file = "C:\\repos\\adventofcode\\day1\\input.txt";
        string[] lines = System.IO.File.ReadAllLines(@file);

        // Display the file contents by using a foreach loop.
        System.Console.WriteLine("Contents of WriteLines2.txt = ");
        foreach (string line in lines)
        {
            // Use a tab to indent each line of the file.
            Console.WriteLine("\t" + line);
        }
        return 0;
    }
}