package leet.Array

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class AddSpacesTest {

    @Test
    fun testAddSpaces() {
        val solution = AddSpaces()
        val s = "LeetcodeHelpsMeLearn"
        val spaces = intArrayOf(8, 13, 15)
        val result = solution.addSpaces(s, spaces)
        assertEquals("Leetcode Helps Me Learn", result)
    }

    @Test
    fun testAddSpaces2() {
        val solution = AddSpaces()
        val s = "icodeinkotlin"
        val spaces = intArrayOf(1, 5, 7)
        val result = solution.addSpaces(s, spaces)
        assertEquals("i code in kotlin", result)
    }
}