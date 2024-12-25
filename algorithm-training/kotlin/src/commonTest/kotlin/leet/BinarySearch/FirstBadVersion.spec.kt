package leet.BinarySearch

import kotlin.test.assertEquals
import kotlin.test.Test

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