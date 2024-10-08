# Recipe Helper

This project requires the following concepts:
- Conditionals
- Functions

The goal of this project is to create a program that will convert US standard recipe measurements to metric and will help the user to determine whether they have enough of their ingredient on hand to make their recipe. You must use conditional statements and logic operators. Your solution must also be well designed and use functions where appropriate.

## Scenario
Your user only has the kitchen tools to measure out teaspoons, tablespoons, cups, and ounces. Their recipe calls for mL and grams. 

Your solution must do all of the following:

1. Ask the user for the ingredient called for by the recipe
2. Ask the user how much of the (specific!) ingredient they have on hand 
   - Your solution must allow the user to enter the units (teaspoon, tablespoon, cup, or ounce)
4. Ask the user how much of the ingredient they need 
   - Your solution must allow the user to enter the units (ml or grams)
5. Display for the user the US standard amount that is needed by the recipe (i.e., convert the "how much is needed" amount from metric to US standard)
6. Display for the user whether they have a sufficient amount of the ingredient for the recipe

## Sample Output

Test 1:

```
Welcome to the recipe helper!
 I can help you convert US standard measurements to metric.
 You tell me the US Standard amount of the ingredient you have on hand,
 and I'll tell you whether you have enough to make a your recipe 
 specified in metric.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Which ingredient does your recipe call for? milk
How much milk do you have on hand? 2 cups
How much milk do you need? 725 ml
You need 2.9 cups of milk.
Sorry, you don't have enough milk.
```

Test 2:

```
Welcome to the recipe helper!
 I can help you convert US standard measurements to metric.
 You tell me the US Standard amount of the ingredient you have on hand,
 and I'll tell you whether you have enough to make a your recipe 
 specified in metric.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Which ingredient does your recipe call for? oil
How much oil do you have on hand? 4 tablespoons
How much oil do you need? 25 ml
You need 1.6666666666666667 tablespoons of oil.
It looks like you can make your recipe!
```

## Requirements
1. Your solution will support the following conversions taken from [https://www.thespruceeats.com/metric-conversions-for-cooking-2355731](https://www.thespruceeats.com/metric-conversions-for-cooking-2355731)
```
    1 teaspoon = 5 mL
    1 tablespoon = 15mL
    1 cup = 250 mL
    1 ounce = 28 grams
```

2. You **must** implement the following function that will be tested via automated test cases:
```python
def get_amount_needed_in_us_std(
        us_std_unit: str, 
        metric_amount_needed: float, 
        metric_unit: str) -> float:
      """
      Given an amount needed in metric units, determines
      the amount needed in US standard units.
      Parameters:
        us_std_units(str): US standard units, e.g., tablespoons
        metric_amount_needed(float): Amount required in metric, e.g., 725
        metric_units(str): Metric units, e.g., ml
      Returns:
        amount in US standard (float)
      """
```

3. *Your program must use additional functions and constants appropriately.* 
4. The user must be able to enter singular and plural measurements (i.e., teaspoon or teaspoons).
5. The "How much" prompts as shown above must include the specific ingredient the user has entered.
6. The amount and units must be entered on one line, i.e., ```4 tablespoons```
7. Your program must print an error message in the case that user has entered an unsupported measurement (i.e., the on hand amount is not teaspoon/tablespoon/cup/ounce or the needed amount is not ml or grams). It is acceptable for the program to exit after the error message is printed.
8. Your program must be saved in a file `recipe_helper.py`.

## Error Handling
1. The program does **not** need to verify that the user has used the correct
   pluralization. It is acceptable to accept input such as "2 cup" or "1
   tablespoons".
2. The program does **not**  need to use the correct pluralization in the
   output. It is acceptable for the output to be "You need 1 tablespoons of
   ...".
3. If the user enters a multi-word item, the program will print a message and
   exit; for example, if the user enters "6 gala apples" the program will tell the user
   the unit is invalid and exit.
4. It is **not** required to handle the case of a non-floating point
   measurement. If the user enters 'bananas 5' the program will generate an
   error and crash when the program tries to convert the word bananas to a
   floating point number.
5. It is not required to use iteration in any part of this program. If an error
   is detected, the program will print a message and exit.

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all four parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully
