def create_notion_HTML(notion_title, notion_description):
    html_notes_1 = '''
 <div class="notion">
    <div class="notion-title">
    ''' + notion_title
    html_notes_2 = '''
    </div>
    <div class="notion-description">
    ''' + notion_description
    html_notes_3 = '''
    </div>
 </div>'''
    full_html_notes = html_notes_1 + html_notes_2 + html_notes_3
    return full_html_notes

def create_HTML(notion):
    notion_title = notion[0]
    notion_description = notion[1]
    return create_notion_HTML(notion_title, notion_description)

    
NOTIONS = [['The Web, Hyperlinks, HTML, HTTP', '''The Web is a collection of web pages. The links between these pages are called Hyper links. A web page is a text document written in a language called HTML. The browser displays an HTML document as a web page.

URLs - how you refer to documents on the web.

There are all different types of files on the web: plain text, HTML, images, videos and music. The browser running on a computer makes a request (using the protocol HTTP - the main protocol of the web) to the servers via Internet. The servers return files that the browser reads, interprets and displays.'''],
['HTML(Hyper Text Markup language)', '''HTML is made up of :

text content - what you see on the web page - the content;
markup - how the content is arranged;
references to other documents
links to other pages.
The markup is made of tags. HTML tags are used to show the browser the types of HTML elements. An HTML element refers to everything within a set of opening and closing tags. How to connect an HTML document to any other document on the internet by adding links.

HTML attributes - a property of an HTML element:

&lt;tag attr="value"&gt;contents &lt;/tag&gt;

&lt;a href="www.reddit.com"&gt; derf &lt;/a&gt;

Anchor tag - &lt;a&gt; for making links

href - attribure name

derf would be a link to reddit.com

&lt;img&gt; image tag for including images

&lt;img scr="url"alt="text"&gt;

scr - attribute called source which equals to URL - the URL of the image to download. alt - attribute - alternate, and this is the text that gets displayed when the image doesn't load. Image tag doesn't have a closing tag. It's a VOID tag, it doesn't have a content.

Whitespace - single space -written in one line

&lt;br&gt; break (void) for multiple lines. &lt;br&gt; - inline, ending a line

text&lt;br&gt;text

&lt;p&gt; paragraph, it's not a VOID tag, it has a content &lt;p&gt;content&lt;/p&gt;

HTML elements can be either inline or block.

&lt;p&gt; is a block element, it makes an invisible box. It has height and width.

&lt;p&gt;text&lt;/p&gt;

&lt;strong&gt; - inline

&lt;form&gt; - block

Container elements

&lt;span&gt;text&lt;/span&gt; - inline.

&lt;div&gt;text&lt;/div&gt; - block

Computers understand only clear instructions. '''],
['The Structure of HTML document', '''HTML controls structure and has a specific syntax and rules. CSS controls style. Java script - interective components.

HTML elements are rectangular. Everything on a web page is actually a box. Some elements are invisible (like the head element) You can read the same text as on the page.The structure of an HTML document is as follows:

&lt;!DOCTYPE HTML&gt; - doctype

&lt;html&gt; opening tag (surrounds the entire document)

&lt;head&gt; meta-data (CSS, java script)

&lt;title&gt;Title!&lt;title&gt; - title of the page

&lt;/head&gt;

&lt;body&gt; contents of the doc

content

&lt;/body&gt;

&lt;/html&gt;

The "tree-like structure" of HTML.

The blowser uses HTML tags as elements to form a tree-like structure according to the standard convention for representing and interacting with elements in HTML - DOM (Document Object Model).'''], ['Inheritance. Why is it important to avoid repetition?', '''CSS stands for "Cascading Style Sheets." "Cascading" means that rules are applied not only to the elements they directly match, but also to all of those elements' child elements. Inheritance is a key feature in CSS. Inheritance is the mechanism by which properties are applied not only to a specified element, but also to its descendants. Properties that can be inherited are color, font, letter-spacing, line-height, list-style, text-align text-indent, text-transform, visibility, white-space and word-spacing. Properties that cannot be inherited are background, border, display, float and clear, height and width, margin, min- and max-height and -width, outline, overflow, padding, position, text-decoration, vertical-align and z-index. Inheritance prevents certain properties from being declared over and over again in a style sheet.'''], ['3 ways to include CSS styling:', '''Writing CSS in the head of HTML. It suits for small projects;
Linking your HTML to a separate CSS file;
Writing your style inline with your HTML.'''], ['Selectors', '''The first thing you write in CSS is a selector. Selectors allow to target HTML elements and apply style to them. ID selectors are the most powerful type of selector. Class selectors are the most useful and well supported in all browsers. Tag selectors are necessary to change properties that are unique to that particular HTML element, f.ex. list-style. You can also combine selectors.'''], ['Box sizing', '''HTML elements are boxes that have 4 components There are 2 techniques to deal with sizing issues:

Set sizes in terms of percents than pixels;
Set the box-sizing attribute to border-box for every element.
Divs are block elements - they take the whole width of a page by default. Adding the rule display:flex; allows divs to appear next to each other.

NB:Different browsers display the same code differently.'''], 
['Computer Program, Python, Expressions', '''A computer is a universal machine that we can program to do almost anything. A programmer writes a computer program - a precise sequence of steps, that can be a web browser, the Python interpreter, calender application or the Python code. The computer executes the steps of a program super fast. There are a lot of languages to program computers. They are special languages invented for computer programming, they are different from natural languages as they don't allow ambiguity and verbosity to mislead a computer.

Python is one of the programming languages. Python Interpreter is a program that runs, interprets and executes the code, written in Python language. There are certain grammar rules in Python that we use to write a program, they allow us to form sentences from the parts of speech. The way we're writing grammars is a notation called Backus-Naur Form invented by John Backus.

An expression is a combination of values, variables, and operators. A value all by itself is considered an expression. Grammar starts with a non-terminal expression. Each rule has the following form: on the left side there's a non-terminal (something that we're not finished with). Then there's an arrow, and then on the right side there's a replacement (a terminal). We can form a sentence by starting from some non-terminal, and then by following the rules we keep replacing non-terminals with their replacements until we're left with only terminals.'''], ['Variables, Strings', '''A variable in Python is like a box where you can store a value. A variable is a name for a value. Variables allow to give names to values. The name can be any sequence of letters, numbers as well as underscores as long as it starts with a letter or an underscore. F.ex. speed_of _light.

To introduce a value we use an assignment statement. The equal sign (=) is used to assign values to variables. Pythons usage of the equal sign is not the mathematical usage of the equal sign. An assignment statement associates a variable name on the left of the equal sign with the value of an expression calculated from the right of the equal sign. Once a variable is assigned a value, the variable can be used in place of that value. F.ex. sum is a variable with a value 5. sum = 5 The variable sum takes the value of 5. We alsways need to introduce a variable before we use it. print sum + sum The result is 10.

There are different ways to use variables:

Variables make the code easier to understand;
Variables allow to store the value of some data;
Variables allow to change the value of some data. When we use the variable again, it refers to the new value.
String is a sequence of characters surrounded by quotes, single or double. We can put strings together by using the plus operator. The new string is the result of pasting 2 strings together: string + string - concatenation. We can't add numbers and strings together. We can multiply strings though. It's also possible to extract subsequences from the string. [] brackets are used to extract part of the string.

The difference between 2+2 and "2"+"2" is as follows: 2 is a number, and 2 in quotes "2" is a string. So, this difference will lead to different results: 2+2 is 4. The code "2"+"2" would give "22".'''], ['Functions', '''A function is a program that performs a specific task. It takes an input, works with it, changes it accoring to a certain pathern and returns an output. F.ex. a function named sum can take numbers and calculate and return a sum of these numbers as output.'''], ['There is a difference between making and using functions.', '''A function has a following structure:

A line of code with a keyword def;
A function name
Parameters in parenthesis
The code that specifies what we are going to do with the parameters
The parameters will be replaced by actual values when the function is called. To call a function we use its name followed by the values in the parenthesis.

Example:

def sum(a,b)
return a+b
print sum (1,4)
Functions help to avoid repetitions. After you have created a function, you can use it at any time, in any place. This saves you the time and effort of having to retell the computer what to do every time it does a common task.

If a function doesn't have a return statement, we won't see an output. We'll get the result none. The return keyword tells Python what the function should produce as output.'''],
['If statements', '''The If statement is used for conditional execution: it allows to control what code executes based on the result of a test expression. The code in &lt; block &gt; only executes if test expression has a true value. Else clause is used in an if statement to provide code that will run when the &lt; TestExpression &gt; has a False value.'''], 
['Operators', '''There are different types of operators in Python:

Arithmetic Operators, f.ex. +, - , *, /;
Comparison Operators, such as &lt;, &gt;, &lt;=, &gt;=, ==, !=
Assignment operator: =
Logical Operators. The and and or operators behave similarly to logical conjunction (and) and disjunction (or). The important property they have which is different from other operators is that the second operand expression is evaluated only when necessary. A boolean expression (or logical expression) evaluates to one of two states true or false. Python provides the boolean type that can be either set to False or True.
etc.'''], 
['Loops', '''A loop is a way to do things over and over again. We use loops when we need to execute a block of code several number of times.

The While loop repeats a statement or group of statements while a given condition is true. It tests the condition before executing the loop body. If the &lt; TestExpression &gt; evaluates to False, the while loop is done and execution continues with the following statement. If the &lt; TestExpression &gt; evaluates to True, the &lt; Block &gt; is executed. Then, the loop repeats, returning to the &lt; TestExpression &gt; and continuing to evaluate the &lt; Block &gt; as long as the &lt; TestExpression &gt; is True.

while &lt; TestExpression &gt;:
&lt; Block &gt;
The For loop allows to execute a block once for each element of a collection:

for &lt; Name &gt; in &lt; Collection &gt;:
&lt; Block &gt;
The loop goes through each element of the collection, assigning that element to the &lt; Name &gt; and evaluating the &lt; Block &gt;.''']]

def HTML_for_all_notions(list_of_notions):
    HTML = ""
    for notion in list_of_notions:
        notion_HTML = create_HTML(notion)
        HTML = HTML + notion_HTML
    return HTML

print HTML_for_all_notions(NOTIONS)
