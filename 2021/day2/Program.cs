Console.WriteLine("Hello, World!");

var file = "C:\\repos\\adventofcode\\day2\\input.txt";
string[] lines = System.IO.File.ReadAllLines(@file);

// Display the file contents by using a foreach loop.
// foreach (string line in lines)
// {
//     Console.WriteLine(line);
// }
// return 0;

List<string> input = new List<string>(lines);

var output = Dive.Depth(input);
Console.WriteLine(output);


var aim = Dive.Aim(input);
Console.WriteLine(aim);

