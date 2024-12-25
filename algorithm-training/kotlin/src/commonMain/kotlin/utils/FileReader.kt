package utils

expect object FileReader {
    fun readFile(path: String): String
    fun fileExists(path: String): Boolean
}