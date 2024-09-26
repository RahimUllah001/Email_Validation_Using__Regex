# Email Validation Script Using Regular Expressions

How to use Python's `re` (regular expression) module to validate an email address. 
The script matches the user-inputted email address against a specified pattern to check if it is valid.

## Python Code for Email Validation

```python
import re

# Corrected email validation pattern
email_condition = r'^[a-z]+[._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$'

# Get user email input
user_email = input("Enter your email: ")

# Validate email against the pattern
if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
```

### Explanation:

1. **`re` module**: Python's regular expression module is imported to handle pattern matching.

2. **Email validation pattern**: 
   - `^[a-z]+`: Ensures that the email starts with one or more lowercase letters.
   - `[._]?[a-z0-9]+`: Allows an optional period or underscore, followed by one or more alphanumeric characters.
   - `@[a-z0-9]+`: Requires an `@` symbol followed by one or more alphanumeric characters.
   - `\.[a-z]{2,3}$`: Requires a period followed by a domain suffix (2 to 3 lowercase letters).

3. **User input**: The user is prompted to input their email address.

4. **`re.search()`**: This function searches for a match to the pattern in the provided email string. If a match is found, the email is valid; otherwise, it is not.

5. **Output**: If the email address matches the pattern, "Right Email" is printed. If it does not, "Wrong Email" is displayed.

---

## Full Example Code

```python
import re

# Corrected email validation pattern
email_condition = r'^[a-z]+[._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$'

user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
```

---

## Output

When you run this script, it will prompt you to enter an email address. It will then validate the email based on the regular expression pattern and print whether it is correct or incorrect.
