/**
 * CodeWars Challenge: [Isograms]
 * Link: [https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/typescript]
 * Difficulty: [7 Kyu]
 *
 * Instructions
 * An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
 *
 * Example
 * "Dermatoglyphics" --> true
 * "aba" --> false
 * "moOse" --> false (ignore letter case)
 */

// # 1
const isIsogram = (str: string): boolean => {
  return new Set(str.toLowerCase()).size == str.length;
};

// # 2
// const isIsogram = (str: string): boolean => {
//   const lowercaseString = str.toLowerCase();

//   for (let i = 0; i < str.length; i++) {
//     if (
//       lowercaseString.indexOf(lowercaseString[i]) !==
//       lowercaseString.lastIndexOf(lowercaseString[i])
//     ) {
//       return false;
//     }
//   }
//   return true;
// };
