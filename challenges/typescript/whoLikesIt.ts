// CodeWars Challenge: [Who likes it?]
// Link: [https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/typescript]
// Difficulty: [6 Kyu]

// Instructions
// Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples. For 4 or more names, the number in "and 2 others" simply increases.

// Examples
// []                                -->  "no one likes this"
// ["Peter"]                         -->  "Peter likes this"
// ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
// ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
// ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

// 1. Switch statement
const likes = (names: string[]): string => {
  switch (names.length) {
    case 0:
      return "no one likes this";
    case 1:
      return `${names[0]} likes this`;
    case 2:
      return `${names[0]} and ${names[1]} like this`;
    case 3:
      return `${names[0]}, ${names[1]} and ${names[2]} like this`;
    default:
      return `${names[0]}, ${names[1]} and ${
        names.length - 2
      } others like this`;
  }
};

// 2. Using an object.
// "[Math.min(4, names.length)] as string" ensures that when the length of the names array is longer than 4, it will always return 4 so we are able to index the default value.
// const likes = (names: string[]): string => {
//   return {
//     0: "no one likes this",
//     1: `${names[0]} likes this`,
//     2: `${names[0]} and ${names[1]} like this`,
//     3: `${names[0]}, ${names[1]} and ${names[2]} like this`,
//     4: `${names[0]}, ${names[1]} and ${names.length - 2} others like this`,
//   }[Math.min(4, names.length)] as string;
// };

// Using an array.
// const likes = (names: string[]): string => {
//   return [
//     "no one likes this",
//     `${names[0]} likes this`,
//     `${names[0]} and ${names[1]} like this`,
//     `${names[0]}, ${names[1]} and ${names[2]} like this`,
//     `${names[0]}, ${names[1]} and ${names.length - 2} others like this`,
//   ][Math.min(4, names.length)];
// };

console.log(likes([]));
console.log(likes(["Peter"]));
console.log(likes(["Jacob", "Alex"]));
console.log(likes(["Max", "John", "Mark"]));
console.log(likes(["Alex", "Jacob", "Mark", "Max"]));
