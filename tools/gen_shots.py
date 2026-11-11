# -*- coding: utf-8 -*-
"""生成 13 个分镜演示页（每个镜头一个自包含 HTML，统一播放器底盘）。"""
import json
import os

OUT = r"C:\Users\24252\Desktop\wx-pages\shots"
os.makedirs(OUT, exist_ok=True)

SANS = '"PingFang SC","Microsoft YaHei","Hiragino Sans GB",sans-serif'
SERIF = '"Songti SC","SimSun","Noto Serif SC",serif'
MONO = 'Consolas,"Courier New",monospace'
DISPLAY = '"Impact","Haettenschweiler","Arial Black",sans-serif'

CHASSIS = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;background:#07070a;overflow:hidden}
#wrap{position:fixed;inset:0;overflow:hidden}
#stage{width:1920px;height:1080px;position:absolute;left:50%;top:50%;overflow:hidden;
  transform:translate(-50%,-50%) scale(1);transform-origin:center center;
  background:__BG__;color:__INK__;
  font-family:__FONT__}
.fx{opacity:0;transform:translateY(__SHIFT__);transition:opacity .72s ease,transform .82s cubic-bezier(.2,.75,.2,1)}
.fx.on{opacity:1;transform:none}
.fx.d1{transition-delay:.06s}.fx.d2{transition-delay:.12s}.fx.d3{transition-delay:.18s}
#hud{position:absolute;left:0;right:0;bottom:0;height:5px;background:rgba(255,255,255,.10);z-index:6}
#bar{height:100%;width:0;background:__ACCENT__}
#hint{position:absolute;right:26px;bottom:22px;font:500 15px/1 __MONO__;letter-spacing:.18em;
  color:__MUTED__;opacity:0;transition:opacity .6s ease;z-index:6}
#hint.on{opacity:.85}
#start{position:absolute;inset:0;background:#050507;display:grid;place-items:center;
  z-index:9;cursor:pointer;transition:opacity .8s ease}
#start.gone{opacity:0;pointer-events:none}
#start .t{color:#e9e6df;font:600 40px/1.5 __SANS__;letter-spacing:.42em;text-indent:.42em}
#start .s{margin-top:22px;color:#6f6a63;font:400 18px/1.6 __MONO__;letter-spacing:.2em;text-align:center}
__CSS__
</style>
</head>
<body>
<div id="wrap"><div id="stage">
__BODY__
<div id="hud"><div id="bar"></div></div>
<div id="hint">SPACE 暂停 · 点右下角重播</div>
<div id="start"><div><div class="t">点 击 开 始 播 放</div>
<div class="s">__SUB__</div></div></div>
</div></div>
<script>
var DUR = __DUR__, CUES = __CUES__;
var stage = document.getElementById('stage'), bar = document.getElementById('bar');
var startEl = document.getElementById('start'), hintEl = document.getElementById('hint');
var playing = false, t0 = 0, elapsed = 0, paused = false, done = {}, timer = null;
function fit(){
  var s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
  stage.style.transform = 'translate(-50%,-50%) scale(' + s + ')';
}
window.addEventListener('resize', fit); fit();
function run(c){
  var el = document.querySelector(c.sel);
  if(!el) return;
  if(c.act === 'on'){ el.classList.add('on');
    var hv = el.style.getPropertyValue('--h'); if(hv){ el.style.height = hv; } }
  else if(c.act === 'w'){ el.style.width = c.arg + '%'; el.style.transition = 'width 1.05s cubic-bezier(.2,.8,.2,1)'; }
  else if(c.act === 'h'){ el.style.height = c.arg + '%'; el.style.transition = 'height 1.15s cubic-bezier(.2,.8,.2,1)'; }
  else if(c.act === 'cls'){ el.classList.add(c.arg); }
  else if(c.act === 'count'){
    var to = c.arg, dec = c.dec || 0, dur = 900, s0 = Date.now();
    var id = setInterval(function(){
      var k = Math.min(1, (Date.now() - s0) / dur);
      var v = to * (1 - Math.pow(1 - k, 3));
      el.textContent = v.toLocaleString('en-US', {minimumFractionDigits: dec, maximumFractionDigits: dec});
      if(k >= 1) clearInterval(id);
    }, 33);
  }
}
function tick(){
  if(!playing){ if(timer){ clearInterval(timer); timer = null; } return; }
  var now = Date.now();
  if(!paused){
    if(!t0) t0 = now;
    elapsed += now - t0; t0 = now;
    for(var i = 0; i < CUES.length; i++){
      var c = CUES[i];
      if(!done[i] && elapsed >= c.t){ done[i] = 1; run(c); }
    }
    bar.style.width = Math.min(100, elapsed / DUR * 100) + '%';
    if(elapsed >= DUR){
      playing = false; hintEl.classList.add('on'); hintEl.textContent = '重 播';
      hintEl.style.pointerEvents = 'auto'; hintEl.style.cursor = 'pointer';
      if(timer){ clearInterval(timer); timer = null; }
      return;
    }
  } else { t0 = now; }
}
function play(){
  startEl.classList.add('gone');
  playing = true; elapsed = 0; t0 = 0; done = {}; paused = false;
  bar.style.width = '0%'; hintEl.classList.remove('on');
  document.querySelectorAll('.fx').forEach(function(e){ e.classList.remove('on'); });
  if(timer) clearInterval(timer);
  timer = setInterval(tick, 16);
}
startEl.addEventListener('click', play);
if(__AUTO__){ setTimeout(play, 60); }
hintEl.addEventListener('click', function(){ if(hintEl.textContent.indexOf('重') >= 0) play(); });
window.addEventListener('keydown', function(e){
  if(e.code === 'Space'){ e.preventDefault();
    if(!playing){ play(); return; }
    paused = !paused;
    document.querySelectorAll('.fx').forEach(function(el){
      el.style.transitionDuration = paused ? '0s' : '';
    });
  }
});
</script>
</body>
</html>
"""


def page(shot, auto=False):
    return (CHASSIS
            .replace("__TITLE__", shot["title"])
            .replace("__BG__", shot["bg"])
            .replace("__INK__", shot["ink"])
            .replace("__FONT__", shot["font"])
            .replace("__MONO__", MONO)
            .replace("__SANS__", SANS)
            .replace("__SERIF__", SERIF)
            .replace("__DISPLAY__", DISPLAY)
            .replace("__SHIFT__", shot.get("shift", "26px"))
            .replace("__ACCENT__", shot["accent"])
            .replace("__MUTED__", shot["muted"])
            .replace("__SUB__", shot["sub"] if "sub" in shot else "")
            .replace("__CSS__", shot["css"])
            .replace("__BODY__", shot["body"])
            .replace("__DUR__", str(int(shot["dur"] * 1000)))
            .replace("__CUES__", json.dumps(shot["cues"], ensure_ascii=False))
            .replace("__AUTO__", "true" if auto else "false"))


import shots_a, shots_b, shots_c
SHOTS = shots_a.SHOTS + shots_b.SHOTS + shots_c.SHOTS

QC = os.path.join(OUT, "_qc")
os.makedirs(QC, exist_ok=True)

for s in SHOTS:
    name = "shot-%s.html" % s["id"]
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(page(s))
    with open(os.path.join(QC, name), "w", encoding="utf-8") as f:
        f.write(page(s, auto=True))
    print("wrote", name, len(page(s)))