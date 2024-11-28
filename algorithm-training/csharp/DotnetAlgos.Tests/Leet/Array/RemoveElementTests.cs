using DotnetAlgos.Leet.Array;

namespace DotnetAlgos.Tests.Leet.Array
{
    public class RemoveElementTests
    {
        [Fact]
        public void Test_RemoveElement_ReturnsExpectedCount()
        {
            // Arrange
            var solution = new RemoveElementMatchingValue();
            int[] nums = { 3, 2, 2, 3 };
            int val = 3;

            // Act
            int result = solution.RemoveElement(nums, val);

            // Assert
            Assert.Equal(2, result);
            Assert.Equal(new[] { 2, 2 }, new ArraySegment<int>(nums, 0, result));
        }

        [Fact]
        public void Test_RemoveElement_ReturnsExpectedCount2()
        {
            // Arrange
            var solution = new RemoveElementMatchingValue();
            int[] nums = { 0, 1, 2, 2, 3, 0, 4, 2 };
            int val = 2;

            // Act
            int result = solution.RemoveElement(nums, val);

            // Assert
            Assert.Equal(5, result);
            Assert.Equal(new[] { 0, 1, 3, 0, 4 }, new ArraySegment<int>(nums, 0, result));
        }
    }
}