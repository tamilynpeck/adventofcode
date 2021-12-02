using Xunit;

public class ScrabbleScoreTests
{
    [Fact]
    public void get_output()
    {
        Assert.Equal(1, SonarSweep.Score());
    }
}