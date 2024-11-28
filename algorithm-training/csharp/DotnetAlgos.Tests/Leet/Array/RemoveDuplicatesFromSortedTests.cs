using DotnetAlgos.Leet.Array;

namespace DotnetAlgos.Tests.Leet.Array
{
    public class RemoveDuplicatesFromSortedTests
    {
        [Fact]
        public void Test_RemoveDuplicates_ReturnsExpectedCount()
        {
            // Arrange
            var solution = new RemoveDuplicatesFromSorted();
            int[] nums = { 1, 1, 2 };

            // Act
            int result = solution.RemoveDuplicates(nums);

            // Assert
            Assert.Equal(2, result);
            Assert.Equal(new[] { 1, 2 }, new ArraySegment<int>(nums, 0, result));
        }


        [Fact]
        public void Test_RemoveDuplicates_ReturnsExpectedCount2()
        {
            // Arrange
            var solution = new RemoveDuplicatesFromSorted();
            int[] nums = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };

            // Act
            int result = solution.RemoveDuplicates(nums);

            // Assert
            Assert.Equal(5, result);
            Assert.Equal(new[] { 0, 1, 2, 3, 4 }, new ArraySegment<int>(nums, 0, result));
        }

    }
}