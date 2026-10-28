"""Gera a área de membros (/areademembros), a área da Biblioteca Premium e a página de obrigado (/gracias).
Uso: python _fonte/gerar_area.py  (os links do Google Drive ficam no bloco LINKS de cada página gerada)
"""
import html
import os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
SLUG_BIBLIOTECA = "biblioteca-premium-r7k4q2"

# ===== LINKS DE GOOGLE DRIVE (preencher e rodar o script de novo) =====
LINKS_DRIVE = {
    "guia": "", "bono1": "", "bono2": "", "bono3": "", "bono4": "", "bono5": "",
    "libro1": "", "libro2": "", "libro3": "", "libro4": "", "libro5": "",
}

CSS = """
:root{--ink:#142d44;--muted:#5d6974;--gold:#9b7a3b;--gold2:#e3c682;--soft:#f5f7f9;--ivory:#fbf8f2;--line:#e4e8ec;--ok:#1f7a4d}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:16px/1.65 Arial,sans-serif;color:var(--ink);background:var(--ivory)}
a{color:inherit}img{display:block;max-width:100%;height:auto}button{font:inherit;cursor:pointer}
h1,h2,h3{font-family:Georgia,serif;font-weight:400;line-height:1.2;margin:0;letter-spacing:-.4px}
p{color:var(--muted);margin:8px 0}
.top{background:var(--ink);color:#fff}
.top .in{max-width:1120px;margin:auto;padding:16px 24px;display:flex;justify-content:space-between;align-items:center;gap:16px}
.brand{font:20px Georgia,serif;text-decoration:none;color:#fff}.brand span{display:block;font:9px/1.8 Arial;letter-spacing:3px;color:var(--gold2)}
.top nav{display:flex;gap:18px;font-size:13.5px}.top nav a{text-decoration:none;color:#d4dfe7}.top nav a:hover{color:#fff}
.hero{background:linear-gradient(180deg,var(--ink),#1d3c56);color:#fff;padding:46px 24px 70px;text-align:center}
.hero .eyebrow{color:var(--gold2)}.hero h1{font-size:clamp(28px,4vw,42px);color:#fff}.hero p{color:#d4dfe7;max-width:640px;margin:12px auto 0}
.eyebrow{font:700 11.5px Arial;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.wrap{max-width:1120px;margin:auto;padding:0 24px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:-40px auto 0;max-width:1120px;padding:0 24px;position:relative}
.steps div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px 20px;box-shadow:0 8px 24px #142d4410;font-size:14.5px;color:var(--muted)}
.steps b{display:block;font:17px Georgia,serif;color:var(--ink);margin-bottom:4px}.steps span{color:var(--gold);font:700 12px Arial;letter-spacing:1.5px}
.sec{padding:54px 0 10px}.sec-head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;margin-bottom:22px;flex-wrap:wrap}
.sec-head h2{font-size:clamp(25px,3vw,32px)}.progress{font-size:13px;color:var(--muted)}.progress b{color:var(--ink)}
.bar{height:6px;background:#e9e2d2;border-radius:6px;overflow:hidden;width:220px;margin-top:6px}.bar i{display:block;height:100%;width:0;background:var(--gold);transition:width .3s}
.main-card{display:grid;grid-template-columns:230px 1fr;gap:30px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;align-items:center;box-shadow:0 10px 30px #142d440d}
.main-card img{border-radius:8px;box-shadow:0 12px 26px #142d4426}
.main-card h3{font-size:clamp(23px,2.6vw,30px);margin:4px 0 6px}
.tag{display:inline-block;font:700 10.5px Arial;letter-spacing:1.4px;text-transform:uppercase;padding:4px 9px;border-radius:20px;background:#f3ead6;color:#7a5d2e}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(205px,1fr));gap:20px}
.card{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-3px);box-shadow:0 14px 30px #142d4414}
.card .cover{background:#f4efe4;padding:16px 16px 0}.card .cover img{border-radius:6px 6px 0 0;box-shadow:0 6px 16px #142d4420}
.card .body{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.card h3{font-size:17.5px}.card p{font-size:13.5px;line-height:1.5;margin:0;flex:1}
.btn{display:block;text-align:center;text-decoration:none;border:0;border-radius:8px;background:var(--ink);color:#fff;padding:12px 14px;font-weight:700;font-size:14px;transition:background .15s}
.btn:hover{background:#284c68}.btn.gold{background:var(--gold)}.btn.gold:hover{background:#856829}
.btn.off{background:#e6e9ec;color:#8a949c;pointer-events:none}
.done{display:flex;align-items:center;gap:7px;font-size:12.5px;color:var(--muted);background:none;border:0;padding:4px 0 0}
.done i{width:16px;height:16px;border:1.5px solid #b9c2ca;border-radius:4px;display:inline-flex;align-items:center;justify-content:center;font-style:normal;font-size:11px}
.done.on{color:var(--ok)}.done.on i{background:var(--ok);border-color:var(--ok);color:#fff}
.lock{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;background:linear-gradient(120deg,#1d3c56,var(--ink));color:#fff;border-radius:16px;padding:28px 30px}
.lock h3{color:#fff;font-size:24px}.lock p{color:#d4dfe7}.lock .covers{display:flex}.lock .covers img{width:64px;border-radius:4px;margin-left:-18px;border:2px solid var(--ink);box-shadow:0 6px 14px #0006}
.lock .covers img:first-child{margin-left:0}.lock .acts{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.lock .btn{background:var(--gold)}.lock .btn.ghost{background:transparent;border:1px solid #ffffff55}
.help{margin:56px 0 0;background:#fff;border:1px solid var(--line);border-radius:14px;padding:24px 26px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.help h3{font-size:17px;margin-bottom:4px}.help p{font-size:14px;margin:0}
footer{text-align:center;font-size:12.5px;color:#8a949c;padding:40px 24px 50px}
@media(max-width:760px){.top nav{display:none}.steps{grid-template-columns:1fr;margin-top:-34px}.main-card{grid-template-columns:1fr;padding:20px}.main-card img{max-width:220px;margin:0 auto}
.lock{grid-template-columns:1fr;padding:24px 20px}.help{grid-template-columns:1fr}.grid{grid-template-columns:1fr 1fr;gap:12px}.card .cover{padding:10px 10px 0}.card .body{padding:10px 11px 12px}.card h3{font-size:15.5px}.card p{display:none}.bar{width:160px}}
"""

JS = """
(function(){
  function get(k){try{return JSON.parse(localStorage.getItem('area72')||'{}')[k]}catch(e){return null}}
  function set(k,v){try{var o=JSON.parse(localStorage.getItem('area72')||'{}');o[k]=v;localStorage.setItem('area72',JSON.stringify(o))}catch(e){}}
  document.querySelectorAll('[data-link]').forEach(function(a){
    var url=LINKS[a.dataset.link];
    if(url){a.href=url;a.target='_blank';a.rel='noopener'}else{a.classList.add('off');a.textContent='Disponible pronto'}
  });
  function progreso(){
    document.querySelectorAll('[data-grupo]').forEach(function(g){
      var bs=g.querySelectorAll('.done'),n=0;bs.forEach(function(b){if(b.classList.contains('on'))n++});
      var t=g.querySelector('.js-n');if(t)t.textContent=n+' de '+bs.length;var bar=g.querySelector('.bar i');if(bar)bar.style.width=(bs.length?n/bs.length*100:0)+'%';
    });
  }
  document.querySelectorAll('.done').forEach(function(b){
    if(get(b.dataset.id)){b.classList.add('on');b.querySelector('span').textContent='Leído'}
    b.addEventListener('click',function(){var on=!b.classList.contains('on');b.classList.toggle('on',on);b.querySelector('span').textContent=on?'Leído':'Marcar como leído';set(b.dataset.id,on);progreso()});
  });
  progreso();
})();
"""


def head(title, extra=""):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><link rel="icon" href="favicon.svg"><style>{CSS}</style>{extra}</head><body>')


def topo(nav):
    links = "".join(f'<a href="{h}">{E(t)}</a>' for t, h in nav)
    return f'<header class="top"><div class="in"><a class="brand" href="#">Los 72 Ángeles<span>DE LA CÁBALA</span></a><nav>{links}</nav></div></header>'


def card(cid, img, tag, titulo, desc):
    return (f'<article class="card"><div class="cover"><img loading="lazy" src="{img}" width="600" height="800" alt="Portada: {E(titulo)}"></div>'
            f'<div class="body"><span class="tag">{E(tag)}</span><h3>{E(titulo)}</h3><p>{E(desc)}</p>'
            f'<a class="btn" data-link="{cid}" href="#">Abrir material</a>'
            f'<button class="done" data-id="{cid}" type="button"><i>✓</i><span>Marcar como leído</span></button></div></article>')


def links_block(keys):
    linhas = ",\n".join(f'  {k}: "{LINKS_DRIVE.get(k, "")}"' for k in keys)
    return f"<script>\nvar LINKS = {{\n{linhas}\n}};\n</script>"


def footer():
    return ('<footer>Material digital para uso personal. No se permite su reventa ni redistribución.<br>'
            'Material educativo y de reflexión personal; no garantiza resultados sobrenaturales.<br>© 2026 Los 72 Ángeles de la Cábala.</footer>')


BONOS = [
    ("bono1", "assets/bono-premium-01.webp", "Bono 01", "Las 72 Cartas Angélicas", "72 cartas con el nombre, la virtud y un mensaje breve de cada Ángel."),
    ("bono2", "assets/bono-premium-02.webp", "Bono 02", "Calendario de los 72 Ángeles", "Los 72 nombres organizados en los doce signos del ciclo simbólico del año."),
    ("bono3", "assets/bono-premium-03.webp", "Bono 03", "18 Oraciones Angélicas para la Vida", "Dieciocho oraciones originales para distintos momentos de la vida."),
    ("bono4", "assets/bono-premium-04.webp", "Bono 04", "Atlas de 24 Símbolos de la Cábala", "Conceptos de la tradición explicados con su contexto histórico."),
    ("bono5", "assets/bono-premium-05.webp", "Bono 05", "9 Contemplaciones para la Paz Interior", "Nueve lecturas ilustradas sobre serenidad, paciencia y equilibrio."),
]
LIBROS = [
    ("libro1", "assets/upsell/libro-1-portada.webp", "Libro I", "La Historia y los Misterios de la Cábala", "Orígenes, textos, maestros y evolución de una tradición mística."),
    ("libro2", "assets/upsell/libro-2-portada.webp", "Libro II", "El Árbol de la Vida", "Interpretaciones avanzadas, relaciones y sabiduría simbólica."),
    ("libro3", "assets/upsell/libro-3-portada.webp", "Libro III", "Las Cuatro Dimensiones del Mundo Cabalístico", "Emanación, creación, formación y acción."),
    ("libro4", "assets/upsell/libro-4-portada.webp", "Libro IV", "El Lenguaje de los Símbolos Místicos", "Imágenes, interpretación y significados en la tradición cabalística."),
    ("libro5", "assets/upsell/libro-5-portada.webp", "Libro V", "El Camino de la Sabiduría Cabalística", "Estudio, interpretación y reflexión a través de la tradición."),
]

PASSOS = ('<div class="steps"><div><span>PASO 1</span><b>Empieza por tu guía</b>Lee primero «Cómo utilizar esta guía» y el índice general.</div>'
          '<div><span>PASO 2</span><b>Un Ángel por día</b>Lee una ficha con calma y quédate con una frase o una pregunta.</div>'
          '<div><span>PASO 3</span><b>Explora los bonos</b>Úsalos para consultar, orar y profundizar a tu ritmo.</div></div>')
AJUDA = ('<div class="help"><div><h3>¿Cómo abro los materiales?</h3><p>Toca «Abrir material»: se abre en una nueva pestaña, donde puedes leerlo o descargarlo.</p></div>'
         '<div><h3>¿Puedo imprimirlos?</h3><p>Sí, para tu uso personal. Descarga el archivo y envíalo a tu impresora.</p></div>'
         '<div><h3>¿Necesitas ayuda?</h3><p>Escríbenos usando los datos de soporte que aparecen en el correo de tu compra en Hotmart.</p></div></div>')


def area():
    h = head("Área de miembros · Los 72 Ángeles de la Cábala")
    h += topo([("Mi guía", "#guia"), ("Bonos", "#bonos"), ("Biblioteca Premium", "#biblioteca")])
    h += ('<section class="hero"><p class="eyebrow">Área de miembros</p><h1>Te damos la bienvenida a tu espacio de estudio</h1>'
          '<p>Aquí tienes tu guía de los 72 Ángeles y tus 5 bonos. Guarda esta página en tus favoritos para volver cuando quieras.</p></section>')
    h += PASSOS + '<main class="wrap">'
    h += (f'<section class="sec" id="guia" data-grupo><div class="sec-head"><div><p class="eyebrow">Tu material principal</p><h2>Tu guía</h2></div></div>'
          f'<div class="main-card"><img src="assets/area/guia-portada.webp" width="600" height="800" alt="Portada de la guía Los 72 Ángeles de la Cábala">'
          f'<div><span class="tag">Guía principal</span><h3>Los 72 Ángeles de la Cábala</h3><p style="font-style:italic;color:var(--gold);margin:0 0 6px">Enciclopedia Visual y Espiritual</p>'
          f'<p>La introducción a la tradición, el índice completo y las 72 fichas: esencia, virtudes, cuándo consultarlo, oración inspirada y reflexión de cada Ángel.</p>'
          f'<div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:14px"><a class="btn gold" data-link="guia" href="#" style="min-width:220px">Abrir mi guía</a>'
          f'<button class="done" data-id="guia" type="button"><i>✓</i><span>Marcar como leído</span></button></div></div></div></section>')
    h += ('<section class="sec" id="bonos" data-grupo><div class="sec-head"><div><p class="eyebrow">Incluidos en tu acceso</p><h2>Tus 5 bonos</h2></div>'
          '<div class="progress">Leídos: <b class="js-n">0 de 5</b><div class="bar"><i></i></div></div></div>'
          f'<div class="grid">{"".join(card(*b) for b in BONOS)}</div></section>')
    capas = "".join(f'<img src="{l[1]}" width="600" height="800" alt="">' for l in LIBROS)
    h += (f'<section class="sec" id="biblioteca"><div class="lock"><div><p class="eyebrow" style="color:var(--gold2)">Colección complementaria</p>'
          f'<h3>Biblioteca Premium de la Cábala y sus Misterios</h3><p>¿Añadiste la Biblioteca a tu compra? Tu acceso exclusivo llegó en el correo de Hotmart: ábrelo desde el enlace del mensaje.</p>'
          f'<div class="acts"><a class="btn ghost" href="/upsell">Conocer la Biblioteca</a></div></div><div class="covers">{capas}</div></div></section>')
    h += AJUDA + "</main>" + footer() + links_block(["guia"] + [b[0] for b in BONOS]) + f"<script>{JS}</script></body></html>"
    return h


def biblioteca():
    h = head("Biblioteca Premium · Área de miembros")
    h += topo([("Biblioteca", "#libros"), ("Mi guía y bonos", "/areademembros")])
    h += ('<section class="hero"><p class="eyebrow">Área de miembros · Acceso exclusivo</p><h1>Biblioteca Premium de la Cábala y sus Misterios</h1>'
          '<p>Tus 5 libros ilustrados, listos para leer. Te recomendamos seguir el orden: de la historia de la tradición al camino del estudio.</p></section>')
    h += ('<div class="steps"><div><span>LIBRO I</span><b>Empieza por la historia</b>Conoce los textos y maestros que dieron forma a la Cábala.</div>'
          '<div><span>LIBROS II–IV</span><b>Explora las estructuras</b>El Árbol de la Vida, los cuatro mundos y el lenguaje de los símbolos.</div>'
          '<div><span>LIBRO V</span><b>Integra lo aprendido</b>Un método para estudiar la tradición con criterio.</div></div><main class="wrap">')
    h += ('<section class="sec" id="libros" data-grupo><div class="sec-head"><div><p class="eyebrow">Tu colección</p><h2>Los 5 libros</h2></div>'
          '<div class="progress">Leídos: <b class="js-n">0 de 5</b><div class="bar"><i></i></div></div></div>'
          f'<div class="grid">{"".join(card(*l) for l in LIBROS)}</div></section>')
    h += ('<section class="sec"><div class="lock"><div><p class="eyebrow" style="color:var(--gold2)">Tu material principal</p><h3>Tu guía de los 72 Ángeles y tus bonos</h3>'
          '<p>Están en tu área de miembros principal.</p><div class="acts"><a class="btn" href="/areademembros">Ir a mi guía y bonos</a></div></div>'
          f'<div class="covers"><img src="assets/area/guia-portada.webp" width="600" height="800" alt="">{"".join(f"<img src={chr(34)}{b[1]}{chr(34)} width=600 height=800 alt={chr(34)}{chr(34)}>" for b in BONOS[:3])}</div></div></section>')
    h += AJUDA + "</main>" + footer() + links_block([l[0] for l in LIBROS]) + f"<script>{JS}</script></body></html>"
    return h


def gracias():
    pixel = ('<script>!function(w,d){var f=w.fbq=function(){f.callMethod?f.callMethod.apply(f,arguments):f.queue.push(arguments)};w._fbq||(w._fbq=f);f.push=f;f.loaded=!0;f.version="2.0";f.queue=[];'
             'fbq("init","1791405689657118");fbq("track","PageView");function s(u){var e=d.createElement("script");e.async=!0;e.src=u;d.head.appendChild(e)}'
             'function go(){s("https://connect.facebook.net/en_US/fbevents.js")}d.readyState==="complete"?go():w.addEventListener("load",go)}(window,document)</script>')
    h = head("¡Gracias por tu compra! · Los 72 Ángeles de la Cábala")
    h += f'''<style>
.ty{{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:40px 20px;background:radial-gradient(circle at 50% 0,#1d3c56,var(--ink) 70%)}}
.box{{background:#fff;border-radius:20px;max-width:560px;width:100%;padding:40px 34px 34px;text-align:center;box-shadow:0 30px 70px #0006;position:relative}}
.seal{{width:74px;height:74px;border-radius:50%;background:var(--ok);color:#fff;font-size:38px;display:flex;align-items:center;justify-content:center;margin:-76px auto 16px;border:6px solid #fff;box-shadow:0 10px 24px #1f7a4d55}}
.box h1{{font-size:clamp(26px,5vw,34px)}}.box .btn{{font-size:16px;padding:18px;margin-top:22px}}
.list{{text-align:left;background:var(--ivory);border:1px solid #efe6d2;border-radius:12px;padding:14px 18px;margin-top:18px;font-size:14.5px;color:var(--muted)}}
.list li{{margin:6px 0}}.count{{font-size:13px;color:var(--muted);margin-top:12px}}
</style>
<div class="ty"><div class="box"><div class="seal">✓</div>
<p class="eyebrow">Compra confirmada</p><h1>¡Gracias! Tu acceso ya está listo</h1>
<p>Entra ahora a tu área de miembros para empezar a leer tu guía de los 72 Ángeles y tus bonos.</p>
<a class="btn gold" id="entrar" href="/areademembros">ENTRAR A MI ÁREA DE MIEMBROS</a>
<p class="count" id="count">Te llevaremos automáticamente en <b>8</b> segundos…</p>
<ul class="list"><li>📧 También recibirás un correo de Hotmart con los datos de tu compra.</li>
<li>⭐ Guarda tu área de miembros en favoritos para volver cuando quieras.</li>
<li>📚 Si añadiste la Biblioteca Premium, su acceso llega en el mismo correo.</li></ul>
</div></div>
<script>(function(){{var n=8,b=document.querySelector('#count b');var t=setInterval(function(){{n--;if(b)b.textContent=n;if(n<=0){{clearInterval(t);location.href='/areademembros'}}}},1000);
document.getElementById('entrar').addEventListener('click',function(){{clearInterval(t)}})}})();</script>{pixel}</body></html>'''
    return h


if __name__ == "__main__":
    for nome, conteudo in [("areademembros.html", area()), (f"{SLUG_BIBLIOTECA}.html", biblioteca()), ("gracias.html", gracias())]:
        open(os.path.join(SITE, nome), "w", encoding="utf-8", newline="\n").write(conteudo)
        print(nome, len(conteudo))
