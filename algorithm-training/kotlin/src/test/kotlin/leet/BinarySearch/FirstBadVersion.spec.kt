package leet.BinarySearch

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class FirstBadVersionTest {

    @Test
    fun testFirstBadVersion() {
        // Mock the isBadVersion function
        val isBadVersion: (Int) -> Boolean = { version ->
            version >= 4 // Example: the first bad version is 4
        }

        val solution = FirstBadVersion()
        val n = 5 // Example: total versions

        // Verify that the first bad version is correctly identified
        val result = solution.firstBadVersion(n, isBadVersion)
        assertEquals(4, result)
    }
}