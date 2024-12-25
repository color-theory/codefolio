package utils

import kotlin.test.Test
import kotlin.test.assertEquals

class FileReaderTests {
    @Test
    fun testReadFile() {
        val path = "src/jvmTest/resources/jvmtest.txt"
        val content = FileReader.readFile(path)
        assertEquals("Hello, jvm!", content)
    }
}