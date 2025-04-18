/**
 * CodeWars Challenge: [Transportation on vacation]
 * Link: [URL]
 * Difficulty: [8 Kyu]
 * 
 * Instructions:
 * After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
 */

export function rentalCarCost(d: number): number {
  if (d >= 7) return d * 40 - 50;
  if (d >= 3) return d * 40 - 20;
  return d * 40;
}

// export function rentalCarCost(d: number): number {
//   const price = d * 40;

//   return d >= 7 ? price - 50 : d >= 3 ? price - 20 : price;
// }

// export function rentalCarCost(d: number): number {
//   const discount = d >= 3 && d < 7 ? 20 : d >= 7 ? 50 : 0;
//   return d * 40 - discount;
// }
