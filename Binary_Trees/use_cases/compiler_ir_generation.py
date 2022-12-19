from Binary_Trees.binary_tree import TreeNode, print_tree
import operator
"""
compiler_ir_generation.py
@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 19 DEC 22

Performing arithmetic via the use of postorder traversal of an abstract syntax tree
"""

"""
Use Case:
In compiler design, an abstract syntax tree (AST) is a key step between the parsing of source code and the generation of 
an intermediate representation (IR). ASTs represent multi-operator expressions as nodes containing operators with their
operands as leaf nodes. To generate an IR, the subtree of the AST containing the expression must be read from bottom-up.

Approach:
Traverse the subtree of the AST containing the expression, building a postfix expression. Use said postfix expression
to construct an IR of the expression. The advantage of using a postfix expression is that it is stack-friendly
"""

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "%": operator.mod}

# Use postorder traversal of AST to build a stack-friendly postfix expression
def traverse_AST(ast):
    if not ast:
        return None
    postfixExpression = []
    left = traverse_AST(ast.left)
    if left is not None: postfixExpression += left
    right = traverse_AST(ast.right)
    if right is not None: postfixExpression += right
    postfixExpression += [ast.value]
    return postfixExpression

# Use postfix expression to construct an IR
def construct_IR(postfixExpression):
    global ops
    ir = []

    if isEvaluable(postfixExpression):
        expressionValue = evaluate_expression(postfixExpression)
        ir.append("reg = " + str(expressionValue))
        return ir

    # Otherwise, we need to handle the expression manually
    stack = []
    regIterator = 0
    for element in postfixExpression:
        if element not in ops:
            stack.append(element)
        else:
            regName = "reg" + str(regIterator)
            ir.append(regName + " = " + str(stack[len(stack) - 2]) + ' ' + element + ' ' + str(stack[len(stack) - 1]))
            stack.pop()
            stack.pop()
            stack.append(regName)
            regIterator += 1
        continue
    return ir

# If there are no elements that are not numeric or an operator, then the expression is evaluable
def isEvaluable(postfixExpression):
    global ops
    return not any(type(element) != int and element not in ops for element in postfixExpression)

# We can also simply evaluate the expression to optimize the IR
def evaluate_expression(postfixExpression):
    global ops
    stack = []
    for element in postfixExpression:
        if element not in ops:
            stack.append(element)
        else:
            register = ops[element](stack[len(stack) - 2], stack[len(stack) - 1])  # [1, 2, '+'] -> +(1, 2) = 1 + 2 = 3
            stack.pop()
            stack.pop()
            stack.append(register)
        continue
    return stack[0]

# ------------------------------
# Examples
# ------------------------------
def drive_example(ast):
    print("Abstract Syntax Tree:")
    print_tree(ast)
    postfixExpression = traverse_AST(ast)
    print("Postfix Expression:\n" + str(postfixExpression) + "\n")
    ir = construct_IR(postfixExpression)
    print("Intermediate Representation:")
    for element in ir:
        print(element)
    print()

# Example 1: 2 + 3 * 4
print("------------------------------\n" + "Example1:\t2 + 3 * 4\n" + "------------------------------")
ast1 = TreeNode('+', TreeNode(2), TreeNode('*', TreeNode(3), TreeNode(4)))
drive_example(ast1)

# Example 2: var1 * var2 + var3 * var4
print("------------------------------\n" + "Example2:\tvar1 * var2 + var3 * var4\n" + "------------------------------")
ast2 = TreeNode('+', TreeNode('*', TreeNode('var1'), TreeNode('var2')),
                TreeNode('*', TreeNode('var3'), TreeNode('var4')))
drive_example(ast2)





