// CodeWars Challenge: [Abbreviate a Two Word Name]
// Link: [https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/typescript]
// Difficulty: [8 Kyu]

// Instructions
// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them. The output should be two capital letters with a dot separating them.

// Examples
// Sam Harris -> S.H
// patrick feeney -> P.F

// 1.
const abbrevName = (name: string): string => {
  const [firstName, lastName] = name.split(" ");
  return `${firstName[0]}.${lastName[0]}`.toUpperCase();
};

// 2.
// const abbrevName = (name: string): string => {
//   return name
//     .split(" ")
//     .map((name) => name[0].toUpperCase())
//     .join(".");
// };
