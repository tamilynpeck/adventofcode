using Xunit;

public class DevTests
{
    [Fact]
    public void small_depth_dive()
    {
        List<string> input = new List<string>
        {
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        };

        Assert.Equal(150, Dive.Depth(input));
    }

    [Fact]
    public void small_aim_dive()
    {
        List<string> input = new List<string>
        {
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        };

        Assert.Equal(900, Dive.Aim(input));
    }
}