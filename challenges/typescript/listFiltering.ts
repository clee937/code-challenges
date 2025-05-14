/**
 * CodeWars Challenge: [List Filtering]
 * Link: [https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/typescript]
 * Difficulty: [8 Kyu]

 * Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

 * Example

 * filter_list([1,2,'a','b']) == [1,2]
 * filter_list([1,'a','b',0,15]) == [1,0,15]
 * filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
 **/

// filter() and typeof(). typeof() checks whether the value's type is 'number', regardless of whether it's an integer or a float. Will return true for a decimal, float, NaN, Infinity (unlike using Number.isinteger()).
const filter_list = (list: Array<any>): Array<number> => {
  return list.filter((element) => typeof element == "number");
};

// implicit return
// const filter_list = (list: Array<any>): Array<number> =>
//   list.filter((element) => typeof element == "number");

// filter() with Number.isInteger(). Checks whether the value is a number and is an integer (no decimal part). Use it when: You want to confirm a number is a whole number (e.g. 1, 2, -3), not a float, or NaN.
// const filter_list = (list: Array<any>): Array<number> => {
//   return list.filter((element) => Number.isInteger(element));
// };

// forEach loop with push()
// const filter_list = (l: Array<any>): Array<number> => {
//   const newList: number[] = [];

//   l.forEach((element) => {
//     if (typeof element != "string") {
//       newList.push(element);
//     }
//   });

//   return newList;
// };

// standard for loop with push()
// const filter_list = (list: Array<any>): Array<number> => {
//   const newList: number[] = [];

//   for (let i = 0; i < list.length; i++) {
//     if (typeof list[i] != "string") {
//       newList.push(list[i]);
//     }
//   }

//   return newList;
// };

console.log(filter_list([1, 2, "a", "b"]));
console.log(filter_list([1, "a", "b", 0, 15]));
console.log(filter_list([1, 2, "aasf", "1", "123", 123]));
