package utils

import kotlin.test.Test
import kotlin.test.assertTrue
import kotlin.test.assertEquals
import kotlin.js.Promise

class FileReaderTest {

    @Test
    fun testReadFile() {
        val fs = js("require('fs')")
        val path = js("require('path')")

        val dirname = js("__dirname") as String

        val testFilePath = path.resolve(dirname, "jstest.txt")
        val content = FileReader
            .readFile(testFilePath)
            .trim()
        assertEquals("Hello, node.js!", content)
    }
}

