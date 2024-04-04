# Password Game Solver

This repository contains a Python script that solves the Password Game up to 11 rules using Python and Playwright.

## Prerequisites

- Python 3.12 installed (should work fine with older 3.x versions)
- pipenv 2023.12.1 installed `pip install pipenv`

## How to Run

1. Clone this repository.
2. Navigate to the project folder:
    ```
    cd passoword-game
    ```
3. Install the dependencies:
    ```
    pipenv install
    ```
4. Activate the virtual environment:
    ```
    pipenv shell
    ```
5. Run the tests:

    **! Running tests on https://neal.fun/password-game/ does NOT work in headless mode due to instat human veirifaction checks**

    **! See html file `checking_if_you_are_human.html` to view what headless mode is running into**

    **Please use `pytest --headed`**

    - To run in headless mode:
        ```
        pytest
        ```
    - To see the browser open (headed mode):
        ```
        pytest --headed
        ```

## Notes

* To pause tests at any given time use `page.pause()` in the test code.

* Occasionally, you might encounter a human verification prompt ("Please Verify You Are a Human") that requires clicking a checkbox manually to proceed. Unfortunately, this verification step is built into the Password Game and cannot be bypassed.
