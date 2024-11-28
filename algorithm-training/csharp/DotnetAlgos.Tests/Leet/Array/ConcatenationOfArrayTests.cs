using DotnetAlgos.Leet.Array;

namespace DotnetAlgos.Tests.Leet.Array;

public class ConcatenationOfArrayTests
{
    [Fact]
    public void Test_GetConcatenation_ReturnsExpectedArray()
    {
        // Arrange
        var solution = new ConcatenationOfArray();
        int[] nums = { 1, 2, 1 };

        // Act
        int[] result = solution.GetConcatenation(nums);

        // Assert
        Assert.Equal(new[] { 1, 2, 1, 1, 2, 1 }, result);
    }

    [Fact]
    public void Test_GetConcatenation_ReturnsExpectedArray2()
    {
        // Arrange
        var solution = new ConcatenationOfArray();
        int[] nums = { 1, 3, 2, 1 };

        // Act
        int[] result = solution.GetConcatenation(nums);

        // Assert
        Assert.Equal(new[] { 1, 3, 2, 1, 1, 3, 2, 1 }, result);
    }
}