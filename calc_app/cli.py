import sys
from .core import add, sub, mul, div, two_plus_two

def main():
    args = sys.argv[1:]
    if not args:
        print(two_plus_two())
        return
    if len(args) != 3:
        print("Usage: python -m calc_app.cli <add|sub|mul|div> <a> <b>")
        raise SystemExit(1)
    op, a_s, b_s = args
    try:
        a = float(a_s); b = float(b_s)
    except ValueError:
        print("a and b must be numbers"); raise SystemExit(1)

    try:
        if op == "add":  print(add(a, b))
        elif op == "sub": print(sub(a, b))
        elif op == "mul": print(mul(a, b))
        elif op == "div": print(div(a, b))
        else:
            print("Unknown op. Use add|sub|mul|div"); raise SystemExit(1)
    except ZeroDivisionError as e:
        print(f"Error: {e}"); raise SystemExit(1)

if __name__ == "__main__":
    main()
