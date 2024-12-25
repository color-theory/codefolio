package leet.Array

import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.assertEquals

class ClimbStairsTest {
    
    @Test
    fun testClimbStairs() {
        val solution = ClimbStairs()
        val n = 2
        val result = solution.climbStairs(n)
        assertEquals(2, result)
    }

    @Test
    fun testClimbStairs2() {
        val solution = ClimbStairs()
        val n = 3
        val result = solution.climbStairs(n)
        assertEquals(3, result)
    }

    @Test
    fun testClimbStairs3() {
        val solution = ClimbStairs()
        val n = 4
        val result = solution.climbStairs(n)
        assertEquals(5, result)
    }
}