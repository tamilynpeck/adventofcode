using System;
using System.Collections.Generic;

public static class Dive
{
    public static int Depth(List<string> input)
    {

        var depth = 0;
        var horizontal = 0;

        foreach (string line in input)
        {
            // Console.WriteLine(line);
            var direction = line.Split(" ");
            if (direction[0] == "forward")
            {
                horizontal += Int32.Parse(direction[1]);
            }
            if (direction[0] == "down")
            {
                depth += Int32.Parse(direction[1]);
            }
            if (direction[0] == "up")
            {
                depth -= Int32.Parse(direction[1]);
            }
        }
        return depth * horizontal;
    }

    public static int Aim(List<string> input)
    {

        var aim = 0;
        var depth = 0;
        var horizontal = 0;

        foreach (string line in input)
        {
            // Console.WriteLine(line);
            var direction = line.Split(" ");
            if (direction[0] == "forward")
            {
                horizontal += Int32.Parse(direction[1]);
                depth += aim * Int32.Parse(direction[1]);
            }
            if (direction[0] == "down")
            {
                aim += Int32.Parse(direction[1]);
            }
            if (direction[0] == "up")
            {
                aim -= Int32.Parse(direction[1]);
            }
        }
        return depth * horizontal;
    }

}

// down X increases your aim by X units.
// up X decreases your aim by X units.
// forward X does two things:
// It increases your horizontal position by X units.
// It increases your depth by your aim multiplied by X.