/**
 * CodeWars Challenge: [Validate PIN]
 * Link: [https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/typescript]
 * Difficulty: [7 Kyu]
 *
 * Instructions:
 * ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false.
 *
 * Examples:
 * "1234"   ->  true
 * "12345"  ->  false
 * "a234"   ->  false
 **/

// # 1 Using regular expression (regex)
const validatePin = (pin: string): boolean => {
  return /^(\d{4}|\d{6})$/.test(pin);
};

// # 2 Or, create the same regex with the RegExp constructor. But, harder to read (need to double-escape backslashes). Usually only needed when building regex dynamically from a string.

// const validatePin = (pin: string): boolean => {
//   const acceptedFormat = new RegExp("^(\\d{4}|\\d{6})$");
//   return acceptedFormat.test(pin);
// };

// # 3 Using .every()

// const validatePin = (pin: string): boolean => {
//   if (pin.length !== 6 && pin.length !== 4) return false;

//   return [...pin].every((ch) => ch >= "0" && ch <= "9");
// };

// const validatePin = (pin: string): boolean => {
// 	return [...pin].every((ch) => ch >= "0" && ch <= "9") && (pin.length === 4 || pin.length === 6);
//   };

// # 4 - for loop and .charCodeAt()

// const validatePin = (pin: string): boolean => {
//   if (pin.length !== 6 && pin.length !== 4) return false;

//   for (let i = 0; i < pin.length; i++) {
//     if (!(pin.charCodeAt(i) >= 48 && pin.charCodeAt(i) <= 57)) return false;
//   }
//   return true;
// };
