/**
 * CodeWars Challenge: [What's the real floor?]
 * Link: [https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/typescript]
 * Difficulty: [8 Kyu]
 
 * Instructions:
 * Write a function that given a floor in the american system returns the floor in the european system. With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them. Basements (negatives) stay the same as the universal level.

 * Examples:
 * 1  =>  0 
 * 0  =>  0
 * 5  =>  4
 * 15  =>  13
 * -3  =>  -3
 **/

const getRealFloor = (floor: number): number => {
  return floor < 1 ? floor : floor < 13 ? floor - 1 : floor - 2;
};

// const getRealFloor = (floor: number): number => {
//   if (floor <= 0) return floor;
//   else if (floor < 13) return floor - 1;
//   else return floor - 2;
// };

console.log(getRealFloor(1));
console.log(getRealFloor(0));
console.log(getRealFloor(5));
console.log(getRealFloor(15));
console.log(getRealFloor(-3));
