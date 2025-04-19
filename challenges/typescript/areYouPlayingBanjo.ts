/**
 * CodeWars Challenge: [Are You Playing Banjo?]
 * Link: [https://www.codewars.com/kata/53af2b8861023f1d88000832/train/typescript]
 * Difficulty: [8 Kyu]
 
 * Instructions:
 * Create a function which answers the question "Are you playing banjo?".
 * If your name starts with the letter "R" or lower case "r", you are playing banjo!

 * The function takes a name as its only argument, and returns one of the following strings:

 * name + " plays banjo" 
 * name + " does not play banjo"
 
 * Names given are always valid strings.
 **/

export function areYouPlayingBanjo(name: string): string {
  return name[0].toLowerCase() === "r"
    ? `${name} plays banjo`
    : `${name} does not play banjo`;
}

// Alternatives:

// export function areYouPlayingBanjo(name: string): string {
//   return name.charAt(0).toUpperCase() === "R"
//     ? `${name} plays banjo`
//     : `${name} does not play banjo`;
// }

// export function areYouPlayingBanjo(name: string): string {
//   return name.startsWith("r") || name.startsWith("R")
//     ? name + " plays banjo"
//     : name + " does not play banjo";
// }

console.log(areYouPlayingBanjo("Roger"));
console.log(areYouPlayingBanjo("Bob"));
