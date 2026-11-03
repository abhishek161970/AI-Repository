def parse_expression(expr):
    predicate, args_str = expr.split('(', 1)
    args = [arg.strip() for arg in args_str.rstrip(')').split(',')]
    return predicate, args

def unify(expr_a, expr_b):
    pred_a, args_a = parse_expression(expr_a)
    pred_b, args_b = parse_expression(expr_b)
    
    if pred_a != pred_b or len(args_a) != len(args_b):
        return None, "Unification Failed: Predicate mismatch or argument count mismatch."
    
    substitutions = {}
    unified_args = []
    
    for arg1, arg2 in zip(args_a, args_b):
        is_var1 = arg1.islower()
        is_var2 = arg2.islower()
        
        if is_var1 and not is_var2:
            substitutions[arg1] = arg2
            unified_args.append(arg2)
        elif not is_var1 and is_var2:
            substitutions[arg2] = arg1
            unified_args.append(arg1)
        elif is_var1 and is_var2:
            substitutions[arg1] = arg2
            unified_args.append(arg2)
        else:
            if arg1 == arg2:
                unified_args.append(arg1)
            else:
                return None, f"Unification Failed: Constant mismatch ({arg1} != {arg2})."
                
    unified_expr = f"{pred_a}({', '.join(unified_args)})"
    return substitutions, unified_expr

expression_A = input("Enter first expression (e.g., Eats(x, Apple)): ")
expression_B = input("Enter second expression (e.g., Eats(Riya, y)): ")

subs, result = unify(expression_A, expression_B)

if subs is not None and not isinstance(subs, str):
    print("\nUnification Successful!")
    print("Substitutions:")
    for var, val in subs.items():
        print(f"  {var} = {val}")
    print(f"Unified Expression: {result}")
else:
    print(f"\n{result}")
