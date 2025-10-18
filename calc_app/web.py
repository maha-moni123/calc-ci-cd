from flask import Flask, request, jsonify, render_template_string
from .core import add, sub, mul, div, sqrt, power, sin, cos, tan

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Scientific Calculator (V1.2)</title>
  <style>
    body{font-family:system-ui,Arial,sans-serif;margin:2rem}
    .card{max-width:500px;padding:1rem 1.25rem;border:1px solid #ddd;border-radius:12px}
    label{display:block;margin-top:.75rem;font-weight:600}
    select,input{width:100%;padding:.5rem;margin-top:.25rem}
    button{margin-top:1rem;padding:.6rem 1rem;border:0;border-radius:8px;background:#111827;color:#fff;cursor:pointer}
    .result{margin-top:1rem;font-weight:700}
    .muted{color:#6b7280;font-size:.9rem}
  </style>
</head>
<body>
  <div class="card">
    <h2>Scientific Calculator (V1.2)</h2>
    <form method="get" action="/calc-ui">
      <label for="op">Operation</label>
      <select name="op" id="op" required>
        <optgroup label="Basic">
          <option value="add"  {{ 'selected' if op=='add'  else '' }}>Add</option>
          <option value="sub"  {{ 'selected' if op=='sub'  else '' }}>Subtract</option>
          <option value="mul"  {{ 'selected' if op=='mul'  else '' }}>Multiply</option>
          <option value="div"  {{ 'selected' if op=='div'  else '' }}>Divide</option>
        </optgroup>
        <optgroup label="Scientific">
          <option value="sqrt"  {{ 'selected' if op=='sqrt'  else '' }}>Square Root</option>
          <option value="power" {{ 'selected' if op=='power' else '' }}>Power</option>
          <option value="sin"   {{ 'selected' if op=='sin'   else '' }}>Sine</option>
          <option value="cos"   {{ 'selected' if op=='cos'   else '' }}>Cosine</option>
          <option value="tan"   {{ 'selected' if op=='tan'   else '' }}>Tangent</option>
        </optgroup>
      </select>

      <label for="a">A (number)</label>
      <input type="number" step="any" id="a" name="a" required value="{{ a if a is not none else '' }}">

      <label for="b">B (number, optional for sqrt/sin/cos/tan)</label>
      <input type="number" step="any" id="b" name="b" value="{{ b if b is not none else '' }}">

      <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
      <div class="result">Result: {{ result }}</div>
    {% elif error %}
      <div class="result" style="color:#b91c1c">Error: {{ error }}</div>
    {% else %}
      <p class="muted">Tip: choose an operation and enter numbers.</p>
    {% endif %}
  </div>
</body>
</html>
"""

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/calc")
    def calc():
        op = request.args.get("op")
        a_raw = request.args.get("a")
        b_raw = request.args.get("b")

        try:
            a = float(a_raw) if a_raw not in (None, "") else None
            b = float(b_raw) if b_raw not in (None, "") else None
        except ValueError:
            return jsonify(error="a and b must be numbers"), 400

        try:
            if op == "add":    res = add(a, b)
            elif op == "sub":  res = sub(a, b)
            elif op == "mul":  res = mul(a, b)
            elif op == "div":  res = div(a, b)
            elif op == "sqrt": res = sqrt(a)
            elif op == "power":res = power(a, b)
            elif op == "sin":  res = sin(a)
            elif op == "cos":  res = cos(a)
            elif op == "tan":  res = tan(a)
            else:
                return jsonify(error="invalid op"), 400
            return jsonify(result=res)
        except Exception as e:
            return jsonify(error=str(e)), 400

    @app.get("/calc-ui")
    def calc_ui():
        op = request.args.get("op", "add")
        a_raw = request.args.get("a")
        b_raw = request.args.get("b")

        a = b = None
        result = None
        error = None

        try:
            if a_raw not in (None, ""):
                a = float(a_raw)
            if b_raw not in (None, ""):
                b = float(b_raw)
        except ValueError:
            error = "a and b must be numbers"
            return render_template_string(HTML, op=op, a=a_raw, b=b_raw, result=None, error=error)

        try:
            if op == "add":    result = add(a, b)
            elif op == "sub":  result = sub(a, b)
            elif op == "mul":  result = mul(a, b)
            elif op == "div":  result = div(a, b)
            elif op == "sqrt": result = sqrt(a)
            elif op == "power":result = power(a, b)
            elif op == "sin":  result = sin(a)
            elif op == "cos":  result = cos(a)
            elif op == "tan":  result = tan(a)
            else:
                error = "invalid op"
        except Exception as e:
            error = str(e)

        return render_template_string(HTML, op=op, a=a, b=b, result=result, error=error)

    return app

def run(port: int = 8000):
    app = create_app()
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    run()
