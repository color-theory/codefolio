package utils

import kotlin.js.Json

actual object FileReader {
    actual fun readFile(path: String): String {
        val fs = js("require('fs')")
        return fs.readFileSync(path, "utf8") as String
    }

    actual fun fileExists(path: String): Boolean {
        val fs = js("require('fs')")
        return fs.existsSync(path) as Boolean
    }
}