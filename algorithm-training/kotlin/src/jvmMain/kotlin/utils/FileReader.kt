package utils

import java.io.File

actual object FileReader {
    actual fun readFile(path: String): String {
        val file = File(path)
        if (!file.exists()) throw IllegalArgumentException("File not found: $path")
        return file.readText()
    }

    actual fun fileExists(path: String): Boolean {
        return File(path).exists()
    }
}