# QAwebAutomation
Simple demo on QA web automation using Python and Selenium.

## Instructions

As a user I want to make a purchase in Amazon web. The process to make the purchase is: find an article, go to the article page, add it to the cart and validate the cart (Buying the product is obviously not required).

- The code can be in one of the following languages: Python, Java, Ruby, NodeJS.
- The activity should be completed in less than five days.
- The implementation of coding good practices and automation patterns will be valued very positively.
- If possible, use any automation framework based on Selenium (or similar).
- The code should be delivered using Github or similar (or, if you want, you can also send it by e-mail).
- It is mandatory to include a README file with instructions regarding the necessary steps to execute the code and all the required dependencies.
- Including in the README an explanation with the code structure and good practices used will be valued positively.

## Notes from the author (Javier Aguerri)

- The chosen programming language has been Python
- The automation framework of choice is pytest, using pytest-selenium plugin (extends the pytest framework capabilities). Some advantages of this setup are: it allows fixtures (env setup), it provides test reports, clear syntax
- Find below the instructions regarding the environment setup and execution of the test.
- Find some explanations of the code structure and good practices directly as code comments in test_ValidateCart.py. Also, some general comments on that here:
    - <b>Use of a fixture function</b> to set up and tear down the environment and a test function to encapsulate the test script. Further tests would be encapsulated in additional test_*(driver) functions, which will share the same fixture function as its default value is 'function'.
    - <b>Implicit and explicit waits</b>. Instead of explicitly wait for each element before interacting with it, an implicit wait time of 6s has been set in the fixture (env setup). This will allow elements (like buttons) to show in a 6s time window before considering the test failed. However, explicit waits with a longer time have been added in cases where they would make sense. For example, when we are waiting for a new page to load.
    - <b>Multiple locating strategies</b>. Find elements by ID, class name or CSS selector. In general, I used ID location as a primary choice because ID is unique for each element, so it is the most reliable and efficient method. Whenever I had to locate elements based on attributes or the relation with other elements.
    - <b>Usage of try blocks</b> to handle exceptions in case some optional elements are not present. 
    - <b>Usage of assert statement</b> to validate the expected outcome. 
    - <b>Use of variables</b> to store product information and selectors, making the code more readable and maintainable.

## Environment setup and execution instructions
 
 - Use a Linux based machine
 - Make sure Firefox browser is installed in your system
 - Make sure python3 (preferrably v3.8.10) is installed in your system
 - Install dependencies: selenium, pytest and pytest-selenium. Execute the following commands in your terminal:
    - <code>pip install -U selenium</code>
    - <code>pip install -U pytest</code>
    - <code>pip install -U pytest-selenium</code>
 - Navigate to the project folder and run the following command in the terminal: 
    - <code>pytest --driver-path geckodriver</code>
