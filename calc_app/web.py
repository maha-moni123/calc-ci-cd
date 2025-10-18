from flask import Flask, request, jsonify, render_template_string
from .core import add, sub, mul, div

HTML = """
<!doctype html><html><head><meta charset="utf-8"><title>Calculator</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{font-family:system-ui,Arial,sans-serif;margin:2rem}
.card{max-width:460px;padding:1rem 1.25rem;border:1px solid #ddd;border-radius:12px}
label{display:block;margin-top:.75rem;font-weight:600}
select,input{width:100%;padding:.5rem;margin-top:.25rem}
button{margin-top:1rem;padding:.6rem 1rem;border:0;border-radius:8px;background:#111827;color:#fff;cursor:pointer}
.result{margin-top:1rem;font-weight:700}
.muted{color:#6b7280;font-size:.9rem}
</style></head><body>
<div class="card"><h2>Calculator (V1.1)</h2>
<form method="get" action="/calc-ui">
<label for="op">Operation</label>
<select name="op" id="op" required>
  <option value="add" {{ 'selected' if op=='add' else '' }}>Add</option>
  <option value="sub" {{ 'selected' if op=='sub' else '' }}>Subtract</option>
  <option value="mul" {{ 'selected' if op=='mul' else '' }}>Multiply</option>
  <option value="div" {{ 'selected' if op=='div' else '' }}>Divide</option>
</select>
<label for="a">A (number)</label>
<input type="number" step="any" id="a" name="a" required value="{{ a if a is not none else '' }}">
<label for="b">B (number)</label>
<input type="number" step="any" id="b" name="b" required value="{{ b if b is not none else '' }}">
<button type="submit">Calculate</button>
</form>
{% if result is not none %}<div class="result">Result: {{ result }}</div>
{% elif error %}<div class="result" style="color:#b91c1c">Error: {{ error }}</div>
{% else %}<p class="muted">Tip: choose an operation and enter A & B.</p>{% endif %}
<p class="muted">API: <code>/calc?op=add|sub|mul|div&a=..&b=..</code></p>
</div></body></html>
"""

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/calc")
    def calc():
        op = request.args.get("op")
        try:
            a = float(request.args.get("a"))
            b = float(request.args.get("b"))
        except (TypeError, ValueError):
            return jsonify(error="a and b must be numbers"), 400

        try:
            if op == "add":  res = add(a, b)
            elif op == "sub": res = sub(a, b)
            elif op == "mul": res = mul(a, b)
            elif op == "div": res = div(a, b)
            else: return jsonify(error="op must be one of add|sub|mul|div"), 400
            return jsonify(result=res)
        except ZeroDivisionError as e:
            return jsonify(error=str(e)), 400

    @app.get("/calc-ui")
    def calc_ui():
        op = request.args.get("op", "add")
        a_raw = request.args.get("a")
        b_raw = request.args.get("b")
        a = b = None; result = None; error = None
        if a_raw is None or b_raw is None:
            return render_template_string(HTML, op=op, a=a, b=b, result=result, error=error)
        try:
            a = float(a_raw); b = float(b_raw)
        except (TypeError, ValueError):
            error = "a and b must be numbers"
            return render_template_string(HTML, op=op, a=a_raw, b=b_raw, result=None, error=error)
        try:
            if op == "add": result = add(a, b)
            elif op == "sub": result = sub(a, b)
            elif op == "mul": result = mul(a, b)
            elif op == "div": result = div(a, b)
            else: error = "op must be one of add|sub|mul|div"
        except ZeroDivisionError as e:
            error = str(e)
        return render_template_string(HTML, op=op, a=a, b=b, result=result, error=error)

    return app

def run(port: int = 8000):
    app = create_app()
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    run()
