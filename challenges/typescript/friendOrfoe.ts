/**
 * CodeWars Challenge: [Friend or Foe]
 * Link: [https://www.codewars.com/kata/55b42574ff091733d900002f/train/typescript]
 * Difficulty: [7 Kyu]
 *
 * Instructions
 * Make a program that filters a list of strings and returns a list with only your friends' name in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not. Input strings will only contain letters. Note: keep the original order of the names in the output.
 *
 * Example
 * Input = ["Ryan", "Kieran", "Jason", "Yous"]
 * Output = ["Ryan", "Yous"]

 * Input = ["Peter", "Stephen", "Joe"]
 * Output = []
 */

const showFriends = (friends: string[]): string[] => {
  return friends.filter((friend) => friend.length === 4);
};

// const showFriends = (friends: string[]): string[] => {
//   let myFriends: string[] = [];
//   for (let friend of friends) {
//     if (friend.length === 4) {
//       myFriends.push(friend);
//     }
//   }
//   return myFriends;
// };

console.log(showFriends(["Ryan", "Kieran", "Jason", "Yous"]));
console.log(showFriends(["Peter", "Stephen", "Joe"]));
