package main

func toLowerCase(c byte) byte {
	if c >= 65 && c <= 90 {
		return c + 32
	}
	return c
}

func isPunctuation(c byte) bool {
	if (c >= 32 && c <= 47) || (c >= 58 && c <= 64) || (c >= 91 && c <= 96) || (c >= 123 && c <= 126) {
		return true
	}
	return false
}

func isPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		if isPunctuation(s[i]) {
			i++
			continue
		}

		if isPunctuation(s[j]) {
			j--
			continue
		}

		if toLowerCase(s[i]) == toLowerCase(s[j]) {
			i++
			j--
		} else {
			return false
		}
	}

	return true
}

func main() {
	println(isPalindrome("A man, a plan, a canal: Panama"))
	println(isPalindrome("race a car"))
	println(isPalindrome(" "))
}
